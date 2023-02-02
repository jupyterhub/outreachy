from pathlib import Path

import pandas as pd
import requests

PATH_ROOT = Path(__file__).parent.parent.parent
PATH_TMP = PATH_ROOT.joinpath("tmp")
PATH_TMP.mkdir(exist_ok=True)


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
    issue_labels: list[str] = ["microtask"],
):
    # Set the HTTP headers
    headers = {"Accept": "application/vnd.github+json"}

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
            project_label = f"![GitHub labels](https://img.shields.io/github/labels/{full_repo_name}/{project_label.replace(' ', '%20')})"

        level_label = next(
            (label for label in labels if label.startswith("level:")),
            None,
        )
        if level_label is not None:
            level_label = f"![GitHub labels](https://img.shields.io/github/labels/{full_repo_name}/{level_label.replace(' ', '%20')})"

        issue_list.append(
            {
                "Title": f"[{issue['title']}]({issue['html_url']})",
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
    path_table = PATH_TMP.joinpath("microtask-table.csv")
    df.to_csv(path_table, index=None)


if __name__ == "__main__":
    get_microtask_issues()
