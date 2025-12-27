def check(candidate):
    assert candidate(4)==2
    assert candidate(16)==4
    assert candidate(400)==20


def square_root_of_perfect_number(n):
    if n < 1:
        return None
    sqrt_n = int(n ** 0.5)
    if sqrt_n * sqrt_n == n:
        return sqrt_n
    else:
        return None

check(square_root_of_perfect_number)