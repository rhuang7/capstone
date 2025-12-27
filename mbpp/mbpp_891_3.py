def check(candidate):
    assert candidate(12,1) == False
    assert candidate(2,2) == True
    assert candidate(10,20) == True


def have_same_number_of_digits(a, b):
    return len(str(abs(a))) == len(str(abs(b)))

check(have_same_number_of_digits)