def check(candidate):
    assert candidate(10)==20
    assert candidate(40)==80
    assert candidate(15)==30


def diameter(radius):
    return 2 * radius

check(diameter)