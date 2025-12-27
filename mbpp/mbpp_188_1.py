def check(candidate):
    assert candidate(25) == False
    assert candidate(30) == False
    assert candidate(16) == True


def is_product_of_two_squares(n):
    if n < 0:
        return False
    for i in range(1, int(n**0.5) + 1):
        if n % (i*i) == 0:
            return True
    return False

check(is_product_of_two_squares)