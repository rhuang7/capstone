def check(candidate):
    assert candidate("LearnToBuildAnythingWithGoogle") == ['Learn', 'To', 'Build', 'Anything', 'With', 'Google']
    assert candidate("ApmlifyingTheBlack+DeveloperCommunity") == ['Apmlifying', 'The', 'Black+', 'Developer', 'Community']
    assert candidate("UpdateInTheGoEcoSystem") == ['Update', 'In', 'The', 'Go', 'Eco', 'System']


import re

def split_at_uppercase(s):
    return re.split('(?=[A-Z])', s)

check(split_at_uppercase)