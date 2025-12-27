def check(candidate):
    assert candidate([19, 65, 57, 39, 152, 639, 121, 44, 90, 190],2,4)==[ 152,44]
    assert candidate([1, 2, 3, 5, 7, 8, 10],2,5)==[10]
    assert candidate([10,15,14,13,18,12,20],10,5)==[10,20]


def find_divisible_numbers(numbers, m, n):
    return list(filter(lambda x: x % m == 0 and x % n == 0, numbers))

check(find_divisible_numbers)