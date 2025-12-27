def check(candidate):
    assert candidate([2,4,3,5,7],[3,7])==False
    assert candidate([2,4,3,5,7],[4,3])==True
    assert candidate([2,4,3,5,7],[1,6])==False


def contains_sublist(main_list, sublist):
    for i in range(len(main_list) - len(sublist) + 1):
        if main_list[i:i+len(sublist)] == sublist:
            return True
    return False

check(contains_sublist)