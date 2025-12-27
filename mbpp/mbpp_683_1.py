def check(candidate):
    assert candidate(25) == True
    assert candidate(24) == False
    assert candidate(17) == True


def is_sum_of_two_squares(n):
    for i in range(int(n**0.5) + 1):
        j = n - i*i
        if j < 0:
            break
        root = int(j**0.5)
        if root * root == j:
            return True
    return False

check(is_sum_of_two_squares)