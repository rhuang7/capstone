def check(candidate):
    assert candidate([10,20,30,40,50,60,7]) == 37
    assert candidate([1,2,3,4,5]) == 6
    assert candidate([0,1,2,3,4,5]) == 6


def sum_of_three_lowest_positive(numbers):
    positive_numbers = [num for num in numbers if num > 0]
    if len(positive_numbers) < 3:
        return sum(positive_numbers)
    positive_numbers.sort()
    return sum(positive_numbers[:3])

check(sum_of_three_lowest_positive)