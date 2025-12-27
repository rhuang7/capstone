def check(candidate):
    assert candidate('Jumanji The Jungle') == 'Jumanji_The_Jungle'
    assert candidate('The Avengers') == 'The_Avengers'
    assert candidate('Fast and Furious') == 'Fast_and_Furious'


import re

def replace_whitespaces_and_underscores(s):
    # Replace whitespaces with underscores
    s = re.sub(r'\s+', '_', s)
    # Replace underscores with whitespaces
    s = re.sub(r'_+', ' ', s)
    return s

check(replace_whitespaces_and_underscores)