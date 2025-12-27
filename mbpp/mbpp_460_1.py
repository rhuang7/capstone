def check(candidate):
    assert candidate([[1, 2], [3, 4, 5], [6, 7, 8, 9]]) == [1, 3, 6]
    assert candidate([[1,2,3],[4, 5]]) == [1,4]
    assert candidate([[9,8,1],[1,2]]) == [9,1]


def get_first_elements(list_of_lists):
    return [sublist[0] for sublist in list_of_lists if sublist]

check(get_first_elements)