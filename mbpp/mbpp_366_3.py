def check(candidate):
    assert candidate([1,2,3,4,5,6]) == 30
    assert candidate([1,2,3,4,5]) == 20
    assert candidate([2,3]) == 6


def largest_adjacent_product(nums):
    if len(nums) < 2:
        return None  # Not enough elements for a pair
    max_product = nums[0] * nums[1]
    for i in range(1, len(nums) - 1):
        product = nums[i] * nums[i + 1]
        if product > max_product:
            max_product = product
    return max_product

check(largest_adjacent_product)