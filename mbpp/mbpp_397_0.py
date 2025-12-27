def check(candidate):
    assert candidate(25,55,65)==55.0
    assert candidate(20,10,30)==20.0
    assert candidate(15,45,75)==45.0


def find_median(a, b, c):
    return sorted([a, b, c])[1]

check(find_median)