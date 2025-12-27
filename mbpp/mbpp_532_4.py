def check(candidate):
    assert candidate("abc", "cba") == True
    assert candidate("test", "ttew") == False
    assert candidate("xxyz", "yxzx") == True


def are_permutations(s1, s2):
    return sorted(s1) == sorted(s2)

check(are_permutations)