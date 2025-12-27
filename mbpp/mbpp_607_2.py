def check(candidate):
    assert candidate('The quick brown fox jumps over the lazy dog.', 'fox') == ('fox', 16, 19)
    assert candidate('Its been a very crazy procedure right', 'crazy') == ('crazy', 16, 21)
    assert candidate('Hardest choices required strongest will', 'will') == ('will', 35, 39)


import re

def find_pattern_in_string(text, pattern):
    matches = re.finditer(pattern, text)
    results = []
    for match in matches:
        start = match.start()
        end = match.end()
        results.append((start, end, match.group()))
    return results

check(find_pattern_in_string)