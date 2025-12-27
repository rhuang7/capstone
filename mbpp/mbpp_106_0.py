def check(candidate):
    assert candidate([5, 6, 7], (9, 10)) == (9, 10, 5, 6, 7)
    assert candidate([6, 7, 8], (10, 11)) == (10, 11, 6, 7, 8)
    assert candidate([7, 8, 9], (11, 12)) == (11, 12, 7, 8, 9)


def add_to_tuples(tuples, list_to_add):
    return [t + (x,) for t in tuples for x in list_to_add]

check(add_to_tuples)