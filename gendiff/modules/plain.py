def plain_string(data, param=''):
    result = ''
    for item in data:
        key = item['name']
        if param:
            key = param + '.' + key
        match item['action']:
            case '+':
                result += f"Property '{key}' was added with "
                result += f"value: {edit_plain_value(item['value'])}\n"
            case '-':
                result += f"Property '{key}' was removed\n"
            case '>':
                result += f"Property '{key}' was updated. From "
                result += f"{edit_plain_value(item['value'])} "
                result += f"to {edit_plain_value(item['value2'])}\n"
            case 'inner':
                result += plain_string(item['value'], key)
    return result


def edit_plain_value(string, sp=''):
    if isinstance(string, bool):
        return str(string).lower()
    elif isinstance(string, str):
        return f"'{string}'"
    elif string is None:
        return 'null'
    elif isinstance(string, list):
        return edit_plain_value(string[0], sp)
    elif isinstance(string, dict):
        return '[complex value]'
    else:
        return string
