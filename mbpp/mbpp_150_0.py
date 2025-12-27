def check(candidate):
    assert candidate(1,7,3) == True
    assert candidate(1,-3,5) == False
    assert candidate(3,2,5) == False


def is_number_in_infinite_sequence(n):
    # The infinite sequence is 1, 2, 3, 4, 5, ...
    # Any positive integer n will be present in this sequence
    if n > 0:
        return True
    else:
        return False

check(is_number_in_infinite_sequence)