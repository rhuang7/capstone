def check(candidate):
    assert candidate((7, 8, 9, 1, 10, 7)) == 42
    assert candidate((1, 2, 3, 4, 5, 6)) == 21
    assert candidate((11, 12 ,13 ,45, 14)) == 95


def sum_tuple_elements(tuple_list):
    return sum(element for element in tuple_list if isinstance(element, tuple))

check(sum_tuple_elements)