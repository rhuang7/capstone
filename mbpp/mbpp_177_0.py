def check(candidate):
    assert candidate(3,8) == (3,6)
    assert candidate(2,6) == (2,4)
    assert candidate(1,3) == (1,2)


def find_numbers_with_lcm_in_range(lower, upper):
    def lcm(a, b):
        from math import gcd
        return a * b // gcd(a, b)
    
    for i in range(1, upper + 1):
        for j in range(i + 1, upper + 1):
            current_lcm = lcm(i, j)
            if lower <= current_lcm <= upper:
                return (i, j)
    return None

check(find_numbers_with_lcm_in_range)