def check(candidate):
    assert candidate('cAstyoUrFavoRitETVshoWs') == 'cstyoravoitshos'
    assert candidate('wAtchTheinTernEtrAdIo') == 'wtchheinerntrdo'
    assert candidate('VoicESeaRchAndreComMendaTionS') == 'oiceachndreomendaion'


import re

def remove_uppercase_substrings(s):
    return re.sub(r'[A-Z]+', '', s)

check(remove_uppercase_substrings)