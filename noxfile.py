"""
A nox configuration file so that we can build the documentation easily with nox.
- see the README.md for information about nox.
- ref: https://nox.thea.codes
"""
import nox

nox.options.reuse_existing_virtualenvs = True

BUILD_COMMAND = ["-b", "html", "docs/source", "docs/_build/html"]


def install_deps(session):
    session.conda_install("python=3.10")
    session.install("-r", "docs/requirements.txt")
    session.install("-r", "helper-scripts/requirements.txt")


@nox.session(venv_backend="conda")
def docs(session):
    install_deps(session)

    if "live" in session.posargs:
        # Add relative paths here if we ever need to ignore them during autobuilds
        AUTOBUILD_IGNORE = [
            "docs/_build",
            "docs/source/tmp",
        ]

        cmd = ["sphinx-autobuild"]
        for folder in AUTOBUILD_IGNORE:
            cmd.extend(["--ignore", f"*/{folder}/*"])

        cmd.extend(BUILD_COMMAND)
        session.run(*cmd)

    else:
        session.run("sphinx-build", *BUILD_COMMAND)
