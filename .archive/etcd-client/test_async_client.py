import pytest
import aio_etcd as etcd
import asyncio

from unittest import mock
from mock import Mock
from async_etcd_client import AsyncEtcdClient


class MockResp:
    def __init__(self):
        self.children = []

    def set_value(self, value):
        self.value = value

    def set_key(self, key):
        self.key = key


def mock_get(cls, *args, **kwargs):
    ret_val = asyncio.Future()
    ret_val.set_result("testing")
    return ret_val


host = "127.0.0.1"
port = 2379


def test_get():
    with mock.patch("async_etcd_client.etcd.Client") as MockClient:
        resp = MockResp()
        resp.value = "testing"
        resp.key = "/test"

        ret_val = asyncio.Future()
        ret_val.set_result(resp)

        MockClient.return_value.read.return_value = ret_val
        async_client = AsyncEtcdClient(host, port)

        loop = asyncio.get_event_loop()
        assert (
            loop.run_until_complete(async_client.get(resp.key)) == resp.value
        )

        MockClient.assert_called_once_with(host, port)
        MockClient.return_value.read.assert_called_once_with(resp.key)
        MockClient.return_value.close.assert_called_once()


def test_get_exception():
    with mock.patch("async_etcd_client.etcd.Client") as MockClient:
        resp = MockResp()
        resp.key = "/test"
        with pytest.raises(etcd.EtcdKeyNotFound):
            ret_val = asyncio.Future()
            ret_val.set_exception(etcd.EtcdKeyNotFound)

            expected_output = "etcd.EtcdKeyNotFound: None"

            MockClient.return_value.read.return_value = ret_val
            async_client = AsyncEtcdClient(host, port)

            loop = asyncio.get_event_loop()
            loop.run_until_complete(async_client.get(resp.key))

        MockClient.assert_called_once_with(host, port)
        MockClient.return_value.read.assert_called_once_with(resp.key)
        MockClient.return_value.close.assert_called_once()


def test_get_prefix():
    with mock.patch("async_etcd_client.etcd.Client") as MockClient:
        resp = MockResp()
        resp.key = "/test"
        resp.value = "testing"
        prefix_resp = MockResp()
        prefix_resp.children.append(resp)
        expected_output = ["/test: testing"]

        ret_val = asyncio.Future()
        ret_val.set_result(prefix_resp)

        MockClient.return_value.read.return_value = ret_val
        async_client = AsyncEtcdClient(host, port)

        loop = asyncio.get_event_loop()
        assert (
            loop.run_until_complete(async_client.get(resp.key, True))
            == expected_output
        )

        MockClient.assert_called_once_with(host, port)
        MockClient.return_value.read.assert_called_once_with(
            resp.key, recursive=True, sorted=True
        )
        MockClient.return_value.close.assert_called_once()


def test_get_prefix_exception():
    with mock.patch("async_etcd_client.etcd.Client") as MockClient:
        resp = MockResp()
        resp.key = "/test"
        resp.value = "testing"
        with pytest.raises(etcd.EtcdKeyNotFound):
            ret_val = asyncio.Future()
            ret_val.set_exception(etcd.EtcdKeyNotFound)
            expected_output = "etcd.EtcdKeyNotFound: None"

            MockClient.return_value.read.return_value = ret_val
            async_client = AsyncEtcdClient(host, port)

            loop = asyncio.get_event_loop()
            loop.run_until_complete(async_client.get(resp.key, True))

        MockClient.assert_called_once_with(host, port)
        MockClient.return_value.read.assert_called_once_with(
            resp.key, recursive=True, sorted=True
        )
        MockClient.return_value.close.assert_called_once()


def test_set_new_key():
    with mock.patch("async_etcd_client.etcd.Client") as MockClient:
        resp = MockResp()
        resp.key = "/test"
        resp.value = "testing"

        ret_val = asyncio.Future()
        ret_val.set_result(resp)

        MockClient.return_value.write.return_value = ret_val
        async_client = AsyncEtcdClient(host, port)

        loop = asyncio.get_event_loop()
        assert (
            loop.run_until_complete(async_client.set(resp.key, resp.value))
            == resp.value
        )

        MockClient.assert_called_once_with(host, port)
        MockClient.return_value.write.assert_called_once_with(
            resp.key, resp.value, prevExist=False
        )
        MockClient.return_value.close.assert_called_once()


