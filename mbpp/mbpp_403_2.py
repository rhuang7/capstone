def check(candidate):
    assert candidate("https://www.google.com") == True
    assert candidate("https:/www.gmail.com") == False
    assert candidate("https:// www.redit.com") == False


import re

def is_valid_url(url):
    # Regular expression pattern for URL validation
    pattern = re.compile(
        r'^(https?://)?'  # http or https
        r'([a-zA-Z0-9-]+\.)+'  # domain name
        r'[a-zA-Z]{2,}'  # top-level domain
        r'(\/[^\s]*)?$'  # optional path
    )
    return bool(pattern.match(url))

check(is_valid_url)