def check(candidate):
    assert candidate('**//Google Android// - 12. ') == 'GoogleAndroid12'
    assert candidate('****//Google Flutter//*** - 36. ') == 'GoogleFlutter36'
    assert candidate('**//Google Firebase// - 478. ') == 'GoogleFirebase478'


import re

def remove_non_alphanumeric(s):
    return re.sub(r'[^a-zA-Z0-9]', '', s)

check(remove_non_alphanumeric)