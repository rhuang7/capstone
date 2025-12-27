def check(candidate):
    assert candidate([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],3,4)==[8, 9, 10, 1, 2, 3, 4, 5, 6]
    assert candidate([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],2,2)==[9, 10, 1, 2, 3, 4, 5, 6, 7, 8]
    assert candidate([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],5,2)==[6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8]


def rotate_list(lst, n):
    if not lst:
        return lst
    n = n % len(lst)
    return lst[-n:] + lst[:-n]

check(rotate_list)