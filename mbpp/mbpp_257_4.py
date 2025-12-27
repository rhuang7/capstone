def check(candidate):
    assert candidate(10,20)==(20,10)
    assert candidate(15,17)==(17,15)
    assert candidate(100,200)==(200,100)


def swap_numbers(a, b):
    return b, a

check(swap_numbers)