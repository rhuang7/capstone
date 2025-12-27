def check(candidate):
    assert candidate([1,1,2,3],4) == 6
    assert candidate([1,2,3,1,1],5) == 6
    assert candidate([1,1,4,5,6],5) == 120


def product_of_non_repeated_elements(arr):
    from collections import Counter
    count = Counter(arr)
    product = 1
    for num in count:
        if count[num] == 1:
            product *= num
    return product

check(product_of_non_repeated_elements)