def check(candidate):
    assert candidate([1,2,3,4,5]) == [2,4]
    assert candidate([4,5,6,7,8,0,1]) == [4,6,8,0]
    assert candidate ([8,12,15,19]) == [8,12]


def find_even_numbers(mixed_list):
    return [num for num in mixed_list if num % 2 == 0]

check(find_even_numbers)