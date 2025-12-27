def check(candidate):
    assert candidate([1, 2, 3, 5, 7, 8, 9, 10],[1, 2, 4, 8, 9])==[1, 2, 8, 9]
    assert candidate([1, 2, 3, 5, 7, 8, 9, 10],[3,5,7,9])==[3,5,7,9]
    assert candidate([1, 2, 3, 5, 7, 8, 9, 10],[10,20,30,40])==[10]


def find_intersection(arr1, arr2):
    return list(set(arr1) & set(arr2))

check(find_intersection)