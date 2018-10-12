"""
Test
"""
import traefikUtils

import pytest
from os.path import abspath, dirname, join
from subprocess import Popen, PIPE

def test_routing():
    traefikPort     = traefikUtils.getPort("traefik")
    configFilePath  = abspath(join(dirname(__file__), 'traefik.toml'))
    traefik         = Popen(["traefik", "-c", configFilePath],
                            stdout=PIPE)
    defaultBackend, firstBackend, secondBackend = traefikUtils.launchBackends()

    try:
        """
            Before sending HTTP requests to traefik (and to the backends)
            we need to make sure the services are up and ready
        """
        assert traefikUtils.checkHostUp("localhost", traefikPort) == True
        traefikUtils.checkBackendsReady()
        traefikUtils.checkRouting()

    finally:
        defaultBackend.kill()
        firstBackend.kill()
        secondBackend.kill()
        traefik.kill()

        defaultBackend.wait()
        firstBackend.wait()
        secondBackend.wait()
        traefik.wait()

def test_etcd_routing():
    traefikPort = traefikUtils.getPort("traefik")
    traefik        = Popen(["traefik", "--etcd", "--etcd.useapiv3=true"], stdout=None)

    defaultBackend, firstBackend, secondBackend = traefikUtils.launchBackends()

    try:
        """
            Before sending HTTP requests to traefik (and to the backends)
            we need to make sure the services are up and ready
        """
        assert traefikUtils.checkHostUp("localhost", traefikPort) == True
        traefikUtils.checkBackendsReady()
        traefikUtils.checkTraefikReady()
        traefikUtils.checkRouting()
    finally:
        defaultBackend.kill()
        firstBackend.kill()
        secondBackend.kill()
        traefik.kill()

        defaultBackend.wait()
        firstBackend.wait()
        secondBackend.wait()
        traefik.wait()
