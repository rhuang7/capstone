def check(candidate):
    assert candidate([1, 2, 3],[4,5,6])==[5, 7, 9]
    assert candidate([1,2],[3,4])==[4,6]
    assert candidate([10,20],[50,70])==[60,90]


def add_lists(list1, list2):
    return list(map(lambda x, y: x + y, list1, list2))

check(add_lists)