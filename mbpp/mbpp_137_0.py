def check(candidate):
    assert candidate([0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8])==0.15
    assert candidate([2, 1, 2, -1, -5, 6, 4, -3, -2, 3, 4, 6, 8])==0.00
    assert candidate([2, 4, -6, -9, 11, -12, 14, -5, 17])==0.00


def ratio_of_zeroes(arr):
    total = len(arr)
    zeroes = arr.count(0)
    if total == 0:
        return 0.0
    return zeroes / total

check(ratio_of_zeroes)