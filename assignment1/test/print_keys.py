#!/usr/bin/python -tt

import sys

def main():
  if len(sys.argv) != 2:
    print 'usage: ./print_keys.py filename'
    sys.exit(1)

  dict = {}
  dict = open(sys.argv[2], 'rU')
  for key in dict.keys():
    print key

if __name__ == '__main__':
  main()