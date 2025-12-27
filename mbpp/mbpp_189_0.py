def check(candidate):
    assert candidate([1,2,3,-1,5],5) == 4
    assert candidate([0,-1,-2,1,5,8],6) == 2
    assert candidate([0,1,2,5,-8],5) == 3


def first_missing_positive(nums):
    n = len(nums)
    for i in range(n):
        while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
            nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
    for i in range(n):
        if nums[i] != i + 1:
            return i + 1
    return n + 1

check(first_missing_positive)