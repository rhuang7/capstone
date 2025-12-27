def check(candidate):
    assert candidate("011001",6) == 3
    assert candidate("11011",5) == 4
    assert candidate("1010",4) == 2


def count_odd_rotations(s):
    if len(s) == 0:
        return 0
    count = 0
    for i in range(len(s)):
        rotated = s[i:] + s[:i]
        if int(rotated, 2) % 2 == 1:
            count += 1
    return count

check(count_odd_rotations)