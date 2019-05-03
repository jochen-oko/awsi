import unittest
import json

from awsi.aws import Aws


class Ec2Stub():
    def __init__(self):
        pass

    def describe_instances(self):
        with open('instances.json') as json_file:
            return json.load(json_file)


class LogStub():
    def __init__(self):
        pass

    def describe_log_groups(self):
        with open('loggroups.json') as json_file:
            return json.load(json_file)


class TestParser(unittest.TestCase):
    def test_log_group_parsing(self):
        """
        Test that it can parse the aws result for log groups
        """
        aws = Aws(Ec2Stub(), LogStub())
        log_groups = aws.get_list_of_log_groups()
        self.assertEqual(log_groups, {'/aws/lambda/autoscaling-monitor - retention: 2 days, created: 22.07.18 22:56:53': '/aws/lambda/autoscaling-monitor',
                                      '/aws/lambda/kafka-check - retention: ? days, created: 06.04.18 19:04:25': '/aws/lambda/kafka-check'})

    def test_instance_parsing(self):
        """
        Test that it can parse the aws result for instances
        """
        aws = Aws(Ec2Stub(), LogStub())
        instances = aws.get_list_of_instances()
        self.assertEqual(instances, {'products-01-develop - i-1234567abcde12345 (m5.large), running, start: 2019-14-22T12:50:05.000Z': 'i-1234567abcde12345'})


if __name__ == '__main__':
    unittest.main()