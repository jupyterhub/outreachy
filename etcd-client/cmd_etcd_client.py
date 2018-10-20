import argparse
from async_etcd_client import AsyncEtcdClient


def main():
    parser = argparse.ArgumentParser(description="Description of your program")
    subparsers = parser.add_subparsers(help="commands", dest="command")
    subparsers.required = True

    # Get command
    get_parser = subparsers.add_parser(
        "get", help="Get the value associated with a key"
    )
    get_parser.add_argument(
        "--prefix",
        default=False,
        action="store_true",
        help="Get all the KV pairs starting with a prefix",
    )
    get_parser.add_argument("key", action="store", help="Key to search for")

    # Set command
    set_parser = subparsers.add_parser("set", help="Set the value of a key")
    set_parser.add_argument("key", action="store", help="Key to add")
    set_parser.add_argument("value", action="store", help="Value of the key")
    set_parser.add_argument(
        "--swap",
        default=False,
        action="store_true",
        help="Change the value of an existing key.",
    )
    set_parser.add_argument(
        "--old_value",
        default=False,
        action="store",
        help="The previous value of the key",
    )

    # Mkdir command
    mkdir_parser = subparsers.add_parser(
        "mkdir", help="Create a new directory"
    )
    mkdir_parser.add_argument(
        "key", action="store", help="The directory you want to add"
    )

    # Ls command
    ls_parser = subparsers.add_parser("ls", help="List a directory")
    ls_parser.add_argument(
        "key", action="store", help="The directory you want to list"
    )

    # Rm command
    rm_parser = subparsers.add_parser("rm", help="Remove a key or a directory")
    rm_parser.add_argument(
        "key", action="store", help="The key or directory you want to remove"
    )

    args = parser.parse_args()

    command = args.command
    params = [args.key]

    if command == "set":
        params.append(args.value)
        if args.swap:
            params.extend([args.swap, args.old_value])
    elif command == "get" and args.prefix:
        params.append(args.prefix)

    client = AsyncEtcdClient("127.0.0.1", 2379)
    print(client.command_selector(command, params))


if __name__ == "__main__":
    main()
