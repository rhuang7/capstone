def check(candidate):
    assert candidate([1, 2, 3, 5, 7, 8, 9, 10])==3
    assert candidate([10,15,14,13,-18,12,-20])==5
    assert candidate([1, 2, 4, 8, 9])==3


def count_even_elements(lst):
    return len(list(filter(lambda x: x % 2 == 0, lst)))

check(count_even_elements)