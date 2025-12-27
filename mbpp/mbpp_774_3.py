def check(candidate):
    assert candidate("ankitrai326@gmail.com") == 'Valid Email'
    assert candidate("my.ownsite@ourearth.org") == 'Valid Email'
    assert candidate("ankitaoie326.com") == 'Invalid Email'


import re

def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email) is not None

check(is_valid_email)