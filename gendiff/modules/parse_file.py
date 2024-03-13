def generate_big_string(f1, f2, format):
    keys_list = sorted(list((f1 | f2).keys()))
    result = '{\n' if format == 'stylish' else ''
    for key in keys_list:
        if key in f1 and key in f2:
            if f1[key] == f2[key]:
                result += stylish_or_plain(key, f1[key], format, param='=')
            else:
                result += stylish_or_plain(
                    key, [f1[key], f2[key]], format, param='>')
        elif key not in f2:
            result += stylish_or_plain(key, f1[key], format, param='-')
        else:
            result += stylish_or_plain(key, f2[key], format, param='+')
    result += '}' if format == 'stylish' else ''
    return result


def edit_value(string, format='stylish'):
    if string is True:
        return 'true'
    elif string is False:
        return 'false'
    elif isinstance(string, str) and format == 'plain':
        return f"'{string}'"
    else:
        return string


def stylish_or_plain(key, value, format, param):
    if format == 'plain':
        match param:
            case '=':
                return ''
            case '+':
                s = f"Property '{key}' was added with "
                s += f"value: {edit_value(value, format)}\n"
                return s
            case '-':
                return f"Property '{key}' was removed\n"
            case '>':
                s = f"Property '{key}' was updated. From "
                s += f"{edit_value(value[0], format)} "
                s += f"to {edit_value(value[1], format)}\n"
                return s
    elif format == 'stylish':
        match param:
            case '=':
                return f'    {key}: {edit_value(value)}\n'
            case '+':
                return f'  + {key}: {edit_value(value)}\n'
            case '-':
                return f'  - {key}: {edit_value(value)}\n'
            case '>':
                s = f'  - {key}: {edit_value(value[0])}\n'
                s += f'  + {key}: {edit_value(value[1])}\n'
                return s
