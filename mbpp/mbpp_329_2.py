def check(candidate):
    assert candidate([-1,-2,3,-4,-5]) == 4
    assert candidate([1,2,3]) == 0
    assert candidate([1,2,-3,-10,20]) == 2


def count_negative_numbers(lst):
    return sum(1 for num in lst if num < 0)

check(count_negative_numbers)