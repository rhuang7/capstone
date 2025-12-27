def check(candidate):
    assert candidate(([1,2,3,4,5]))==False
    assert candidate(([1,2,3,4, 4]))==True
    assert candidate([1,1,2,2,3,3,4,4,5])==True


def contains_duplicate(nums):
    return len(nums) != len(set(nums))

check(contains_duplicate)