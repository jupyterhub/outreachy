==============================================
Highly-available JupyterHub proxy with Traefik
==============================================

Long Description
================

JupyterHub uses a **proxy** to direct incoming user requests to
notebook servers. A proxy's *routing table* determines which
requests are sent where. For example, if user ``userA``'s notebook
server is available at the address ``10.0.1.2:8000``, the routing
table should contain a mapping ``/user/userA`` -> ``10.0.1.2:8000``.
For each request, the proxy determins the URL, consults this routing
table & directs the request to appropriate address.

As users start / stop their servers, JupyterHub must dynamically
modify the routing table to add / remove routes. Modifying the
routing table should also not cause disruption to requests currently
being processed.

`configurable-http-proxy <https://github.com/jupyterhub/configurable-http-proxy>`_
is currently the most used proxy implementation for JupyterHub. The
routing table is kept in-memory, which means you can only run a
single copy of ``configurable-http-proxy`` at a time. If the proxy
process is disrupted for some reason (the node it is running on goes down,
it uses too much memory, etc), the whole JupyterHub is unavailable.
This is particularly a problem in dynamic large scale systems like
`Zero to JupyterHub on Kubernetes <http://z2jh.jupyter.org>`_, where
nodes dynamically come and go.

In this project, you will implement a `JupyterHub proxy
<https://github.com/jupyterhub/jupyterhub/blob/master/docs/source/reference/proxy.md>`_
that uses `traefik <https://traefik.io/>`_ to do the routing, and `etcd
<https://coreos.com/etcd/>`_ to store the routing table. This allows multiple
copies of the proxy to be running easily, making the proxy highly available.
You will also integrate this proxy implementation into our high-scale
`kubernetes <https://k8s.io>`_ distribution, `Zero to JupyterHub on
Kubernetes <http://z2jh.jupyter.org>`_.

How can applicants make a contribution to the project?
======================================================

We require students finish at least one project-specific microtask before
they apply. https://github.com/jupyterhub/outreachy/labels/project-traefik-proxy
lists the various microtasks that are specific to this project. You should
complete at least one of them. Comment on the issue, or reach out to us at
https://gitter.im/jupyterhub/jupyterhub for help!

Remember that we do not expect you to already have **all** the skills required
to complete the tasks. Ask and we shall help!

Intern Benefits
===============

You'll learn important development skills in this project:

1. Asynchronous programming with Python
2. Modeling & building distributed systems
3. Tradeofss between simplicity, high-availability & latency in distributed systems
4. Direct experience with modern large scale system tools, such as Kubernetes,
   etcd & treafik.

You'll also learn to work with a distributed community of people in various
fields from across the world. Your work will be featured prominently on the
`Project Jupyter Blog <https://blog.jupyter.org>`_, and lots of people around
the world will likely use this proxy in many ways.

Community Benefits
==================

JupyterHub is gaining adoption in large scale deployments that place a lot of
value in highly available systems. The ability to make use of a highly-available
proxy would be a big step in that direction. In the long term, it reduces the total
amount of code the community will have to maintain, and leverage improvements in
the traefik / etcd communities easily. There will also be other performance &
reliability improvements as a side effect of this change.
