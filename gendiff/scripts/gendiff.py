#!/usr/bin/env python3


import argparse
from gendiff import generate_diff
from pathlib import Path


def main():
    args = arguments()
    print(generate_diff(find_file(args.first_file),
                        find_file(args.second_file), args.format))
    return


def arguments():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-V', '--version', action='version',
                        help='output the version number', version='0.2.0')
    parser.add_argument('-f', '--format', 
                        help='set format of output: stylish, plain, json',
                        default='stylish')
    return parser.parse_args()


def find_file(fname):
    p = Path(__file__)
    dir = p.absolute().parent
    paths = ['', dir, dir.parent, dir.parent.parent, 
             dir.parent.joinpath('test_files')]
    for path in paths:
        try:
            open(path.joinpath(fname), 'r')
            return path.joinpath(fname)
        except Exception:
            pass
    print('wrong file path')
    return


if __name__ == '__main__':
    main()
