def check(candidate):
    assert candidate('Please move back to strem') == ['strem']
    assert candidate('4K Ultra HD streaming player') == ['Ultra']
    assert candidate('Streaming Media Player') == ['Media']


import re

def find_five_char_words(text):
    return re.findall(r'\b\w{5}\b', text)

check(find_five_char_words)