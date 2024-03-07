#!/usr/bin/env python3


import argparse
from gendiff import generate_diff
from pathlib import Path


def main():
      parser = argparse.ArgumentParser(
            description='Compares two configuration files and shows a difference.')
      parser.add_argument('first_file')
      parser.add_argument('second_file')
      parser.add_argument('-f', '--format', help='set format of output')
      args = parser.parse_args()
      p = Path(__file__)
      cur_dir = p.absolute().parent.parent
      print(generate_diff(cur_dir / args.first_file, cur_dir / args.second_file))


if __name__ == '__main__':
      main()
