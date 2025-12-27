def check(candidate):
    assert candidate('For the four consumer complaints contact manager AKR reddy') == ['For', 'the', 'four', 'AKR', 'reddy']
    assert candidate('Certain service are subject to change MSR') == ['are', 'MSR']
    assert candidate('Third party legal desclaimers') == ['Third', 'party', 'legal']


import re

def find_words_by_length(s):
    pattern = r'\b\w{3,5}\b'
    return re.findall(pattern, s)

check(find_words_by_length)