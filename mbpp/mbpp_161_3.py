def check(candidate):
    assert candidate([1,2,3,4,5,6,7,8,9,10],[2,4,6,8])==[1, 3, 5, 7, 9, 10]
    assert candidate([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],[1, 3, 5, 7])==[2, 4, 6, 8, 9, 10]
    assert candidate([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],[5,7])==[1, 2, 3, 4, 6, 8, 9, 10]


def remove_elements_from_list(main_list, exclude_list):
    return [item for item in main_list if item not in exclude_list]

check(remove_elements_from_list)