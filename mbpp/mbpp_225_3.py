def check(candidate):
    assert candidate([1,2,3,4,5],0,4) == 1
    assert candidate([4,6,8],0,2) == 4
    assert candidate([2,3,5,7,9],0,4) == 2


def find_min_in_rotated_sorted_array(nums):
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid
    return nums[left]

check(find_min_in_rotated_sorted_array)