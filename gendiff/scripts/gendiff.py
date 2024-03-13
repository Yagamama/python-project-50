#!/usr/bin/env python3


import argparse
from gendiff import generate_diff
from pathlib import Path


def main():
    args = arguments()
    p = Path(__file__)
    cur_dir = p.absolute().parent.parent
    print(generate_diff(cur_dir / args.first_file,
                        cur_dir / args.second_file, args.format))
    return


def arguments():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-V', '--version', action='version',
                        help='output the version number', version='0.2.0')
    parser.add_argument('-f', '--format', help='set format of output',
                        default='stylish')
    return parser.parse_args()


if __name__ == '__main__':
    main()
