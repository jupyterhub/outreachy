import pytest
import sys
from os.path import abspath, dirname, join
from subprocess import Popen
from subprocess import check_output
from subprocess import CalledProcessError

cmd_client_path = abspath(join(dirname(__file__), "cmd_etcd_client.py"))


def cleanup(key):
    Popen(["etcdctl", "rm", key], stdout=None, stderr=None)


def cleanup_dir(dirname):
    Popen(["etcdctl", "rmdir", dirname], stdout=None, stderr=None)


def test_no_args():
    try:
        output = (
            check_output([sys.executable, cmd_client_path])
            .decode(sys.stdout.encoding)
            .strip()
            != 0
        )
    except CalledProcessError as err:
        rc = err.returncode
    assert rc != 0


def test_invalid_command():
    command = "invalid"
    try:
        output = (
            check_output([sys.executable, cmd_client_path, command])
            .decode(sys.stdout.encoding)
            .strip()
            != 0
        )
    except CalledProcessError as err:
        rc = err.returncode
    assert rc != 0


def test_no_args_for_get():
    command = "get"
    try:
        output = (
            check_output([sys.executable, cmd_client_path, command])
            .decode(sys.stdout.encoding)
            .strip()
            != 0
        )
    except CalledProcessError as err:
        rc = err.returncode
    assert rc != 0


def test_no_args_for_set():
    command = "set"
    try:
        output = (
            check_output([sys.executable, cmd_client_path, command])
            .decode(sys.stdout.encoding)
            .strip()
            != 0
        )
    except CalledProcessError as err:
        rc = err.returncode
    assert rc != 0


def test_no_args_for_mkdir():
    command = "mkdir"
    try:
        output = (
            check_output([sys.executable, cmd_client_path, command])
            .decode(sys.stdout.encoding)
            .strip()
            != 0
        )
    except CalledProcessError as err:
        rc = err.returncode
    assert rc != 0


def test_no_args_for_ls():
    command = "ls"
    try:
        output = (
            check_output([sys.executable, cmd_client_path, command])
            .decode(sys.stdout.encoding)
            .strip()
            != 0
        )
    except CalledProcessError as err:
        rc = err.returncode
    assert rc != 0


def test_no_args_for_rm():
    command = "rm"
    try:
        output = (
            check_output([sys.executable, cmd_client_path, command])
            .decode(sys.stdout.encoding)
            .strip()
            != 0
        )
    except CalledProcessError as err:
        rc = err.returncode
    assert rc != 0


def test_get_key_not_found():
    command = "get"
    key = "/test_key_not_found"
    expected_output = "Key not found : %s\nNone" % key

    assert (
        check_output([sys.executable, cmd_client_path, command, key])
        .decode(sys.stdout.encoding)
        .strip()
        == expected_output
    )


def test_get_existing_key():
    command = "get"
    key = "/test/get"
    value = "get"

    # First introduce the KV pair using etcdctl
    assert (
        check_output(["etcdctl", "set", key, value])
        .decode(sys.stdout.encoding)
        .strip()
        == value
    )
    assert (
        check_output([sys.executable, cmd_client_path, command, key])
        .decode(sys.stdout.encoding)
        .strip()
        == value
    )

    cleanup(key)


def test_get_prefix():
    command = "get"
    prefix = "/testprefix"
    keys = ["/testprefix/t1", "/testprefix/t2", "/testprefix/t3"]
    values = ["t1", "t2", "t3"]
    expected_output = [
        str(keys[i] + ": " + values[i]) for i in range(len(keys))
    ]

    # First introduce the KV pair using etcdctl
    assert (
        check_output(["etcdctl", "set", keys[0], values[0]])
        .decode(sys.stdout.encoding)
        .strip()
        == values[0]
    )
    assert (
        check_output(["etcdctl", "set", keys[1], values[1]])
        .decode(sys.stdout.encoding)
        .strip()
        == values[1]
    )
    assert (
        check_output(["etcdctl", "set", keys[2], values[2]])
        .decode(sys.stdout.encoding)
        .strip()
        == values[2]
    )

    out = (
        check_output(
            [sys.executable, cmd_client_path, command, "--prefix", prefix]
        )
        .decode(sys.stdout.encoding)
        .strip()
    )
    assert out == str(expected_output)

    cleanup(keys[0])
    cleanup(keys[1])
    cleanup(keys[2])


def test_set_existing_key():
    command = "set"
    key = "/set_existing"
    value = "exists"
    expected_output = "Key already exists : %s\nNone" % key

    assert (
        check_output(["etcdctl", "set", key, value])
        .decode(sys.stdout.encoding)
        .strip()
        == value
    )
    assert (
        check_output([sys.executable, cmd_client_path, command, key, value])
        .decode(sys.stdout.encoding)
        .strip()
        == expected_output
    )

    cleanup(key)


