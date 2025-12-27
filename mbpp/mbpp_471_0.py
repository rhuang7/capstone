def check(candidate):
    assert candidate([ 100, 10, 5, 25, 35, 14 ],6,11) ==9
    assert candidate([1,1,1],3,1) == 0
    assert candidate([1,2,1],3,2) == 0


def array_mod_product(arr, n):
    if n <= 0:
        raise ValueError("n must be positive")
    product = 1
    for num in arr:
        product = (product * (num % n)) % n
    return product

check(array_mod_product)