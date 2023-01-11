(microtasks)=

# Creating Microtasks for the Contribution Period

For the contribution period, mentors need to create a set of tasks ("microtasks")
for applicants to complete.

## Guidelines for designing microtasks

Here are some guidelines to consider when designing microtasks.

- **Primarily, microtasks should allow mentors _assess what the applicant can do_
  within the problem space of the project**
  - Giving the applicant information and a chance to practice specific tools
    related to the project is important, but should be a secondary goal.
    Mentors will need to evaluate these contributions in order to decide who to
    offer the internship to, so ensuring sufficient output for differentiating
    applicants is critical.
- **Have applicants complete similar/the same microtasks**
  - This is beneficial for two reasons:
    - firstly, we will be able to directly compare applicants that complete the
      tasks;
    - and secondly, it will reduce the overhead of tracking who is working on
      which task, assigning them to it, chasing them up if other applicants are
      asking about it, etc.
- **Have "levels" of microtasks and pathways that an applicant can grow through**
  - Start with some simple tasks that applicants can build confidence with, and
    work up to larger, more open ended tasks that are more challenging
  - The open ended tasks will give each applicant more to do per contribution,
    as well as provide mentors more information to evaluate
  - If the task involves making a pull request, the open/review/iterate/merge
    flow is really valuable
- **Limit the number of times an applicant can complete a specific microtask**
  - Some applicants submit a lot of contributions hoping for quantity over
    quality, which is not really in the spirit of the kinds of contributions
    we'd like to see. Limiting the number of times an applicant can complete
    a given microtask, especially the simpler ones, before moving onto harder
    tasks will help in two ways: not inundating mentors with lots of
    contributions to review, and provide meaningful information to evaluate.

```{admonition} This is really hard!
:class: attention
Designing microtasks that provide useful information is a really hard task that
will vary from project to project. It's encouraged for mentors to help each
other out, speak to other Outreachy mentors on the [Zulip chat](https://chat.outreachy.org),
or reach out to our [partners](partners) for help.
```

### Examples of contribution tasks

