def check(candidate):
    assert candidate([1,3,5,7,4,1,6,8])==4
    assert candidate([1,2,3,4,5,6,7,8,9,10])==2
    assert candidate([1,5,7,9,10])==10


def find_division_of_even_and_odd(numbers):
    even = None
    odd = None
    for num in numbers:
        if num % 2 == 0:
            even = num
        else:
            odd = num
        if even is not None and odd is not None:
            break
    if even is None or odd is None:
        return None
    return even / odd

check(find_division_of_even_and_odd)