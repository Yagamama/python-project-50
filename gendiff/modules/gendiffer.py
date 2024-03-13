import json
from .parse_file import generate_big_string


def generate_diff(file1, file2, format):
    f1 = json.load(open(file1))
    f2 = json.load(open(file2))
    return generate_big_string(f1, f2, format)
