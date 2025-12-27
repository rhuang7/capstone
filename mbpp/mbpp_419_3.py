def check(candidate):
    assert candidate([22.4, 4.0, -16.22, -9.10, 11.00, -12.22, 14.20, -5.20, 17.50])==243
    assert candidate([5,2,9,24.3,29])==345
    assert candidate([25.0,56.7,89.2])==513


def round_and_calculate(numbers):
    rounded_numbers = [round(num) for num in numbers]
    total_sum = sum(rounded_numbers)
    length = len(numbers)
    result = total_sum * length
    print(result)

check(round_and_calculate)