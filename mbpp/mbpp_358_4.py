def check(candidate):
    assert candidate([4,5,6],[1, 2, 3])==[0, 1, 0]
    assert candidate([3,2],[1,4])==[0, 2]
    assert candidate([90,120],[50,70])==[40, 50]


def modulo_division(list1, list2):
    return list(map(lambda a, b: a % b, list1, list2))

check(modulo_division)