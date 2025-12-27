def check(candidate):
    assert candidate([2, 1, 5, 6, 8, 3, 4, 9, 10, 11, 8, 12],8,10) == 29
    assert candidate([1,2,3,4,5],1,2) == 5
    assert candidate([1,0,1,2,5,6],4,5) == 11


def sum_in_range(numbers, start, end):
    return sum(numbers[start:end])

check(sum_in_range)