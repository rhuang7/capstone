def check(candidate):
    assert candidate(10, 2) == 90
    assert candidate(10, 3) == 720
    assert candidate(10, 1) == 10


def permutation_coefficient(n, k):
    if k > n:
        return 0
    if k == 0 or k == n:
        return 1
    # Calculate the permutation coefficient using factorial
    # p(n, k) = n! / (n - k)!
    return factorial(n) // factorial(n - k)

def factorial(x):
    if x == 0:
        return 1
    result = 1
    for i in range(1, x + 1):
        result *= i
    return result

check(factorial)