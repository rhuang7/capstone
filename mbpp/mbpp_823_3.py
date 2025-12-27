def check(candidate):
    assert candidate("dreams for dreams makes life fun", "makes") == 'string doesnt start with the given substring'
    assert candidate("Hi there how are you Hi alex", "Hi") == 'string starts with the given substring'
    assert candidate("Its been a long day", "been") == 'string doesnt start with the given substring'


import re

def starts_with_substring(text, substring):
    pattern = re.compile(f'^{re.escape(substring)}')
    return bool(pattern.match(text))

check(starts_with_substring)