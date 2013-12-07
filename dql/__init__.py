"""
Simple SQL-like query language for dynamo

"""
import argparse
import boto.dynamodb2

from .cli import DQLREPL
from .engine import Engine


def main():
    """ Start the DQL client """
    parse = argparse.ArgumentParser(description=main.__doc__)
    parse.add_argument('-c', '--command', help="Run this command and exit")
    regions = [region.name for region in boto.dynamodb2.regions()]
    regions.append('local')
    parse.add_argument('-r', '--region', choices=regions, default='us-west-1',
                       help="AWS region to connect to (default %(default)s")
    parse.add_argument('-H', '--host', default='localhost',
                       help="Host to connect to if region is 'local' "
                       "(default %(default)s")
    parse.add_argument('-p', '--port', default=8000,
                       help="Port to connect to if region is 'local' "
                       "(default %(default)s)")
    parse.add_argument('-a', '--access-key', help="Your AWS access key id")
    parse.add_argument('-s', '--secret-key', help="Your AWS secret access key")

    args = parse.parse_args()

    cli = DQLREPL()
    cli.initialize(region=args.region, host=args.host, port=args.port,
                   access_key=args.access_key, secret_key=args.secret_key)

    if args.command:
        cli.onecmd(args.command)
    else:
        cli.start()
