def check(candidate):
    assert candidate(10) == False
    assert candidate(36) == True
    assert candidate(14) == False


def is_perfect_square(n):
    if n < 0:
        return False
    root = int(n ** 0.5)
    return root * root == n

check(is_perfect_square)