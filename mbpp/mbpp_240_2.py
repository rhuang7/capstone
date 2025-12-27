def check(candidate):
    assert candidate([1, 3, 5, 7, 9, 10],[2, 4, 6, 8])==[1, 3, 5, 7, 9, 2, 4, 6, 8]
    assert candidate([1,2,3,4,5],[5,6,7,8])==[1,2,3,4,5,6,7,8]
    assert candidate(["red","blue","green"],["yellow"])==["red","blue","yellow"]


def replace_last_element(lst, new_list):
    if not lst:
        return new_list
    lst[-1] = new_list
    return lst

check(replace_last_element)