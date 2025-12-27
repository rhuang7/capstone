def check(candidate):
    assert candidate(2,5,2) == "2 solutions"
    assert candidate(1,1,1) == "No solutions"
    assert candidate(1,2,1) == "1 solution"


def find_quadratic_solutions(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0:
        return 0
    elif discriminant == 0:
        return 1
    else:
        return 2

check(find_quadratic_solutions)