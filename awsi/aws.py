import datetime

from .util import *
from .config import Config


class Instance:
    config = Config()

    def __init__(self, instance_json):
        self.instance_id = extract_element(instance_json, "InstanceId", "?")
        self.instance_type = extract_element(instance_json, "InstanceType", "?")
        self.launch_time = extract_element(instance_json, "LaunchTime", "?")
        self.state = extract_element(instance_json, "State", {"Name": "?"})["Name"]
        self.complete = instance_json
        self.service_name = first_non_null_tag_of(instance_json, self.config.get_service_naming_tags())

    def short_launch_time(self, launch_time):
        # aws format: 2019-04-15 09:00:38+00:00
        if self.launch_time == "?":
            return "?"
        try:
            return datetime.datetime.strptime(str(launch_time), '%Y-%m-%d %H:%M:%S%z')\
                .strftime(self.config.get_launch_date_format())
        except ValueError:
            return str(launch_time)

    def to_string(self):
        return "{} - {} ({}), {}, start: {}" \
            .format(self.service_name,
                    self.instance_id,
                    self.instance_type,
                    self.state,
                    self.short_launch_time(self.launch_time))

    def __repr__(self):
        return self.to_string()


class LogGroup:
    config = Config()
    def __init__(self, log_json):
        self.log_group_name = extract_element(log_json, "logGroupName", "?")
        self.retention_time = extract_element(log_json, "retentionInDays", "?")
        self.creation_time = extract_element(log_json, "creationTime", "?")

    def to_string(self):
        return "{} - retention: {} days, created: {}" \
            .format(self.log_group_name,
                    self.retention_time,
                    self.short_creation_time())

    def short_creation_time(self):
        # aws format: 1520594744504
        if self.creation_time == "?":
            return "?"
        return datetime.datetime.fromtimestamp(self.creation_time / 1000.0).strftime(self.config.get_launch_date_format())

    def __repr__(self):
        return self.to_string()


class Aws:

    def __init__(self, ec2_client, logs_client):
        self.ec2 = ec2_client
        self.logs = logs_client


    def get_list_of_log_groups(self):
        data = (self.logs.describe_log_groups())["logGroups"]

        log_group_desc_to_name = {} # description -> name

        groups = [LogGroup(x) for x in data]

        for g in sorted(groups, key=lambda group: group.log_group_name):
            log_group_desc_to_name[str(g)] = g.log_group_name

        return log_group_desc_to_name

    def get_list_of_instances(self):

        data = (self.ec2.describe_instances())["Reservations"]

        instances_with_repr = {} # sring (instance representation) -> instance_id
        services = {}  # servicename -> service
        all_instances = []

        for instance in data:
            _instances = [Instance(x) for x in instance['Instances']]

            first_instance = _instances[0]
            if len(_instances) == 0:
                break
            service_name = first_instance.service_name

            stored = services.get(service_name)
            all_instances.extend(_instances)

            if stored is not None:
                stored.extend(_instances)
            else:
                services[service_name] = _instances

        for i in sorted(all_instances, key=lambda instance: instance.service_name):
            instances_with_repr[str(i)] = i.instance_id

        return instances_with_repr
