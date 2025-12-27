def check(candidate):
    assert candidate([5, 6, 7], (9, 10)) == [5, 6, 7, 9, 10]
    assert candidate([6, 7, 8], (10, 11)) == [6, 7, 8, 10, 11]
    assert candidate([7, 8, 9], (11, 12)) == [7, 8, 9, 11, 12]


def add_tuple_to_list(lst, tup):
    lst.append(tup)

check(add_tuple_to_list)