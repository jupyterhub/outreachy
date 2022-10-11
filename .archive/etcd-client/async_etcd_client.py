"""Asynchronous etcd client

This class allows the user to talk asynchronously with etcd and assumes
there is an etcd cluster which can be reached through the host and port
passed to the constructor.
"""

import aio_etcd as etcd
import asyncio
import sys


class AsyncEtcdClient:
    """
    A class used to represent simple async etcd commandline client

    ...

    Attributes
    ----------
    host : str
        the address of etcd
    port : int
        the port of etcd accepting client connections

    Methods
    -------
    get(key, prefix=False)
        Returns the value stored in etcd associated with a key or a
        list of key-value pairs stored in etcd associated with keys
        starting with a given prefix
    set(key, value, swap=False, oldvalue="")
        Sets a new key-value pair in etcd and returns the value or
        replaces a value associated with a key with a new one and
        returns the new value
    mkdir(directory)
        Creates a new directory in etcd
    ls(directory)
        Returns a list containing all the key-value pairs stored inside
        a given directory
    rm(key)
        Removes a key or a directory from etcd
    command_selector(command, params)
        Runs the given command with the given parameters
    """

    def __init__(self, host, port):
        """
        Parameters
        ----------
        host : str
            The address of etcd
        port : int
            The port of etcd accepting client connections
        """
        self.host = host
        self.port = port

    def create_client(self):
        return etcd.Client(self.host, self.port)

    async def get(self, key, prefix=False):
        """Returns the value stored in etcd associated with a key or a
        list of key-value pairs stored in etcd associated with keys
        starting with a given prefix.

        If the argument `prefix` isn't passed in, it won't treat the
        key as a prefix.

        Parameters
        ----------
        key : str
            The key to search for or the prefix if prefix is True
        prefix : bool, optional
            Whether or not treat the given key as prefix and search for
            all the keys starting with that prefix (default is None)

        Raises
        ------
        etcd.EtcdKeyNotFound
            If the key isn't found in etcd
        """
        client = self.create_client()
        try:
            if prefix:
                rv = []
                resp = await client.read(key, recursive=True, sorted=True)
                # print(resp.children)
                for child in resp.children:
                    rv.append("%s: %s" % (child.key, child.value))
                client.close()
                return rv
            resp = await client.read(key)
            client.close()
            return resp.value
        except etcd.EtcdKeyNotFound as e:
            client.close()
            raise e

    async def set(self, key, value, swap=False, oldvalue=""):
        """Sets a new key-value pair in etcd and returns the value or
        replaces a value associated with a key with a new one and
        returns the new value.

        If the argument `swap` isn't passed in, it won't try to replace
        the value of the given key.

        Parameters
        ----------
        key : str
            The key to be added in etcd
        value : str
            The value of the new key
        swap : bool, optional
            Whether or not to swap `value` and `oldvalue` associated
            with the given key (default is None)
        oldvalue : str, optional
            The value associated with the given key meant to be
            replaced (default is "")

        Raises
        ------
        etcd.EtcdAlreadyExist
            If the key already exists in etcd and `swap` is False
        etcd.EtcdCompareFailed
            If `oldvalue` is not the value stored in etcd for the given
            key
        """
        client = self.create_client()
        try:
            if swap:
                resp = await client.write(
                    key, value, prevExist=True, prevValue=oldvalue
                )
                client.close()
                return resp.value
            resp = await client.write(key, value, prevExist=False)
            client.close()
            return resp.value
        except (etcd.EtcdAlreadyExist, etcd.EtcdCompareFailed) as e:
            client.close()
            raise e

    async def mkdir(self, directory):
        """Creates a new directory in etcd.

        Parameters
        ----------
        directory : str
            The name of the directory to be added in etcd

        Raises
        ------
        etcd.EtcdNotFile
            If directory already exists in etcd
        """
        client = self.create_client()
        try:
            await client.write(directory, None, dir=True)
            client.close()
        except etcd.EtcdNotFile as e:
            client.close()
            raise e

    async def ls(self, directory):
        """Returns a list containing all the key-value pairs stored
        inside a given directory.

        Parameters
        ----------
        directory : str
            The directory to retrieve

        Raises
        ------
        etcd.EtcdKeyNotFound
            If directory doesn't exist in etcd
        """
        client = self.create_client()
        try:
            rv = []
            resp = await client.read(directory, recursive=True, sorted=True)
            for child in resp.children:
                rv.append("%s: %s" % (child.key, child.value))
            client.close()
            return rv
        except etcd.EtcdKeyNotFound as e:
            client.close()
            raise e

    async def rm(self, key):
        """Removes a key or a directory from etcd.

        Parameters
        ----------
        key : str
            The key/directory to remove

        Raises
        ------
        etcd.EtcdKeyNotFound
            If key/directory don't exist in etcd
        """
        client = self.create_client()
        try:
            await client.delete(key, recursive=True)
            client.close()
        except etcd.EtcdKeyNotFound as e:
            client.close()
            raise e

    def command_selector(self, command, params):
        """Runs the given command with the given parameters and returns
        its result.

        Parameters
        ----------
        command : str
            The command to be run
        params : list<str>
            The parameters of the given command
        """
        method = getattr(self, command)
        loop = asyncio.get_event_loop()
        if len(params) == 1:
            param = params[0]
            try:
                return loop.run_until_complete(method(param))
            except BaseException as e:
                print(e)
                return
        try:
            return loop.run_until_complete(method(*params))
        except BaseException as e:
            print(e)
            return
