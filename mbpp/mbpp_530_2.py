def check(candidate):
    assert candidate([0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8])==0.31
    assert candidate([2, 1, 2, -1, -5, 6, 4, -3, -2, 3, 4, 6, 8])==0.31
    assert candidate([2, 4, -6, -9, 11, -12, 14, -5, 17])==0.44


def ratio_of_negatives(arr):
    if not arr:
        return 0.0
    negative_count = sum(1 for num in arr if num < 0)
    return negative_count / len(arr)

check(ratio_of_negatives)