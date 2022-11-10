# Helper Scripts

This folder contains some helper scripts to automate some tasks related to
Outreachy. They are primarily written in Python and all the requirements to
run the scripts are listed in the [requirements file](./requirements.txt).

## Closing microtask issues after the contribution period has closed

For contribution microtasks, we may ask applicants to open issues using a
template to demonstrate work they have done. This can lead to a lot of open
issues open on the repo that are no longer useful once the contribution
period has closed. The `comment-close-issues.py` script will pull a list of all
open issues on the repo that match a list of defined labels, it will loop
through them and post a comment thanking the applicant for their contribution,
and then close the issue.

```{bash}
Usage: comment-close-issues.py [OPTIONS] ISSUE_LABELS...                                           
                                                                                                    
 Loop over a list of GitHub issues that have specific labels, leave a comment on each issue, then   
 close it.                                                                                          
                                                                                                    
╭─ Arguments ──────────────────────────────────────────────────────────────────────────────────────╮
│ *    issue_labels      ISSUE_LABELS...  [default: None] [required]                               │
╰──────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Options ────────────────────────────────────────────────────────────────────────────────────────╮
│ --full-repo-name        TEXT  [default: jupyterhub/outreachy]                                    │
│ --comment-body          TEXT  [default: Thank you for your contribution! Since the contribution  │
│                               period is now over, we will close this issue.]                     │
│ --help                        Show this message and exit.                                        │
╰──────────────────────────────────────────────────────────────────────────────────────────────────╯
```