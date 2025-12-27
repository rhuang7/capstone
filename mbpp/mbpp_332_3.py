def check(candidate):
    assert candidate('python')=={'p': 1, 'y': 1, 't': 1, 'h': 1, 'o': 1, 'n': 1}
    assert candidate('program')=={'p': 1, 'r': 2, 'o': 1, 'g': 1, 'a': 1, 'm': 1}
    assert candidate('language')=={'l': 1, 'a': 2, 'n': 1, 'g': 2, 'u': 1, 'e': 1}


def count_character_frequency(s):
    frequency = {}
    for char in s:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency

check(count_character_frequency)