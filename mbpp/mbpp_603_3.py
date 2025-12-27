def check(candidate):
    assert candidate(10) == [1, 2, 3, 5, 7]
    assert candidate(25) == [1, 2, 3, 5, 7, 11, 13, 17, 23, 25]
    assert candidate(45) == [1, 2, 3, 5, 7, 11, 13, 17, 23, 25, 29, 37, 41, 43]


def lucid_number(n):
    def is_lucid(x):
        s = str(x)
        for i in range(len(s) // 2):
            if s[i] != s[-i-1]:
                return False
        return True

    for i in range(n, -1, -1):
        if is_lucid(i):
            return i
    return 0

check(lucid_number)