def check(candidate):
    assert candidate([1,3,5,7,4,1,6,8])==5
    assert candidate([1,2,3,4,5,6,7,8,9,10])==3
    assert candidate([1,5,7,9,10])==11


def sum_even_odd_numbers(numbers):
    even_sum = 0
    odd_sum = 0
    for num in numbers:
        if num % 2 == 0:
            even_sum += num
        else:
            odd_sum += num
    return even_sum + odd_sum

check(sum_even_odd_numbers)