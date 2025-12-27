def check(candidate):
    assert candidate([1,2,3,4], 10) == 11
    assert candidate([4,8,7,2], 50) == 9
    assert candidate([5,6,7,8], 15) == 4


def count_subsequences_with_product_less_than_k(arr, k):
    from itertools import combinations
    
    n = len(arr)
    count = 0
    
    for i in range(1, n + 1):
        for subset in combinations(arr, i):
            product = 1
            for num in subset:
                product *= num
            if product < k:
                count += 1
                
    return count

check(count_subsequences_with_product_less_than_k)