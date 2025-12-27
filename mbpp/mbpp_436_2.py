def check(candidate):
    assert candidate([-1,4,5,-6]) == -1,-6
    assert candidate([-1,-2,3,4]) == -1,-2
    assert candidate([-7,-6,8,9]) == -7,-6


def print_negative_numbers(numbers):
    for num in numbers:
        if num < 0:
            print(num)

check(print_negative_numbers)