(proposing-projects)=

# Proposing an Outreachy Project

## Who can submit a project proposal

Anyone in the JupyterHub community can submit a project proposal by following
the process outlined below. **Just because you have a project idea, it does not
mean that you are required to mentor it.** In an ideal world, those who propose
projects would also mentor them. However, the world is not ideal and sometimes
folk don't have the time to mentor even if they have a good project idea.
Instead, we can hopefully generate a board of project ideas that can provide
inspiration to those _who do_ have the capacity to mentor.

```{seealso}
You can view the [](project-list)
```

(proposing-projects:process)=

## Project proposal and scoping process

(proposing-projects:labels)=

### Labelling project proposals

We use labels to distinguish projects from one other types of issues on the
repository, and their status with regards to scoping and submission. This is
because we can generate a URL that filters issues on labels and can be easily
distributed. For example
`https://github.com/jupyterhub/outreachy/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc+label%3Aproject-proposal`

- ![GitHub labels](https://img.shields.io/github/labels/jupyterhub/outreachy/project-proposal):
  Each new project proposal created with the form receives this label
- ![GitHub labels](https://img.shields.io/github/labels/jupyterhub/outreachy/needs:%20mentor):
  If the project proposal is in need of a mentor to steward it through the
  Outreachy round, this label can be used to signal boost that need
- Status labels: We have various status labels that can be used to differentiate
  where a project proposal is within the . These are:
  - ![GitHub labels](https://img.shields.io/github/labels/jupyterhub/outreachy/status:%20scoping):
    The proposal is still being scoped and written up
  - ![GitHub labels](https://img.shields.io/github/labels/jupyterhub/outreachy/status:%20submitted):
    This project proposal has been submitted to the Outreachy platform and will
    be receiving applications
  - ![GitHub labels](https://img.shields.io/github/labels/jupyterhub/outreachy/status:%20intern%20assigned):
    This project proposal was successful in finding a suitable intern and **will**
    be mentored
  - ![GitHub labels](https://img.shields.io/github/labels/jupyterhub/outreachy/status:%20no%20intern%20found):
    A suitable intern was not found for this project proposal and **will not** be
    mentored. These project proposals may be resubmitted to future rounds.

### Claiming a project proposal in need of a mentor

If you would like to claim a project proposal that is looking for a mentor:

1. Comment on the relevant issue stating that you would like to mentor this
   project
2. Check with the original proposer regarding their capcity to mentor? Would
   they like to co-mentor the project with you, or do they have no capacity at
   all?
3. Remove the `needs: mentor` label from the issue
4. Begin scoping the project and completing the project proposal template. The
   original proposer may have some cycles to help do this if they had a specific
   vision.

(proposing-projects:submitting)=

## Submitting the project to the Outreachy platform

### Resubmitting an unsuccessful project proposal

If a project proposal was unsuccessful in finding a suitable intern, the
following actions should be taken:

1. Add the `status: no intern found` label to the issue
2. If you are the original proposer and you have capacity to mentor in the next
   round, notify your [Community Coordinator](comm-coord) that you will be
   resubmitting the proposal
3. If you **do not** have capacity to mentor the next round, add the
   `needs: mentor` label to indicate that the proposal is available to be claimed

(proposing-projects:co-mentors)=

## Assigning a co-mentor
