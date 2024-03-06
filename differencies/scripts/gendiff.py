#!/usr/bin/env python3
'''Compares two configuration files and shows a difference.
'''

import argparse


def main():
      parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')
      parser.add_argument('first_file')
      parser.add_argument('second_file')
      args = parser.parse_args()
      #print(args.first_file, args.second_file)
      #print('Compares two configuration files and shows a difference.')


if __name__ == '__main__':
      main()
