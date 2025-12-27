def check(candidate):
    assert candidate(6,9,4)==30
    assert candidate(10,20,30)==450
    assert candidate(15,25,35)==700


def trapezium_area(base1, base2, height):
    return (base1 + base2) * height / 2

check(trapezium_area)