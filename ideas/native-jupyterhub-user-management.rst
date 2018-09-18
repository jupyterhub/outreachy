========================================
JupyterHub native user management system
========================================

Long Description
================

JupyterHub **authenticators** determine how users on a particular
installation of JupyterHub can log in. Large installations usually
rely on a third party service (Google, GitHub, LDAP, etc), while smaller
ones maintain Linux user accounts by hand. There is a need for a more
modern system for smaller installations that is easier than maintaining
linux user accounts by hand, but doesn't require too much set up. This
should let users sign up, be approved by an administrator & then login
with a username / password.

A user management system that is native to JupyterHub, implemented
as an authenticator, would solve this need. 

This JupyterHub native user management system should support the following
workflows:

1. Username / Password based sign-up
2. Administrator approval for new users (optional)
3. Password can be reset by user or admin.

It should also implement at least some of the following anti-abuse features:
1. Throttling of login attempts
2. Temporarily / permanently deactivating a user account
3. Password strength meter on signup

Once done, this can be set up as the default authenticator for the JupyterHub
distribution targetted at small scale use cases - `The Littlest JupyterHub
<http://tljh.jupyter.org>`_.

How can applicants make a contribution to the project?
======================================================

The project requires familiarity with asynchronous programming in Python,
using the `Tornado web framework <http://www.tornadoweb.org/en/stable/>`_. 
"`Structure of a Tornado web application <http://www.tornadoweb.org/en/stable/guide/structure.html>`_"
is a good place to start.

We require students finish at least one project-specific microtask before
they apply. https://github.com/jupyterhub/outreachy/labels/project-nativeauth
lists the various microtasks that are specific to this project. You should
complete at least one of them. Comment on the issue, or reach out to us at
https://gitter.im/jupyterhub/jupyterhub for help!

Intern Benefits
===============

You'll learn important web development skillsets through this project:

1. Asynchronous Web Development with Python
2. Understanding how to build secure user authentication systems
3. Common anti-abuse mechanisms for username / password authentication systems
4. The common pitfalls of username / password authentication systems & why/when to avoid them.

You'll also learn to work with a distributed community of people in various
fields from across the world. Your work will be featured prominently on the
`Project Jupyter Blog <https://blog.jupyter.org>`_, and lots of people around
the world will likely use this authenticator in many ways.

Community Benefits
==================

JupyterHub's current authentication mechanisms require you to either:

1. Trust a third party (Google, Auth0, etc) running a proprietary service 
2. Manage user accounts by hand in the ol' school Linux way (not possible in all
   deployments) 
3. Set up & run your own external authentication service

For cases where you have a small number of users & not much technical budget,
none of these options are very good. A JupyterHub-native username/password
based authenticator will fill this gap, and will become the default
Authenticator for `The Littlest JupyterHub <http://tljh.jupyter.org>`_.
This will be much more secure & useful than the current default,
`FirstUseAuthenticator <https://github.com/yuvipanda/jupyterhub-firstuseauthenticator>`_.