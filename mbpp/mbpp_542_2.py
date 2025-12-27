def check(candidate):
    assert candidate('Boult Curve Wireless Neckband') == 'Boult:Curve:Wireless:Neckband'
    assert candidate('Stereo Sound Sweatproof') == 'Stereo:Sound:Sweatproof'
    assert candidate('Probass Curve Audio') == 'Probass:Curve:Audio'


import re

def replace_punctuation_with_colon(s):
    return re.sub(r'[ ,.]', ':', s)

check(replace_punctuation_with_colon)