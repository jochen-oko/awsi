
import os


class Config:

    SEPARATOR="="
    LAUNCH_DATE_FORMAT_NAME="launch_date_format"
    SERVICE_NAMING_TAGS_NAME="service_naming_tags"

    default_config_file=os.path.expanduser("~/.awsi/default.cfg")
    user_config_file=os.path.expanduser("~/.awsi/user.cfg")
    default_config = {}
    user_config = {}

    def __init__(self):
        self.default_config = self.read_config(self.default_config_file)
        self.user_config = self.read_config(self.user_config_file)

    def get(self, name):
        try:
            set_by_user = self.user_config[name]
            if set_by_user is not None:
                return set_by_user
        except KeyError:
            default_set = self.default_config[name]
            if default_set is not None:
                return default_set

    def get_launch_date_format(self):
        return self.get(self.LAUNCH_DATE_FORMAT_NAME)

    def get_service_naming_tags(self):
        return self.get(self.SERVICE_NAMING_TAGS_NAME).split(",")

    def read_config(self, filename):
        result = {}
        with open(filename) as f:
            for line in f:
                if self.SEPARATOR in line:
                    (key, val) = line.split("=")
                    result[key] = val.rstrip()
        return result


