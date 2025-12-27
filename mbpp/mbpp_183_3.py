def check(candidate):
    assert candidate([1, 5, 3, 4, 2], 5, 3) == 2
    assert candidate([8, 12, 16, 4, 0, 20], 6, 4) == 5
    assert candidate([2, 4, 1, 3, 4], 5, 2) == 3


def count_distinct_pairs_with_difference_k(arr, k):
    num_set = set(arr)
    count = 0
    for num in num_set:
        if (num + k) in num_set:
            count += 1
    return count

check(count_distinct_pairs_with_difference_k)