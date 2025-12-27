def check(candidate):
    assert candidate('Forces of the \ndarkness*are coming into the play.') == ['Forces of the ', 'darkness', 'are coming into the play.']
    assert candidate('Mi Box runs on the \n Latest android*which has google assistance and chromecast.') == ['Mi Box runs on the ', ' Latest android', 'which has google assistance and chromecast.']
    assert candidate('Certain services\nare subjected to change*over the seperate subscriptions.') == ['Certain services', 'are subjected to change', 'over the seperate subscriptions.']


import re

def split_string_by_multiple_delimiters(s, delimiters):
    # Create a regex pattern that matches any of the delimiters
    pattern = '|'.join(re.escape(d) for d in delimiters)
    # Use re.split to split the string by the pattern
    return re.split(pattern, s)

check(split_string_by_multiple_delimiters)