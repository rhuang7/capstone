def check(candidate):
    assert candidate((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2),4) == 0
    assert candidate((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2),10) == 3
    assert candidate((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2),8) == 4


def count_element_in_tuple(t, element):
    return t.count(element)

check(count_element_in_tuple)