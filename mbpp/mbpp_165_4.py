def check(candidate):
    assert candidate("xbcefg") == 2
    assert candidate("ABcED") == 3
    assert candidate("AbgdeF") == 5


def count_same_position_chars(s):
    count = 0
    for i in range(len(s)):
        if i < len(s) and ord(s[i]) - ord('a') == i:
            count += 1
    return count

check(count_same_position_chars)