def check(candidate):
    assert candidate([1,2,3,4,7,0,8,4]) == (7,8)
    assert candidate([0,-1,-2,-4,5,0,-6]) == (-4,-6)
    assert candidate([1,2,3]) == (2,3)


def find_highest_product_pair(arr):
    if len(arr) < 2:
        return None  # Not enough elements to form a pair
    
    # Initialize variables to track the highest product and its indices
    max_product = float('-inf')
    max_indices = (0, 1)
    
    # Iterate through all possible pairs
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            product = arr[i] * arr[j]
            if product > max_product:
                max_product = product
                max_indices = (i, j)
    
    return max_indices

check(find_highest_product_pair)