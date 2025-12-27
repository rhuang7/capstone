def check(candidate):
    assert candidate([1,2,3,4,5]) == True
    assert candidate([1,2,3,5,6]) == False
    assert candidate([1,2,1]) == False


def has_consecutive_numbers(lst):
    if not lst:
        return False
    for i in range(1, len(lst)):
        if lst[i] - lst[i-1] != 1:
            return False
    return True

check(has_consecutive_numbers)