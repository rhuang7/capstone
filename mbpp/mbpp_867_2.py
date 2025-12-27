def check(candidate):
    assert candidate([1,2,3,4,5,6,7,8,9],9) == 1
    assert candidate([1,2,3,4,5,6,7,8],8) == 2
    assert candidate([1,2,3],3) == 2


def make_sum_even(arr):
    total = sum(arr)
    if total % 2 == 0:
        return 0
    else:
        return 1

check(make_sum_even)