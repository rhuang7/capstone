def check(candidate):
    assert candidate([10,20,30],[15,25,35])==[25,45,65]
    assert candidate([1,2,3],[5,6,7])==[6,8,10]
    assert candidate([15,20,30],[15,45,75])==[30,65,105]


def sum_lists(list1, list2):
    return [x + y for x, y in zip(list1, list2)]

check(sum_lists)