import time
import socket


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

def generateTraefikToml():
    pass # Not implemented
