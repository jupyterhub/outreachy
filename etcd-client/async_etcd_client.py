import aio_etcd as etcd
import asyncio
import sys

class AsyncEtcdClient:
    def __init__(self, host, port):
        self.host = host
        self.port =port

    async def get(self, key, prefix=False):
        client = etcd.Client(self.host, self.port)
        try:
            if prefix:
                resp = await client.read(key, recursive=True)
                for child in resp.children:
                    print("%s: %s" % (child.key, child.value))
                return
            resp = await client.read(key)
            print("%s: %s" % (key, resp.value))
        except etcd.EtcdKeyNotFound:
            print("Key \"%s\" not found" % key)


    async def set(self, key, value, swap=False, oldvalue=""):
        client = etcd.Client(self.host, self.port)
        try:
            if swap:
                print("Swapping {} with {}".format(oldvalue, value))
                await client.write(key, value, prevValue=oldvalue)
                return
            await client.write(key, value, prevExist=False)
        except etcd.EtcdKeyNotFound:
            print("Key \"%s\" not found" % key)
        except etcd.EtcdAlreadyExist:
            print("Key \"%s\" already exists. Use --swap to change its value" % key)

    async def mkdir(self, directory):
        client = etcd.Client(self.host, self.port)
        try:
            await client.write(directory, None, dir=True)
        except etcd.EtcdNotFile:
            print("Directory \"%s\" already exists" % directory)


    async def ls(self, directory):
        client = etcd.Client(self.host, self.port)
        try:
            r = await client.read(directory, recursive=True, sorted=True)
            for child in r.children:
                print("%s: %s" % (child.key,child.value))
        except etcd.EtcdKeyNotFound:
            print("Dir \"%s\" not found" % directory)
        except etcd.EtcdNotDir:
            print("\"%s\" is not a directory" % directory)


    async def rm(self, key):
        client = etcd.Client(self.host, self.port)
        try:
            await client.delete(key, recursive=True)
        except etcd.EtcdKeyNotFound:
            print("Key \"%s\" not found" % key)


    def action_switcher(self, action, params):
        method = getattr(self, action, lambda: "Invalid month")
        loop = asyncio.get_event_loop()
        if len(params) == 1:
            param = params[0]
            return loop.run_until_complete(method(param))

        return loop.run_until_complete(method(*params))