def test_set_existing_key():
    with mock.patch("async_etcd_client.etcd.Client") as MockClient:
        resp = MockResp()
        resp.key = "/test"
        resp.value = "testing"
        with pytest.raises(etcd.EtcdAlreadyExist):
            ret_val = asyncio.Future()
            ret_val.set_exception(etcd.EtcdAlreadyExist)

            MockClient.return_value.write.return_value = ret_val
            async_client = AsyncEtcdClient(host, port)

            loop = asyncio.get_event_loop()
            loop.run_until_complete(async_client.set(resp.key, resp.value))

        MockClient.assert_called_once_with(host, port)
        MockClient.return_value.write.assert_called_once_with(
            resp.key, resp.value, prevExist=False
        )
        MockClient.return_value.close.assert_called_once()


def test_set_swap_values():
    with mock.patch("async_etcd_client.etcd.Client") as MockClient:
        resp = MockResp()
        resp.key = "/test"
        resp.value = "new_value"

        ret_val = asyncio.Future()
        ret_val.set_result(resp)

        MockClient.return_value.write.return_value = ret_val
        async_client = AsyncEtcdClient(host, port)

        loop = asyncio.get_event_loop()
        assert (
            loop.run_until_complete(
                async_client.set(resp.key, resp.value, True, "prev_value")
            )
            == resp.value
        )

        MockClient.assert_called_once_with(host, port)
        MockClient.return_value.write.assert_called_once_with(
            resp.key, resp.value, prevExist=True, prevValue="prev_value"
        )
        MockClient.return_value.close.assert_called_once()


def test_set_swap_wrong_values():
    with mock.patch("async_etcd_client.etcd.Client") as MockClient:
        resp = MockResp()
        resp.key = "/test"
        resp.value = "testing"
        with pytest.raises(etcd.EtcdCompareFailed):
            ret_val = asyncio.Future()
            ret_val.set_exception(etcd.EtcdCompareFailed)

            MockClient.return_value.write.return_value = ret_val
            async_client = AsyncEtcdClient(host, port)

            loop = asyncio.get_event_loop()
            loop.run_until_complete(
                async_client.set(resp.key, resp.value, True, "prev_value")
            )

        MockClient.assert_called_once_with(host, port)
        MockClient.return_value.write.assert_called_once_with(
            resp.key, resp.value, prevExist=True, prevValue="prev_value"
        )
        MockClient.return_value.close.assert_called_once()


def test_mkdir_new():
    with mock.patch("async_etcd_client.etcd.Client") as MockClient:
        resp = MockResp()
        resp.key = "/new_dir"
        resp.value = None

        ret_val = asyncio.Future()
        ret_val.set_result(resp)

        MockClient.return_value.write.return_value = ret_val
        async_client = AsyncEtcdClient(host, port)

        loop = asyncio.get_event_loop()
        assert (
            loop.run_until_complete(async_client.mkdir(resp.key)) == resp.value
        )

        MockClient.assert_called_once_with(host, port)
        MockClient.return_value.write.assert_called_once_with(
            resp.key, resp.value, dir=True
        )
        MockClient.return_value.close.assert_called_once()


def test_mkdir_existing():
    with mock.patch("async_etcd_client.etcd.Client") as MockClient:
        resp = MockResp()
        resp.key = "/dir"
        resp.value = None
        with pytest.raises(etcd.EtcdNotFile):
            ret_val = asyncio.Future()
            ret_val.set_exception(etcd.EtcdNotFile)

            MockClient.return_value.write.return_value = ret_val
            async_client = AsyncEtcdClient(host, port)

            loop = asyncio.get_event_loop()
            loop.run_until_complete(async_client.mkdir(resp.key))

        MockClient.assert_called_once_with(host, port)
        MockClient.return_value.write.assert_called_once_with(
            resp.key, resp.value, dir=True
        )
        MockClient.return_value.close.assert_called_once()


