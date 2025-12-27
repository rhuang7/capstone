def check(candidate):
    assert candidate([2, 7, 3, 9, 4]) == 252
    assert candidate([1, 2, 8, 3]) == 24
    assert candidate([3, 8, 4, 10, 5]) == 120


def lcm_of_array(arr):
    from math import gcd
    from functools import reduce

    def lcm(a, b):
        return a * b // gcd(a, b)

    return reduce(lcm, arr)

check(lcm_of_array)