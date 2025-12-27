def check(candidate):
    assert candidate([10,2,56])==14
    assert candidate([[10,20,4,5,'b',70,'a']])==19
    assert candidate([10,20,-4,5,-70])==19


def sum_of_digits_in_list(numbers):
    total = 0
    for num in numbers:
        if num < 0:
            num = -num
        while num > 0:
            total += num % 10
            num = num // 10
    return total

check(sum_of_digits_in_list)