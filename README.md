# Outreachy organization repo for JupyterHub

|                                 |                                                                                                            |
| :------------------------------ | :--------------------------------------------------------------------------------------------------------: |
| Chat room for Outreachy interns | [![](https://img.shields.io/badge/chat-outreachy%20interns-green)](https://gitter.im/jupyterhub/outreachy) |

This repository contains information about JupyterHub's
participation in [Outreachy](https://www.outreachy.org/) - a
program that provides three-month internships for people from
groups traditionally underrepresented in tech.

This GitHub repository contains:

1. **Microtasks** for applicants to complete. These are small
   tasks that help the applicant familiarize themself with
   the project they are contributing to. These are accepted
   as GitHub issues.
2. Descriptions for various **Projects Ideas** that applicants can
   apply for. Maintainers can use this space to collaborate on
   keeping these descriptions up to date.
3. **Documentation** describing the processes that the JupyterHub
   community follow when participating in Outreachy rounds.

## How to Build the Documentation Locally

You will need a Python installation and the [`nox` package](https://nox.thea.codes/) installed.

1. Install `nox` via `pip`

   ```bash
   pip install nox
   ```

2. Build the documentation

   ```bash
   nox -s docs
   ```

   You can open the `docs/_build/html/index.html` file in your local browser to
   view the site.

Alternatively, you can watch the `docs` folder for changes and have a copy of
the site live update as you work.

1. Autobuild the documentation

   ```bash
   nox -s docs -- live
   ```

2. Open `http://127.0.0.1:8000` in your browser to see the site in real time

### Check for broken links

You can check for broken links within the documentation by changing into the
`docs` folder and running the linkcheck command.

```bash
cd docs
make linkcheck
```

### Cleaning up generated files

There are two methods of cleaning up generated files.

1. Using Sphinx

   ```bash
   cd docs
   make clean
   ```

2. Using git. Delete untracked files (`-X`), with required confirmation (`-f`),
   recursively (`-d`).

   ```bash
   git clean -Xfd
   ```

## Code of Conduct

We follow the [Project Jupyter Code of Conduct](https://github.com/jupyter/governance/blob/master/conduct/code_of_conduct.md).
