def check(candidate):
    assert candidate([1,2,3]) == 123
    assert candidate([4,5,6]) == 456
    assert candidate([7,8,9]) == 789


def list_to_integer(int_list):
    return int(''.join(map(str, int_list)))

check(list_to_integer)