def check(candidate):
    assert candidate((4, 3, 2, 2, -1, 18)) == -864
    assert candidate((1,2,3)) == 6
    assert candidate((-2,-4,-6)) == -48


def product_of_tuple(numbers):
    product = 1
    for num in numbers:
        product *= num
    return product

check(product_of_tuple)