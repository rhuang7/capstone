def check(candidate):
    assert (candidate([10, 15, 20, 25, 30, 35, 40], [25, 40, 35])) == [10, 20, 30, 15]
    assert (candidate([1,2,3,4,5], [6,7,1])) == [2,3,4,5,6,7]
    assert (candidate([1,2,3], [6,7,1])) == [2,3,6,7]


def list_difference(list1, list2):
    return [item for item in list1 if item not in list2]

check(list_difference)