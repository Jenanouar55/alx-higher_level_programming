def uppercase(input_str):
    modified_str = ""
    for ch in input_str:
        if 97 <= ord(ch) <= 122:
            ch = chr(ord(ch) - 32)
            modified_str += ch
            return modified_str
