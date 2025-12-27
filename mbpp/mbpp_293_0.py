def check(candidate):
    assert candidate(7,8)==10.63014581273465
    assert candidate(3,4)==5
    assert candidate(7,15)==16.55294535724685


def find_third_side(a, b):
    return (a ** 2 + b ** 2) ** 0.5

check(find_third_side)