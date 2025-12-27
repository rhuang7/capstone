def check(candidate):
    assert candidate([1,2,3],3) == 20
    assert candidate([1,2],2) == 5
    assert candidate([1,2,3,4],4) == 84


def sum_of_products_of_subarrays(arr):
    n = len(arr)
    total = 0
    for i in range(n):
        current_product = 1
        for j in range(i, n):
            current_product *= arr[j]
            total += current_product
    return total

check(sum_of_products_of_subarrays)