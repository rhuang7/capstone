def check(candidate):
    assert candidate(13)==360360
    assert candidate(2)==2
    assert candidate(1)==1


def smallest_multiple(n):
    if n == 0:
        return 0
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

check(smallest_multiple)