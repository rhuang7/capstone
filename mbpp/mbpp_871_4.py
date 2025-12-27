def check(candidate):
    assert candidate("abc","cba") == False
    assert candidate("abcd","cdba") == False
    assert candidate("abacd","cdaba") == True


def are_rotations(s1, s2):
    if len(s1) != len(s2):
        return False
    return s2 in s1 + s1

check(are_rotations)