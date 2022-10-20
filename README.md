# Outreachy organization repo for JupyterHub

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

Make sure you have [`conda` installed](https://conda.io/projects/conda/en/latest/user-guide/install/index.html) on your system.
We recommend using [`miniconda`](https://docs.conda.io/en/latest/miniconda.html).

1. Create a new `conda` environment called `outreachy` that is running Python v3.10

   ```bash
   conda create -n outreachy python=3.10
   ```

2. Activate the new environment

   ```bash
   conda activate outreachy
   ```

3. Change into the `docs` folder and install the requirements

   ```bash
   cd docs
   pip install -r requirements.txt
   ```

4. Build the HTML (still within the `docs` folder)

   ```bash
   make html
   ```

5. Open the HTML file in your browser

   ```bash
   open _build/html/index.html
   ```

You can check external links within the site by running:

```bash
make linkcheck
```

You can clean-up any generated files by running:

```bash
make clean
```

## Code of Conduct

We follow the [Project Jupyter Code of Conduct](https://github.com/jupyter/governance/blob/master/conduct/code_of_conduct.md).