def test_set_new_key():
    command = "set"
    key = "/set_new"
    value = "new"

    assert (
        check_output([sys.executable, cmd_client_path, command, key, value])
        .decode(sys.stdout.encoding)
        .strip()
        == value
    )

    cleanup(key)


def test_set_swap_values():
    command = "set"
    key = "/swap_value"
    new_value = "new_value"
    prev_value = "prev_value"

    assert (
        check_output(["etcdctl", "set", key, prev_value])
        .decode(sys.stdout.encoding)
        .strip()
        == prev_value
    )
    assert (
        check_output(
            [
                sys.executable,
                cmd_client_path,
                command,
                key,
                new_value,
                "--swap",
                "--old_value",
                prev_value,
            ]
        )
        .decode(sys.stdout.encoding)
        .strip()
        == new_value
    )

    cleanup(key)


def test_set_swap_wrong_prev():
    command = "set"
    key = "/swap_value"
    new_value = "new_value"
    prev_value = "prev_value"
    wrong_prev_value = "wrong_value"
    expected_output = "Compare failed : [%s != %s]\nNone" % (
        wrong_prev_value,
        prev_value,
    )

    assert (
        check_output(["etcdctl", "set", key, prev_value])
        .decode(sys.stdout.encoding)
        .strip()
        == prev_value
    )
    assert (
        check_output(
            [
                sys.executable,
                cmd_client_path,
                command,
                key,
                new_value,
                "--swap",
                "--old_value",
                wrong_prev_value,
            ]
        )
        .decode(sys.stdout.encoding)
        .strip()
        == expected_output
    )

    cleanup(key)


def test_mkdir_new():
    command = "mkdir"
    dirname = "/test_new_dir"
    expected_output = "None"

    assert (
        check_output([sys.executable, cmd_client_path, command, dirname])
        .decode(sys.stdout.encoding)
        .strip()
        == expected_output
    )

    cleanup_dir(dirname)


def test_mkdir_existing():
    command = "mkdir"
    dirname = "/test_existing_dir"
    expected_output = "Not a file : %s\nNone" % dirname

    assert (
        check_output(["etcdctl", "mkdir", dirname])
        .decode(sys.stdout.encoding)
        .strip()
        == ""
    )

    assert (
        check_output([sys.executable, cmd_client_path, command, dirname])
        .decode(sys.stdout.encoding)
        .strip()
        == expected_output
    )

    cleanup_dir(dirname)


def test_ls_existing_dir():
    command = "ls"
    dirname = "/dir"
    keys = ["/dir/t1", "/dir/t2", "/dir/t3"]
    values = ["t1", "t2", "t3"]
    expected_output = [
        str(keys[i] + ": " + values[i]) for i in range(len(keys))
    ]

    assert (
        check_output(["etcdctl", "mkdir", dirname])
        .decode(sys.stdout.encoding)
        .strip()
        == ""
    )

    # First introduce the KV pair using etcdctl
    assert (
        check_output(["etcdctl", "set", keys[0], values[0]])
        .decode(sys.stdout.encoding)
        .strip()
        == values[0]
    )
    assert (
        check_output(["etcdctl", "set", keys[1], values[1]])
        .decode(sys.stdout.encoding)
        .strip()
        == values[1]
    )
    assert (
        check_output(["etcdctl", "set", keys[2], values[2]])
        .decode(sys.stdout.encoding)
        .strip()
        == values[2]
    )

    assert check_output(
        [sys.executable, cmd_client_path, command, dirname]
    ).decode(sys.stdout.encoding).strip() == str(expected_output)

    cleanup(keys[0])
    cleanup(keys[1])
    cleanup(keys[2])
    cleanup_dir(dirname)


def test_ls_non_existing_dir():
    command = "ls"
    dirname = "/nothing"
    expected_output = "Key not found : %s\nNone" % dirname

    assert check_output(
        [sys.executable, cmd_client_path, command, dirname]
    ).decode(sys.stdout.encoding).strip() == str(expected_output)


def test_rm_non_existing_key():
    command = "rm"
    key = "/nothing"
    expected_output = "Key not found : %s\nNone" % key

    assert check_output(
        [sys.executable, cmd_client_path, command, key]
    ).decode(sys.stdout.encoding).strip() == str(expected_output)


def test_rm_existing_key():
    command = "rm"
    key = "/some_key"
    value = "value"

    # First introduce the KV pair using etcdctl
    assert (
        check_output(["etcdctl", "set", key, value])
        .decode(sys.stdout.encoding)
        .strip()
        == value
    )
    assert (
        check_output([sys.executable, cmd_client_path, command, key])
        .decode(sys.stdout.encoding)
        .strip()
        == "None"
    )