def test_ls_existing():
    with mock.patch("async_etcd_client.etcd.Client") as MockClient:
        resp = MockResp()
        resp.key = "/test"
        resp.value = "testing"
        prefix_resp = MockResp()
        prefix_resp.children.append(resp)
        expected_output = ["/test: testing"]

        ret_val = asyncio.Future()
        ret_val.set_result(prefix_resp)

        MockClient.return_value.read.return_value = ret_val
        async_client = AsyncEtcdClient(host, port)

        loop = asyncio.get_event_loop()
        assert (
            loop.run_until_complete(async_client.ls(resp.key))
            == expected_output
        )

        MockClient.assert_called_once_with(host, port)
        MockClient.return_value.read.assert_called_once_with(
            resp.key, recursive=True, sorted=True
        )
        MockClient.return_value.close.assert_called_once()


def test_ls_non_existing():
    with mock.patch("async_etcd_client.etcd.Client") as MockClient:
        resp = MockResp()
        resp.key = "/test"
        resp.value = "testing"
        with pytest.raises(etcd.EtcdKeyNotFound):
            ret_val = asyncio.Future()
            ret_val.set_exception(etcd.EtcdKeyNotFound)
            expected_output = "etcd.EtcdKeyNotFound: None"

            MockClient.return_value.read.return_value = ret_val
            async_client = AsyncEtcdClient(host, port)

            loop = asyncio.get_event_loop()
            loop.run_until_complete(async_client.ls(resp.key))

        MockClient.assert_called_once_with(host, port)
        MockClient.return_value.read.assert_called_once_with(
            resp.key, recursive=True, sorted=True
        )
        MockClient.return_value.close.assert_called_once()


def test_rm_existing():
    with mock.patch("async_etcd_client.etcd.Client") as MockClient:
        resp = MockResp()
        resp.key = "/test"

        ret_val = asyncio.Future()
        ret_val.set_result(resp)

        MockClient.return_value.delete.return_value = ret_val
        async_client = AsyncEtcdClient(host, port)

        loop = asyncio.get_event_loop()
        loop.run_until_complete(async_client.rm(resp.key))

        MockClient.assert_called_once_with(host, port)
        MockClient.return_value.delete.assert_called_once_with(
            resp.key, recursive=True
        )
        MockClient.return_value.close.assert_called_once()


def test_rm_non_existing():
    with mock.patch("async_etcd_client.etcd.Client") as MockClient:
        resp = MockResp()
        resp.key = "/test"
        with pytest.raises(etcd.EtcdKeyNotFound):
            ret_val = asyncio.Future()
            ret_val.set_exception(etcd.EtcdKeyNotFound)

            MockClient.return_value.delete.return_value = ret_val
            async_client = AsyncEtcdClient(host, port)

            loop = asyncio.get_event_loop()
            loop.run_until_complete(async_client.rm(resp.key))

        MockClient.assert_called_once_with(host, port)
        MockClient.return_value.delete.assert_called_once_with(
            resp.key, recursive=True
        )
        MockClient.return_value.close.assert_called_once()


def test_command_selector_valid_one_param_command():
    with mock.patch.object(AsyncEtcdClient, "get", new=mock_get):
        command = "get"
        key = "/test"
        expected_output = "testing"

        async_client = AsyncEtcdClient(host, port)
        assert async_client.command_selector(command, key) == expected_output


def test_command_selector_valid_multiple_param_command():
    with mock.patch.object(AsyncEtcdClient, "get", new=mock_get):
        command = "get"
        key = "/test"
        expected_output = "testing"
        prefix = True

        async_client = AsyncEtcdClient(host, port)
        assert (
            async_client.command_selector(command, [key, prefix])
            == expected_output
        )


def test_command_selector_valid_command():
    with mock.patch.object(AsyncEtcdClient, "get", new=mock_get):
        with pytest.raises(AttributeError):
            command = "lala"
            key = "/test"
            async_client = AsyncEtcdClient(host, port)
            async_client.command_selector(command, key) == expected_output
