==============================================
Make jupyterhub-cull-idle a standalone package
==============================================

Long Description
================

The JupyterHub REST API includes activity information,
which can be used from outside to do things like shutdown servers
that are idle or have been running for too long.

An `example <https://github.com/jupyterhub/jupyterhub/blob/1.0.0/examples/cull-idle/cull_idle_servers.py>`_
script exists to cull idle servers,
written as a proof-of-concept for the JupyterHub REST API.

This script has become the *de facto* standard for implementing the idle-culling feature,
but since it is only an example script,
it has been copied around to deployments all over the place.

Turning this script into an installable Python package (`jupyterhub-cull-idle`)
will make it easier for more deployments to use idle culling,
and for maintenance to keep up with JupyterHub versions and develop new features.

Additionally, making it a standalone package will facilitate good testing practices,
which have been absent from the culling script in the past.

Goals:

- Make jupyterhub-cull-idle a pip-installable package
- Add automated testing on a CI service such as CircleCI
- Release jupyterhub-cull-idle on PyPI
- Update zero-to-jupyterhub and the-littlest-jupyterhub to use the new package

Stretch goals:

- switch to aiohttp instead of tornado as the client code
- add new features to jupyterhub-cull-idle to address community requests


How can applicants make a contribution to the project?
======================================================

The project requires familiarity with asynchronous programming in Python,
using the `Tornado web framework <http://www.tornadoweb.org/en/stable/>`_.
"`Structure of a Tornado web application <http://www.tornadoweb.org/en/stable/guide/structure.html>`_"
is a good place to start.

We require students finish at least one project-specific microtask before
they apply. https://github.com/jupyterhub/outreachy/labels/project-culler
lists the various microtasks that are specific to this project. You should
complete at least one of them. Comment on the issue, or reach out to us at
https://gitter.im/jupyterhub/jupyterhub for help!

Remember that we do not expect you to already have **all** the skills required
to complete the tasks. Ask and we shall help!


Intern Benefits
===============

You'll learn important skills, such as:

- creating and releasing Python packages
- testing software
- asynchronous programming
- software configuration
- writing clients for REST APIs

Your work will be featured prominently on the
`Project Jupyter Blog <https://blog.jupyter.org>`_,
and lots of people around the world will likely use the results.

Community Benefits
==================

This project will benefit thousands of jupyterhub deployments
by improving the culling features of JupyterHub,
and the maintenance of the culling functionality.
