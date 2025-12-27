def check(candidate):
    assert candidate([1,3,5,7,4,1,6,8])==4
    assert candidate([1,2,3,4,5,6,7,8,9,10])==2
    assert candidate([1,5,7,9,10])==10


def product_of_even_odd(numbers):
    even = None
    odd = None
    for num in numbers:
        if num % 2 == 0:
            even = num
        else:
            odd = num
    if even is None or odd is None:
        return None  # Not enough even or odd numbers
    return even * odd

check(product_of_even_odd)