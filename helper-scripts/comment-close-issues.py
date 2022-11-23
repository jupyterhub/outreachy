import os
import sys
import requests
import typer

# https://typer.tiangolo.com/tutorial/exceptions/#disable-local-variables-for-security
app = typer.Typer(pretty_exceptions_show_locals=False)


def construct_root_api_url(repo: str):
    return "/".join(["https://api.github.com/repos", repo])


@app.command()
def main(
    issue_labels: list[str],
    full_repo_name: str = "jupyterhub/outreachy",
    comment_body: str = "Thank you for your contribution! Since the contribution period is now over, we will close this issue."
):
    """
    Loop over a list of GitHub issues that have specific labels, leave a comment
    on each issue, then close it.
    """
    token = os.environ.get("GITHUB_TOKEN", None)
    if token is None:
        raise ValueError(
            "GITHUB_TOKEN must be set to a GitHub API token with at least read/write permissions for issues"
        )

    root_url = construct_root_api_url(full_repo_name)

    # Set the HTTP headers
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {token}",
    }    

    # List all issues on full_repo_name that have labels issues_labels
    url = "/".join([root_url, "issues"])
    params = {"labels": issue_labels, "per_page": 100}
    all_issues = requests.get(url, params=params, headers=headers)
    if not all_issues.ok:
        sys.exit(
            f"Could not list requested issues"
            + f"\n\tStatus: {all_issues.status}"
            + f"\n\tMessage: {all_issues.text}"
        )

    for issue in all_issues.json():
        # Post a comment to the issue
        resp = requests.post(
            issue["comments_url"], json={"body": comment_body}, headers=headers
        )
        if not resp.ok:
            print(
                f"Could not comment on issue: {issue['html_url']}"
                + f"\n\tStatus: {resp.status}"
                + f"\n\tMessage: {resp.text}"
                + "\nSkipping to next issue..."
            )
            continue

        # Close the issue
        resp = requests.patch(
            issue["url"], json={"state": "closed"}, headers=headers
        )
        if not resp.ok:
            print(
                f"Could not close issue: {issue['html_url']}"
                + f"\n\tStatus: {resp.status}"
                + f"\n\tMessage: {resp.text}"
                + "\nSkipping to next issue..."
            )
            continue


if __name__ == "__main__":
    app()
