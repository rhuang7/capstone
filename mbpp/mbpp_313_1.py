def check(candidate):
    assert candidate([-1,-2,1,2]) == 1,2
    assert candidate([3,4,-5]) == 3,4
    assert candidate([-2,-3,1]) == 1


def print_positive_numbers(numbers):
    for num in numbers:
        if num > 0:
            print(num)

check(print_positive_numbers)