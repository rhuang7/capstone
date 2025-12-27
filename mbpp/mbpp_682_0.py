def check(candidate):
    assert candidate([1, 2, 3],[4,5,6])==[4,10,18]
    assert candidate([1,2],[3,4])==[3,8]
    assert candidate([90,120],[50,70])==[4500,8400]


def multiply_lists(list1, list2):
    return list(map(lambda a, b: a * b, list1, list2))

check(multiply_lists)