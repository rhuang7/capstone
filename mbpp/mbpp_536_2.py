def check(candidate):
    assert candidate([1, 2, 3, 4, 5, 6, 7, 8, 9],2)==[1, 3, 5, 7, 9] 
    assert candidate([10,15,19,17,16,18],3)==[10,17] 
    assert candidate([14,16,19,15,17],4)==[14,17]


def select_nth_item(lst, n):
    if n < 0 or n >= len(lst):
        return None
    return lst[n]

check(select_nth_item)