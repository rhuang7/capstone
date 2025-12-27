def check(candidate):
    assert candidate([1, 2, 3, 5, 7, 8, 10])==4
    assert candidate([10,15,14,13,-18,12,-20])==2
    assert candidate([1, 2, 4, 8, 9])==2


def count_odd_elements(lst):
    return len(list(filter(lambda x: x % 2 != 0, lst)))

check(count_odd_elements)