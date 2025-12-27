def check(candidate):
    assert candidate(' Google    Flutter ') == 'GoogleFlutter'
    assert candidate(' Google    Dart ') == 'GoogleDart'
    assert candidate(' iOS    Swift ') == 'iOSSwift'


import re

def remove_whitespaces(s):
    return re.sub(r'\s+', '', s)

check(remove_whitespaces)