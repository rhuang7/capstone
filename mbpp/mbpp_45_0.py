def check(candidate):
    assert candidate([2, 4, 6, 8, 16]) == 2
    assert candidate([1, 2, 3]) == 1
    assert candidate([2, 4, 6, 8]) == 2 


def gcd_array(arr):
    from math import gcd
    from functools import reduce
    
    def find_gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    
    return reduce(find_gcd, arr)

check(gcd_array)