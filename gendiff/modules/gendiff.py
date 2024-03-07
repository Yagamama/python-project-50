import json


def generate_diff(file1, file2):
    f1 = json.load(open(file1))
    f2 = json.load(open(file2))
    keys_list = sorted(list((f1 | f2).keys()))
    result = '{\n'
    for key in keys_list:
        if key in f1 and key in f2:
            if f1[key] == f2[key]:
                result += f'    {key}: {is_bool(f1[key])}\n'
            else:
                result += f'  - {key}: {is_bool(f1[key])}\n'
                result += f'  + {key}: {is_bool(f2[key])}\n'
        elif key not in f2:
            result += f'  - {key}: {is_bool(f1[key])}\n'
        else:
            result += f'  + {key}: {is_bool(f2[key])}\n'
    result += '}'
    #print(result)
    return result


def is_bool(string):
    if string == True:
        return 'true'
    elif string == False:
        return 'false'
    else:
        return string
