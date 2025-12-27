def check(candidate):
    assert candidate([1,2,3,4,5,6]) == [1,3,5]
    assert candidate([10,11,12,13]) == [11,13]
    assert candidate([7,8,9,1]) == [7,9,1]


def find_odd_numbers(mixed_list):
    return [num for num in mixed_list if num % 2 != 0]

check(find_odd_numbers)