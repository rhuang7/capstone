def check(candidate):
    assert candidate([10, 20, 30, 40, 20, 50, 60, 40]) ==  720000000
    assert candidate([1, 2, 3, 1,]) == 6
    assert candidate([7, 8, 9, 0, 1, 1]) == 0


def product_of_unique_numbers(numbers):
    from collections import Counter
    count = Counter(numbers)
    unique_numbers = [num for num, freq in count.items() if freq == 1]
    product = 1
    for num in unique_numbers:
        product *= num
    return product

check(product_of_unique_numbers)