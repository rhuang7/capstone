def check(candidate):
    assert candidate([220, 330, 500],200)==True
    assert candidate([12, 17, 21],20)==False
    assert candidate([1,2,3,4],10)==False


def find_values_greater_than(lst, num):
    return [value for value in lst if value > num]

check(find_values_greater_than)