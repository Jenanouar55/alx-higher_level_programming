#!/usr/bin/python3
def uppercase(input_str):
    for ch in input_str:
        if 97 <= ord(ch) <= 122:
            ch = chr(ord(ch) - 32)
            print("{:s}".format(ch), end='')
            print()
