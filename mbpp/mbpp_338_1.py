def check(candidate):
    assert candidate('aba') == 4
    assert candidate('abcab') == 7
    assert candidate('abc') == 3


def count_same_first_last_substrings(s):
    count = 0
    n = len(s)
    for i in range(n):
        for j in range(i, n):
            if s[i] == s[j]:
                count += 1
    return count

check(count_same_first_last_substrings)