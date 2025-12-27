def check(candidate):
    assert candidate('Cortex "A53" Based "multi" tasking "Processor"') == ['A53', 'multi', 'Processor']
    assert candidate('Cast your "favorite" entertainment "apps"') == ['favorite', 'apps']
    assert candidate('Watch content "4k Ultra HD" resolution with "HDR 10" Support') == ['4k Ultra HD', 'HDR 10']


import re

def extract_values_by_quotes(s):
    pattern = r'"([^"]*)"'
    matches = re.findall(pattern, s)
    return matches

check(extract_values_by_quotes)