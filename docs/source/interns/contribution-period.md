(contrib:applicants)=

# Contributing to JupyterHub

This guide should help you get with contributing to JupyterHub during the
contribution period as an Outreachy applicant.

(contrib:applicants:get-started)=

## Getting started

If you are new to the JupyterHub project, our
[contributor guide](https://jupyterhub-team-compass.readthedocs.io/en/latest/index-team_guides.html)
contains a lot of resources to help you get started. A few sections you should
specifically read are:

- [Get started contributing](https://jupyterhub-team-compass.readthedocs.io/en/latest/contribute/guide.html)
  covers a lot about our community channels and GitHub practices
- [Useful skills and ways to contribute](https://jupyterhub-team-compass.readthedocs.io/en/latest/contribute/skills.html)
  discusses how you can start off with your first contributions

As you begin to put together your first pull request, these resources may come
in handy:

- [GitHub flow](https://docs.github.com/en/get-started/quickstart/github-flow):
  This is a common git/GitHub-based workflow use across Jupyter and other open
  source projects, so it's a valuable thing to learn
- [Write informative commit messages](https://www.freecodecamp.org/news/how-to-write-better-git-commit-messages/):
  This blog post describes why git commit messages are important and how you
  can write informative ones. This advice goes for pull requests too! Always
  update the pull request title with _what_ it will change, and describe _why_
  you're making the change in the body of the pull request.
- [Practice self-review](https://blog.beanbaginc.com/2014/12/01/practicing-effective-self-review/):
  Checking your own changes against a repository's contributing guidelines first
  will help catch any minor issues before someone else reviews it. This will
  help your pull requests be merged faster, and folks will appreciate the quality
  and professionalism of your work.
- [Ask good questions](https://stackoverflow.com/help/how-to-ask): It's very
  hard to answer a general question like "How do I do this issue?" When asking
  for help, explain your current understanding, including what you've done or
  tried so far, and where you got stuck. Provide tracebacks or other error
  messages if appropriate.

(contrib:applicants:issues)=

## Contribution issues

The JupyterHub team create specific contribution issues, or "microtasks", for
Outreachy applicants to complete during the contribution period.

### Where to find them

We define all microtasks in the issues of the `jupyterhub/outreachy` repository:
<https://github.com/jupyterhub/outreachy/issues> We use a
[labelling system](microtasks:create:labels) to distinguish microtasks from each
other, and other types of issues in the repo.

### How to choose one

Each microtask will have a standard layout that will tell you:

- How many applicants can work on the issue simultaneously
- What work, if any, you will need to have completed before attempting the task
- The maximum number of times you should complete a task before moving on
  (Note: This is a _hard limit_ to discourage flooding of contributions. It is
  **not** a _target to be met_.)
- What the task is and step by step instructions on completing it
- What you should specifically record in Outreachy as a contribution after
  completing the task
- What you can work on next

This should give you a good idea of whether or not you want to tackle that issue.

You should also look out for the following labels:

- The `level: <level>` labels will tell you how difficult the task is. You may
  wish to start with `beginner` level tasks and work your way up.
- The `project:` labels will tell you which project the microtasks are
  associated with. You should, at a minimum, try to complete the tasks linked to
  the project you want to apply for as this will help the mentors evaluate
  whether you are a good fit for the project.

```{attention}
We tend to limit the number of microtasks that a single applicant can work on
as this generates a lot of overhead for the mentors to keep track of who is
working on what.

For microtasks that allow multiple applicants, **we will not be assigning the
issue to anyone**. You don't need to ask permission to begin working, just begin
:)
```

### What to work on next

Each microtask should list what you should move onto next. If it doesn't, or you
have completed all the microtasks, then there are a few other things you can you
do:

- Help answer questions in [Discourse](https://discourse.jupyter.org) or
  [Gitter](https://gitter.im/jupyterhub/jupyterhub)
- Review other applicants' pull requests
- Begin [](application-prep)

```{caution}
You are _allowed_ to begin working on any `help wanted` or `good first issue`
labelled issues you find across the JupyterHub organisation. But these issues
have not been scoped for Outreachy, and could be more complex to start working
on or become unclear very quickly. The JupyterHub team are here to help, but you
should prioritise completing the Outreachy tasks first.
```
