def check(candidate):
    assert candidate([2,1,4,3,6,7,6,3]) == True
    assert candidate([4,1,2]) == True
    assert candidate([1,2,3]) == False


def all_odd_indices_odd(lst):
    for i in range(1, len(lst), 2):
        if lst[i] % 2 == 0:
            return False
    return True

check(all_odd_indices_odd)