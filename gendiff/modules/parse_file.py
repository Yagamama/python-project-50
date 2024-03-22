import json
from .stylish import stylish_string
from .plain import plain_string


def compare_data(f1, f2):
    keys_list = f1.keys() | f2.keys()
    added = f2.keys() - f1.keys()
    deleted = f1.keys() - f2.keys()
    result = []

    for key in keys_list:
        if key in added:
            result.append({'name': key,
                           'action': '+',
                           'value': f2.get(key)})
        elif key in deleted:
            result.append({'name': key,
                           'action': '-',
                           'value': f1.get(key)})
        elif isinstance(f1.get(key), dict) and isinstance(f2.get(key), dict):
            result.append({'name': key,
                           'action': 'inner',
                           'value': compare_data(f1.get(key), f2.get(key))})
        elif f1.get(key) == f2.get(key):
            result.append({'name': key,
                           'action': '=',
                           'value': f1.get(key)})
        else:
            result.append({'name': key,
                           'action': '>',
                           'value': f1.get(key),
                           'value2': f2.get(key)})

        result = sorted(result, key=lambda x: x['name'])
    return result


def generate_big_string(data, format):
    if format == 'stylish':
        return stylish_string(data) + '}'
    elif format == 'json':
        return parse_json(data)
    else:
        return plain_string(data)


def parse_json(data):
    return json.dumps(data[0], sort_keys=True, indent=4)
