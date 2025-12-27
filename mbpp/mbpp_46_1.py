def check(candidate):
    assert candidate([1,5,7,9]) == True
    assert candidate([2,4,5,5,7,9]) == False
    assert candidate([1,2,3]) == True


def all_numbers_different(numbers):
    return len(set(numbers)) == len(numbers)

check(all_numbers_different)