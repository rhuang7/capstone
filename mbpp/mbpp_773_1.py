def check(candidate):
    assert candidate('python programming, python language','python')==('python', 0, 6)
    assert candidate('python programming,programming language','programming')==('programming', 7, 18)
    assert candidate('python programming,programming language','language')==('language', 31, 39)


def find_substrings(text, substrings):
    results = {}
    for sub in substrings:
        start_positions = []
        start = 0
        while True:
            start = text.find(sub, start)
            if start == -1:
                break
            start_positions.append(start)
            start += 1  # Move past the current match to find overlapping matches
        results[sub] = start_positions
    return results

check(find_substrings)