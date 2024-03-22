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


def edit_value(string, sp=''):
    if isinstance(string, bool):
        return str(string).lower()
    elif string is None:
        return 'null'
    elif isinstance(string, list):
        return edit_value(string[0], sp)
    elif isinstance(string, dict):
        r = ''
        for key, value in string.items():
            val = edit_value(value, sp=sp + "    ")
            r += f'    {sp}  {key}: {val}\n'
        return '{' + f'\n{r}{sp}' + '  }'
    else:
        return string
