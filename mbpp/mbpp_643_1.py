def check(candidate):
    assert candidate("pythonzabc.")==('Found a match!')
    assert candidate("xyzabc.")==('Found a match!')
    assert candidate("  lang  .")==('Not matched!')


def has_z_in_middle(word):
    if len(word) < 3:
        return False
    return 'z' in word[1:-1]

check(has_z_in_middle)