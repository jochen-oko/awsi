

def first_non_null_tag_of(d, tag_names):
    for tag_name in tag_names:
        value = __tag_value_of(d, tag_name)
        if value is not None:
            return value
    return "No name found, please check ~/.awsi/default.cfg to define naming tags / fields"


def __tag_value_of(d, tag_name):
    try:
        tags = d['Tags']
        for tag in tags:
            if tag['Key'] == tag_name:
                return tag["Value"]
    except (IndexError, KeyError):
        return None
    return None


def first_non_null_element(d, elements, default=None):
    for e in elements:
        value = extract_element(d, e)
        if value is not None:
            return value
    return default


def extract_element(d, element, default=None):
    try:
        return d[element]
    except (IndexError, KeyError):
        return default
