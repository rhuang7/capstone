def check(candidate):
    assert candidate(["green", "orange", "black", "white"],'blue')==False
    assert candidate([1,2,3,4],7)==False
    assert candidate(["green", "green", "green", "green"],'green')==True


def all_equal_to_string(lst, target):
    return all(item == target for item in lst)

check(all_equal_to_string)