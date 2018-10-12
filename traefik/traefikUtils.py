import time
import socket
import sys
import requests
from os.path import abspath, dirname, join
from subprocess import Popen, PIPE

_ports = {
    "traefik":        8000,
    "defaultBackend": 9000,
    "firstBackend":   9090,
    "secondBackend":  9099
}

def getPort(serviceName):
    return _ports[serviceName]

def isOpen(ip, port):
    timeout = 1
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(timeout)
    try:
        s.connect((ip, port))
        s.shutdown(socket.SHUT_RDWR)
        return True
    except:
        return False
    finally:
        s.close()

def checkHostUp(ip, port):
    up    = False
    retry = 20   # iterations
    delay = 0.05 # 50 ms

    for i in range(retry):
        if isOpen(ip, port):
            up = True
            break
        else:
            time.sleep(delay)
    return up

def traefikRoutesToCorrectBackend(path, expectedPort):
    baseUrl = "http://localhost:" + str(getPort("traefik"))
    resp = requests.get(baseUrl + path)
    """
        If we get the expected port, it means traefik
        routed the request to the right backend
    """
    assert int(resp.text) == expectedPort

def checkTraefikReady():
    baseUrl = "http://localhost:" + str(getPort("traefik"))

    timeout = time.time() + 3 # 3 seconds from now
    ready = False
    while ready is False:
        resp = requests.get(baseUrl + "/api/providers/etcdv3")
        ready = resp.status_code == 200
        assert time.time() < timeout

    assert ready == True

def checkBackendsReady():
    defaultBackendPort, firstBackendPort, secondBackendPort = getBackendPorts()
    assert checkHostUp("localhost", defaultBackendPort) == True
    assert checkHostUp("localhost", firstBackendPort)   == True
    assert checkHostUp("localhost", secondBackendPort)  == True

def checkRouting():
    defaultBackendPort, firstBackendPort, secondBackendPort = getBackendPorts()
    traefikRoutesToCorrectBackend("/otherthings", defaultBackendPort)
    traefikRoutesToCorrectBackend("/user/somebody", defaultBackendPort)
    traefikRoutesToCorrectBackend("/user/first", firstBackendPort)
    traefikRoutesToCorrectBackend("/user/second", secondBackendPort)
    traefikRoutesToCorrectBackend("/user/first/otherthings", firstBackendPort)
    traefikRoutesToCorrectBackend("/user/second/otherthings", secondBackendPort)

def launchBackends():
    defaultBackendPort, firstBackendPort, secondBackendPort = getBackendPorts()
    dummyServerPath = abspath(join(dirname(__file__), 'dummyHttpServer.py'))

    defaultBackend = Popen([sys.executable, dummyServerPath, str(defaultBackendPort)],
                            stdout=PIPE)
    firstBackend   = Popen([sys.executable, dummyServerPath, str(firstBackendPort)],
                            stdout=PIPE)
    secondBackend  = Popen([sys.executable, dummyServerPath, str(secondBackendPort)],
                            stdout=PIPE)
    return defaultBackend, firstBackend, secondBackend

def getBackendPorts():
    defaultBackendPort = getPort("defaultBackend")
    firstBackendPort   = getPort("firstBackend")
    secondBackendPort  = getPort("secondBackend")

    return defaultBackendPort, firstBackendPort, secondBackendPort

def generateTraefikToml():
    pass # Not implemented
