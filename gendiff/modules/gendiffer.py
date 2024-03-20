import json
import yaml
from .parse_file import generate_big_string, compare_data


def generate_diff(file1, file2, format):
    if format not in ['stylish', 'plain', 'json']:
        print('Wrong format! Use --help for info.')
        return
    f1 = load_file(file1)
    f2 = load_file(file2)
    data = compare_data(f1, f2)
    return generate_big_string(data, format)


def load_file(filename):
    if str(filename).endswith('.json'):
        return json.load(open(filename))
    elif str(filename).endswith('.yaml') or str(filename).endswith('.yml'):
        with open(filename) as f:
            res = yaml.load(f, Loader=yaml.Loader)
        return res
    else:
        print('Wrong file type! Use .json/.yml/.yaml files!')
        return
