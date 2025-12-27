def check(candidate):
    assert candidate([11, 33, 50])==113350
    assert candidate([-1,2,3,4,5,6])==-123456
    assert candidate([10,15,20,25])==10152025


def list_to_integer(int_list):
    return int(''.join(map(str, int_list)))

check(list_to_integer)