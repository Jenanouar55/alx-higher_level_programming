#!/usr/bin/python3
def to_upper(str):
    new_str = ""
    for c in str:
        if 97 <= ord(c) <= 122:
            new_str += chr(ord(c) - 32)
        else:
            new_str += c
            return new_str
        
        def uppercase(str):
            print("{}".format(to_upper(str)))
