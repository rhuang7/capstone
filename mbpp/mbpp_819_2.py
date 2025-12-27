def check(candidate):
    assert candidate([1,2,2,2,4,4,4,5,5,5,5])==([1, 2, 4, 5], [1, 3, 3, 4])
    assert candidate([2,2,3,1,2,6,7,9])==([2, 3, 1, 2, 6, 7, 9], [2, 1, 1, 1, 1, 1, 1])
    assert candidate([2,1,5,6,8,3,4,9,10,11,8,12])==([2, 1, 5, 6, 8, 3, 4, 9, 10, 11, 8, 12], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])


def count_consecutive_duplicates(nums):
    if not nums:
        return []
    
    result = []
    i = 0
    while i < len(nums) - 1:
        if nums[i] == nums[i + 1]:
            result.append(2)
            i += 2
        else:
            result.append(1)
            i += 1
    return result

check(count_consecutive_duplicates)