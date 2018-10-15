"""
Test
"""
import traefik_utils
import pytest


def wait_procs(default_backend, first_backend, second_backend, traefik):
    default_backend.wait()
    first_backend.wait()
    second_backend.wait()
    traefik.wait()


def kill_procs(default_backend, first_backend, second_backend, traefik):
    default_backend.kill()
    first_backend.kill()
    second_backend.kill()
    traefik.kill()


def test_toml_routing():
    traefik = traefik_utils.launch_traefik_with_toml()
    default_backend, first_backend, second_backend = (
        traefik_utils.launch_backends()
    )
    try:
        traefik_utils.check_traefik_up()
        traefik_utils.check_backends_up()
        traefik_utils.check_routing()
    finally:
        kill_procs(default_backend, first_backend, second_backend, traefik)
        wait_procs(default_backend, first_backend, second_backend, traefik)


def test_etcd_routing():
    traefik_utils.create_etcd_config()
    traefik = traefik_utils.launch_traefik_with_etcd()
    default_backend, first_backend, second_backend = (
        traefik_utils.launch_backends()
    )
    try:
        traefik_utils.check_traefik_up()
        traefik_utils.check_backends_up()
        traefik_utils.check_traefik_etcd_conf_ready()
        traefik_utils.check_routing()
    finally:
        kill_procs(default_backend, first_backend, second_backend, traefik)
        wait_procs(default_backend, first_backend, second_backend, traefik)
