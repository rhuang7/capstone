def check(candidate):
    assert candidate([1,2,3],3) == True
    assert candidate([1,2,1,4],4) == True
    assert candidate([1,1],2) == False


def is_product_even(numbers):
    return any(num % 2 == 0 for num in numbers)

check(is_product_even)