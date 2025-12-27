def check(candidate):
    assert candidate(10,20,30)==30
    assert candidate(55,47,39)==55
    assert candidate(10,49,30)==49


def max_of_three(a, b, c):
    return max(a, b, c)

check(max_of_three)