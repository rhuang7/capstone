def check(candidate):
    assert candidate([1,-2,3]) == -6
    assert candidate([1,2,3,4]) == 24
    assert candidate([3,1,2,3]) == 18


def multiply_list_items(lst):
    if not lst:
        return 1
    result = 1
    for num in lst:
        result *= num
    return result

check(multiply_list_items)