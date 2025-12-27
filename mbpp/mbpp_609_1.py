def check(candidate):
    assert candidate(10,20,30) == 15
    assert candidate(1,2,1) == 0
    assert candidate(11,10,9) == 9


def find_min_periodic_function(f, period):
    import math

    def periodic(x):
        return f(x % period)

    # Find the minimum value of the periodic function over a period
    # We'll sample the function at many points within one period
    # to approximate the minimum value
    min_val = float('inf')
    num_samples = 100000
    for x in range(1, num_samples + 1):
        val = periodic(x / num_samples)
        if val < min_val:
            min_val = val
    return min_val

check(find_min_periodic_function)