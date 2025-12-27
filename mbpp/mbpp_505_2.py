def check(candidate):
    assert candidate([6, 0, 8, 2, 3, 0, 4, 0, 1]) == [6, 8, 2, 3, 4, 1, 0, 0, 0]
    assert candidate([4, 0, 2, 7, 0, 9, 0, 12, 0]) == [4, 2, 7, 9, 12, 0, 0, 0, 0]
    assert candidate([3, 11, 0, 74, 14, 0, 1, 0, 2]) == [3, 11, 74, 14, 1, 2, 0, 0, 0]


def move_zeroes(nums):
    left = 0
    for right in range(len(nums)):
        if nums[right] != 0:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
    return nums

check(move_zeroes)