def check(candidate):
    assert candidate("123abcjw:, .@! eiw") == '123abcjweiw'
    assert candidate("Hello1234:, ! Howare33u") == 'Hello1234Howare33u'
    assert candidate("Cool543Triks@:, Make@987Trips") == 'Cool543TriksMake987Trips' 


import re

def remove_non_alphanumeric(text):
    return re.sub(r'[^a-zA-Z0-9]', '', text)

check(remove_non_alphanumeric)