def check(candidate):
    assert candidate((4, 5, 7, 9, 3),  [6, 7, 10, 11]) == True
    assert candidate((1, 2, 3, 4),  [4, 6, 7, 8, 9]) == True
    assert candidate((3, 2, 1, 4, 5),  [9, 8, 7, 6]) == False


def contains_element(lst):
    return any(element in lst for element in lst)

check(contains_element)