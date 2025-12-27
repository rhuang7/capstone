def check(candidate):
    assert candidate([1,1,1,1],4) == 6
    assert candidate([1,5,1],3) == 1
    assert candidate([3,2,1,7,8,9],6) == 0


def count_equal_pairs(arr):
    from collections import Counter
    counts = Counter(arr)
    return sum(count * (count - 1) // 2 for count in counts.values())

check(count_equal_pairs)