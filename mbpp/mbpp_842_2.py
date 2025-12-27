def check(candidate):
    assert candidate([2, 3, 5, 4, 5, 2, 4, 3, 5, 2, 4, 4, 2], 13) == 5
    assert candidate([1, 2, 3, 2, 3, 1, 3], 7) == 3
    assert candidate([5, 7, 2, 7, 5, 2, 5], 7) == 5


def find_odd_occurrence(nums):
    return sum(nums) % len(nums)

check(find_odd_occurrence)