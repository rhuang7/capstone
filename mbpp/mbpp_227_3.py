def check(candidate):
    assert candidate(10,20,0)==0
    assert candidate(19,15,18)==15
    assert candidate(-10,-20,-30)==-30


def find_minimum(a, b, c):
    return min(a, b, c)

check(find_minimum)