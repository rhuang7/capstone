def check(candidate):
    assert candidate(4)==3
    assert candidate(3)==2
    assert candidate(5)==5


def count_ways(n):
    # Base cases
    if n == 0:
        return 1
    if n == 1:
        return 1
    
    # Recursive case: either place a vertical tile or two horizontal tiles
    return count_ways(n - 1) + count_ways(n - 2)

check(count_ways)