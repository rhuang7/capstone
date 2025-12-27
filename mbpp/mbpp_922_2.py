def check(candidate):
    assert candidate([1, 2, 3, 4, 7, 0, 8, 4])==(7, 8)
    assert candidate([0, -1, -2, -4, 5, 0, -6])==(-4, -6)
    assert candidate([1, 3, 5, 6, 8, 9])==(8,9)


def find_highest_product_pair(arr):
    if len(arr) < 2:
        return None  # Not enough elements to form a pair
    
    max_product = float('-inf')
    pair = (0, 0)
    
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            product = arr[i] * arr[j]
            if product > max_product:
                max_product = product
                pair = (i, j)
    
    return pair

check(find_highest_product_pair)