To help you in designing microtasks, here is
[Wikimedia's guidance on good first tasks](https://phabricator.wikimedia.org/project/view/169/)
including David Humphrey's blog post on
[Why Good-First-Bugs often aren't](https://blog.humphd.org/why-good-first-bugs-often-arent/),
alongside some example tasks from the Wikimedia and Zulip communities:

- [Wikimedia: Build python library to work with html-dumps](https://phabricator.wikimedia.org/T302242)
- [Wikimedia: Complete PAWS notebook tutorial](https://phabricator.wikimedia.org/T276274)
- [Wikimedia: Pick a MediaWiki Action API to review and improve](https://phabricator.wikimedia.org/T205199)
- [Zulip: Fix vertical alignment in /me messages](https://github.com/zulip/zulip/issues/23101)

(microtasks:create)=

## Creating the microtasks on our Outreachy repo

We centralise the microtasks on [our Outreachy repo](https://github.com/jupyterhub/outreachy)
in order to reduce the number of places applicants and mentors need to check
for information. There is an [issue form](https://github.com/jupyterhub/outreachy/issues/new?assignees=&labels=microtask&template=new-contribution-task.yaml&title=%5BOutreachy+Task%5D%3A+)
for mentors to complete to create a new microtask. It should lead you through
providing all the information an applicant will need to complete the task.

(microtasks:create:labels)=

### Labelling the microtasks

We use labels to distinguish microtasks related to different projects from one
another, and also their level of difficulty. This is because we can generate
a URL that filters issues on labels and can be easily distributed. For example
`https://github.com/jupyterhub/outreachy/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc+label%3Amicrotask`

- ![GitHub labels](https://img.shields.io/github/labels/jupyterhub/outreachy/microtask):
  Each new microtask created with the form receives this label
- ![GitHub labels](https://img.shields.io/github/labels/jupyterhub/outreachy/multiple):
  If multiple applicants can work on the microtask simultaneously, apply this
  label to signal boost that
- Level labels: We have three level labels that can be used to distinguish
  the level of difficulty between related microtasks. These are:
  - ![GitHub labels](https://img.shields.io/github/labels/jupyterhub/outreachy/level:%20beginner)
  - ![GitHub labels](https://img.shields.io/github/labels/jupyterhub/outreachy/level:%20intermediate)
  - ![GitHub labels](https://img.shields.io/github/labels/jupyterhub/outreachy/level:%20advanced)
- Project labels: Each project should have it's own label defined in the repo
  with the format `project: <keywords about the project>` to help distinguish
  which tasks belong to which projects. For example,
  ![GitHub labels](https://img.shields.io/github/labels/jupyterhub/outreachy/project:%20improve-accessibility).
  Feel free to create one if one doesn't exist.
- Cohort labels: Applying a label that idententifies the cohort the issue is a
  part of can be useful. For example,
  ![GitHub labels](https://img.shields.io/github/labels/jupyterhub/outreachy/outreachy-dec22)
  refers to all the issues that were a part of the December 2022 internship
  cohort.
- ![GitHub labels](https://img.shields.io/github/labels/jupyterhub/outreachy/needs:%20review):
  This label can be useful to signal boost to mentors that an issue or pull
  request needs review

(microtasks:create:issue-forms)=

### Creating issue forms for applicants to use

As part of your microtask, you may want an applicant to open an issue
demonstrating their work, rather than a pull request. Maybe because the work
involves making a fork or starting a new repo. For example, see
[this accessibility task](https://github.com/jupyterhub/outreachy/issues/38)
(step 6).

Mentors should feel free to create new
[issue forms](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/syntax-for-issue-forms)
in the repo that walk an
applicant through what they need to provide to complete the task. Some examples
of such forms from previous contribution periods can be viewed in the
[archive folder](https://github.com/jupyterhub/outreachy/tree/HEAD/.github/ISSUE_TEMPLATE/archive).

```{admonition} Issue form conventions
When creating these forms, please follow these conventions if you can:

- The title of the issue form should begin "Applicant:" to indicate that
  it is for the applicant to complete, and distinguish it from our "Mentor:"
  forms
- In the issue form filename, please add a prefix beginning with `0`, such as
  `00-accessibility-project-task.yaml` and `01-documentation-project-task.yaml`.
  This ordering will ensure that your form will appear at the top of the
  template chooser and be easier for the applicants to find.
- Ensure your project's label is automatically applied, along with `needs:
  review` and a cohort-based label if available.
```

### Reducing merge conflicts for pull requests

We may wish for our applicants to do a similar task across many different files,
and create a pull request. We would like to minimise the number of applicants
working on the same file in order to reduce merge conflicts so the pull requests
are easier to review and more manageable for the applicant.

In the past, we have used
[a spreadsheet](https://docs.google.com/spreadsheets/d/1pHg2igoZOCwF4GOEEDblLJ_e29OIRgUkvtKz2bTcOmM/edit?usp=sharing)
to list all the possible _somethings_ (e.g., files) that an applicant could work
on. They are instructed to "claim" a _something_ by putting their GitHub handle
next to it in the "Work in Progress" column, and when their pull request has
been reviewed and merged, "release" that _something_ for someone else to work on
by moving their handle to the "Done" column.

This method requires **very clear** instructions embedded into the microtask
issue, and reminders to the applicants to keep the spreadsheet updated.
However, it does reduce the overhead of mentors needing to manually assign
applicants to certain tasks.

```{admonition} In beta!
:class: warning

This system is not perfect. We found that either applicants were not updating
the spreadsheet properly, or there was some kind of race condition happening
where many PRs addressing the same file were opened at a similar time very
soon after they were "released" in the spreadsheet.

Iterations, improvements or alternative solutions to this process are very
welcome!
```
