def check(candidate):
    assert candidate('KDeoALOklOOHserfLoAJSIskdsf') == 'KDALOOOHLAJSI'
    assert candidate('ProducTnamEstreAmIngMediAplAYer') == 'PTEAIMAAY'
    assert candidate('maNufacTuredbYSheZenTechNolOGIes') == 'NTYSZTNOGI'


import re

def remove_lowercase_substrings(s):
    return re.sub(r'[a-z]', '', s)

check(remove_lowercase_substrings)