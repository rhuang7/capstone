def check(candidate):
    assert candidate('android_tv') == 'AndroidTv'
    assert candidate('google_pixel') == 'GooglePixel'
    assert candidate('apple_watch') == 'AppleWatch'


import re

def snake_to_camel(s):
    return re.sub(r'_([a-z])', lambda m: m.group(1).upper(), s)

check(snake_to_camel)