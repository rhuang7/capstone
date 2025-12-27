def check(candidate):
    assert candidate([1, -2, -3, 0, 7, -8, -2]) == 112
    assert candidate([6, -3, -10, 0, 2]) == 180 
    assert candidate([-2, -40, 0, -2, -3]) == 80


def max_product_subarray(nums):
    if not nums:
        return 0
    
    max_prod = min_prod = result = nums[0]
    
    for num in nums[1:]:
        max_prod, min_prod = max(num, max_prod * num, min_prod * num), min(num, max_prod * num, min_prod * num)
        result = max(result, max_prod)
    
    return result

check(max_product_subarray)