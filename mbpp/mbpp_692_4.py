def check(candidate):
    assert candidate(7) == 40
    assert candidate(5) == 20
    assert candidate(2) == 2


def last_two_digits_of_factorial(n):
    if n < 0:
        return "Negative numbers do not have factorials."
    if n < 2:
        return n
    result = 1
    for i in range(2, n + 1):
        result = (result * i) % 100
    return result

check(last_two_digits_of_factorial)