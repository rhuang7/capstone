def check(candidate):
    assert candidate([5, 6, 12, 1, 18, 8],6) == 30
    assert candidate([3, 20, 17, 9, 2, 10, 18, 13, 6, 18],10) == 26
    assert candidate([5, 6, 12, 1],4) == 12


def sum_even_numbers_at_even_positions(numbers):
    return sum(num for i, num in enumerate(numbers) if i % 2 == 0 and num % 2 == 0)

check(sum_even_numbers_at_even_positions)