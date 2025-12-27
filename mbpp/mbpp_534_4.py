def check(candidate):
    assert candidate('python','python programming language')==(0,6)
    assert candidate('programming','python programming language')==(7,18)
    assert candidate('language','python programming language')==(19,27)


def find_pattern_in_string(text, pattern):
    import re
    matches = re.finditer(pattern, text)
    results = []
    for match in matches:
        start = match.start()
        end = match.end()
        results.append((start, end, text[start:end]))
    return results

check(find_pattern_in_string)