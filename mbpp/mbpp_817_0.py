def check(candidate):
    assert candidate([19, 65, 57, 39, 152, 639, 121, 44, 90, 190],19,13)==[19, 65, 57, 39, 152, 190]
    assert candidate([1, 2, 3, 5, 7, 8, 10],2,5)==[2, 5, 8, 10]
    assert candidate([10,15,14,13,18,12,20],10,5)==[10, 15, 20]


def find_divisible_numbers(numbers, m, n):
    return list(filter(lambda x: x % m == 0 or x % n == 0, numbers))

check(find_divisible_numbers)