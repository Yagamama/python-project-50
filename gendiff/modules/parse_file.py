import json


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


def stylish_string(data, result='{\n', spaces="  "):
    for item in data:
        key = item.get('name')
        edit = edit_value(item["value"], sp=spaces)
        edit2 = edit_value(item.get('value2'), sp=spaces)
        match item['action']:
            case '=':
                result += f'{spaces}  {key}: {edit}\n'
            case '+':
                result += f'{spaces}+ {key}: {edit}\n'
            case '-':
                result += f'{spaces}- {key}: {edit}\n'
            case '>':
                result += f'{spaces}- {key}: {edit}\n'
                result += f'{spaces}+ {key}: {edit2}\n'
            case 'inner':
                result += f'{spaces}  {key}: ' + '{\n'
                result = stylish_string(item['value'], result, spaces + "    ")
                result += spaces + "  }\n"
        # print(result)
    return result


def plain_string(data, param=''):
    result = ''
    for item in data:
        key = item['name']
        if param:
            key = param + '.' + key
        match item['action']:
            case '+':
                result += f"Property '{key}' was added with "
                result += f"value: {edit_value(item['value'], 'plain')}\n"
            case '-':
                result += f"Property '{key}' was removed\n"
            case '>':
                result += f"Property '{key}' was updated. From "
                result += f"{edit_value(item['value'], 'plain')} "
                result += f"to {edit_value(item['value2'], 'plain')}\n"
            case 'inner':
                result += plain_string(item['value'], key)
    return result


def edit_value(string, format='stylish', sp=''):
    if isinstance(string, bool):
        return str(string).lower()
    elif isinstance(string, str) and format == 'plain':
        return f"'{string}'"
    elif string is None:
        return 'null'
    elif isinstance(string, list):
        edit_value(string[0], format, sp)
    elif isinstance(string, dict):
        if format == 'plain':
            return '[complex value]'
        else:
            r = ''
            for key, value in string.items():
                val = edit_value(value, sp=sp + "    ")
                r += f'    {sp}  {key}: {val}\n'
            return '{' + f'\n{r}{sp}' + '  }'
    else:
        return string


def parse_json(data):
    return json.dumps(data[0], sort_keys=True, indent=4)
