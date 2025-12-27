def check(candidate):
    assert candidate([-1, 2, -3, 4, 5, 6, -7, 8, 9], 9) == [-1, -3, -7, 4, 5, 6, 2, 8, 9]
    assert candidate([12, -14, -26, 13, 15], 5) == [-14, -26, 12, 13, 15]
    assert candidate([10, 24, 36, -42, -39, -78, 85], 7) == [-42, -39, -78, 10, 24, 36, 85]


def rearrange_negatives_first(arr):
    negatives = [num for num in arr if num < 0]
    positives = [num for num in arr if num >= 0]
    return negatives + positives

check(rearrange_negatives_first)