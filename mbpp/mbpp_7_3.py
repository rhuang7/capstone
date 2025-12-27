def check(candidate):
    assert candidate('Please move back to stream') == ['Please', 'move', 'back', 'stream']
    assert candidate('Jing Eco and Tech') == ['Jing', 'Tech']
    assert candidate('Jhingai wulu road Zone 3') == ['Jhingai', 'wulu', 'road', 'Zone']


import re

def find_long_words(text):
    return re.findall(r'\b\w{4,}\b', text)

check(find_long_words)