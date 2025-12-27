def check(candidate):
    assert candidate([1,2,3]) == 4
    assert candidate([-1,2,3,4]) == 3
    assert candidate([2,3,6]) == 8


def sum_of_largest_and_smallest(arr):
    if not arr:
        return 0  # Return 0 for empty array as per typical edge case handling
    return max(arr) + min(arr)

check(sum_of_largest_and_smallest)