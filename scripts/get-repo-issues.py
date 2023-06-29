import os
from pathlib import Path
from typing import List

import pandas as pd
import requests

PATH = Path(__file__).parent.parent


def get_github_token():
    """If a GITHUB_TOKEN environment variable exists, return its value. Else
    return None.
    """
    return os.environ.get("GITHUB_TOKEN", None)


def set_http_headers():
    """Set headers for HTTP requests against GitHub's REST API"""
    # Set the HTTP headers
    headers = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }

    # See if there's a GitHub token in the environment and add it to the headers
    token = get_github_token()
    if token is not None:
        headers["Authorization"] = f"Bearer {token}"

    return headers


def get_next_page(page):
    """
    Check if a page of a HTTP response has 'Link' in its headers, indicating
    another page of results
    """
    return page if page.headers.get("link") is not None else None


def get_repo_issues(repo: str, headers: dict = {}, params: dict = {}):
    """Return issues from a GitHub repository. Paginate over results until there
    are no more.

    Args:
        repo (str): The name of the repository to pull issues for, in the format
            `OWNER/REPO`
        headers (dict, optional): Headers to pass to the GET request. Defaults
            to {}.
        params (dict, optional): Query parameters to pass to the GET request.
            Defaults to {}.
    """
    session = requests.Session()

    url = f"https://api.github.com/repos/{repo}/issues"

    first_page = session.get(url, headers=headers, params=params)
    yield first_page

    next_page = first_page
    while get_next_page(next_page) is not None:
        try:
            next_page_url = next_page.links["next"]["url"]
            next_page = session.get(next_page_url, headers=headers, params=params)
            yield next_page

        except KeyError:
            break


def get_microtask_issues(
    full_repo_name: str = "jupyterhub/outreachy",
    issue_labels: List[str] = ["microtask"],
):
    # Set the HTTP headers
    headers = set_http_headers()

    # Set the query parameters
    params = {
        "labels": issue_labels,
        "state": "open",
    }

    issues = []
    for page in get_repo_issues(full_repo_name, headers=headers, params=params):
        issues.extend(page.json())

    issue_list = []
    for i, issue in enumerate(issues):
        labels = [label["name"] for label in issue["labels"]]

        project_label = next(
            (label for label in labels if label.startswith("project:")),
            None,
        )
        if project_label is not None:
            project_label = f'<img src="https://img.shields.io/github/labels/{full_repo_name}/{project_label.replace(" ", "%20")}">'

        level_label = next(
            (label for label in labels if label.startswith("level:")),
            None,
        )
        if level_label is not None:
            level_label = f'<img src="https://img.shields.io/github/labels/{full_repo_name}/{level_label.replace(" ", "%20")}">'

        issue_list.append(
            {
                "Title": f'<a href="{issue["html_url"]}">{issue["title"]}</a>',
                "Project": project_label,
                "Multiple applicants permitted?": "Yes"
                if "multiple" in labels
                else "No",
                "Difficulty level": level_label,
            }
        )

    # Convert list to dataframe
    df = pd.DataFrame(issue_list)

    # Write the dataframe to a CSV file that can be read by sphinx
    path_table = PATH.joinpath("microtask-table.csv")
    df.to_csv(path_table, index=None)


def get_project_proposal_issues(
    full_repo_name: str = "jupyterhub/outreachy",
    issue_labels: List[str] = ["project-proposal"],
):
    # Set the HTTP headers
    headers = set_http_headers()

    # Set the query parameters
    params = {
        "labels": issue_labels,
        "state": "open",
    }

    issues = []
    for page in get_repo_issues(full_repo_name, headers=headers, params=params):
        issues.extend(page.json())

    issue_list = []
    for i, issue in enumerate(issues):
        labels = [label["name"] for label in issue["labels"]]

        status_label = next(
            (label for label in labels if label.startswith("status:")),
            None,
        )
        if status_label is not None:
            status_label = f'<img src="https://img.shields.io/github/labels/{full_repo_name}/{status_label.replace(" ", "%20")}">'

        issue_list.append(
            {
                "Title": f'<a href="{issue["html_url"]}">{issue["title"]}</a>',
                "Status": status_label,
                "Looking for a Mentor?": "Yes" if "needs: mentor" in labels else "No",
            }
        )

    # Convert list to dataframe
    df = pd.DataFrame(issue_list)

    # Write the dataframe to a CSV file that can be read by sphinx
    path_table = PATH.joinpath("project-table.csv")
    df.to_csv(path_table, index=None)


if __name__ == "__main__":
    get_microtask_issues()
    get_project_proposal_issues()
