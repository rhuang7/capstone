def check(candidate):
    assert candidate(15,25,35)==20
    assert candidate(10,20,30)==15
    assert candidate(6,9,4)==7.5


def median_of_trapezium(base1, base2, height):
    return (base1 + base2) / 2 * height

check(median_of_trapezium)