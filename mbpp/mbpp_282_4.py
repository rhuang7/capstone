def check(candidate):
    assert candidate([1, 2, 3],[4,5,6])==[-3,-3,-3]
    assert candidate([1,2],[3,4])==[-2,-2]
    assert candidate([90,120],[50,70])==[40,50]


def subtract_lists(list1, list2):
    return list(map(lambda a, b: a - b, list1, list2))

check(subtract_lists)