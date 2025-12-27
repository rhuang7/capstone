def check(candidate):
    assert candidate([1,3,5]) == 1
    assert candidate([2,4,1,3]) == 1
    assert candidate ([8,9,1]) == 9


def find_first_odd(numbers):
    for num in numbers:
        if num % 2 != 0:
            return num
    return None

check(find_first_odd)