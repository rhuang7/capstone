def check(candidate):
    assert candidate("ABCDEFabcdef123450") == True
    assert candidate("*&%@#!}{") == False
    assert candidate("HELLOhowareyou98765") == True


import re

def is_valid_string(s):
    pattern = r'^[a-z0-9]+$'
    return bool(re.match(pattern, s))

check(is_valid_string)