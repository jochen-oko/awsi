# entry point for the CLI, which will be indicated by our setup configuration
# in setup.py in the root directory.

import iterfzf
import argparse
import boto3

from .aws import Aws


def main():

    parser = argparse.ArgumentParser(description='AWS Instant Ids')
    parser.add_argument('-instances', action='store_true', help="Returns a list of instance ids")
    parser.add_argument('-loggroups', action='store_true', help="Returns a list of log groups")

    args = parser.parse_args()

    aws = Aws(boto3.client('ec2'), boto3.client('logs'))

    results = {}

    if args.instances:
        results = aws.get_list_of_instances()
    elif args.loggroups:
        results = aws.get_list_of_log_groups()

    selection = iterfzf.iterfzf(results.keys())

    try:
        instance_id = results[selection]
    except KeyError:
        instance_id = ""

    print (instance_id)


if __name__ == '__main__':
    main()
