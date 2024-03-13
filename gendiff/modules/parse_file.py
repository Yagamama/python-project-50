def generate_big_string(f1, f2, format):
    keys_list = sorted(list((f1 | f2).keys()))
    result = '{\n'
    for key in keys_list:
        if key in f1 and key in f2:
            if f1[key] == f2[key]:
                result += stylish_or_plain(key, f1[key], format, param='=')
            else:
                result += stylish_or_plain(key, [f1[key], f2[key]], format, param='>')
        elif key not in f2:
            result += stylish_or_plain(key, f1[key], format, param='-')
        else:
            result += stylish_or_plain(key, f2[key], format, param='+')
    result += '}'
    # print(result)
    return result


def is_bool(string):
    if string is True:
        return 'true'
    elif string is False:
        return 'false'
    elif isinstance(string, str):
        return f"'{string}'"
    else:
        return string


def stylish_or_plain(key, value, format, param):
    if format == 'plain':
        match param:
            case '=':
                return ''
            case '+':
                return f"Property '{key}' was added with value: {is_bool(value)}\n"
            case '-':
                return f"Property '{key}' was removed\n"
            case '>':
                return f"Property '{key}' was updated. From {is_bool(value[0])} to {is_bool(value[1])}\n"
    elif format == 'stylish':
        match param:
            case '=':
                return f'    {key}: {is_bool(value)}\n'
            case '+':
                return f'  + {key}: {is_bool(value)}\n'
            case '-':
                return f'  - {key}: {is_bool(value)}\n'
            case '>':
                return f'  - {key}: {is_bool(value[0])}\n  + {key}: {is_bool(value[1])}\n'
    