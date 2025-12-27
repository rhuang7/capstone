def check(candidate):
    assert candidate("192.168.0.1") == 'Valid IP address'
    assert candidate("110.234.52.124") == 'Valid IP address'
    assert candidate("366.1.2.2") == 'Invalid IP address'


import re

def is_valid_ip(ip):
    pattern = r'^(\d{1,3}\.){3}\d{1,3}$'
    return re.match(pattern, ip) is not None

check(is_valid_ip)