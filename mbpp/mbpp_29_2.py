def check(candidate):
    assert candidate([1,2,3,1,2,3,1],7) == 1
    assert candidate([1,2,3,2,3,1,3],7) == 3
    assert candidate([2,3,5,4,5,2,4,3,5,2,4,4,2],13) == 5


def find_odd_occurrence_element(nums):
    return next(num for num in nums if nums.count(num) % 2 != 0)

check(find_odd_occurrence_element)