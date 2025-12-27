def check(candidate):
    assert candidate("abc") == 3
    assert candidate("abcda") == 6
    assert candidate("ab") == 2


def count_substrings_with_same_start_end(s):
    count = 0
    n = len(s)
    for i in range(n):
        for j in range(i, n):
            if s[i] == s[j]:
                count += 1
    return count

check(count_substrings_with_same_start_end)