import argparse
from .aws import *
from .ssh import *
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('command', choices=['start', 'stop', 'describe', 'bind'])
    parser.add_argument('alias')
    args = parser.parse_args()
    if args.command == 'start':
        print(start_instance(args.alias))
    elif args.command == 'stop':
        print(stop_instance(args.alias))
    elif args.command == 'describe':
        print(describe_instance(args.alias))
    elif args.command == 'bind':
        print(bind_instance(args.alias))