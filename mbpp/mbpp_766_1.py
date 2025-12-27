def check(candidate):
    assert candidate([1,1,2,3,3,4,4,5])==[(1, 1), (1, 2), (2, 3), (3, 3), (3, 4), (4, 4), (4, 5)]
    assert candidate([1,5,7,9,10])==[(1, 5), (5, 7), (7, 9), (9, 10)]
    assert candidate([1,2,3,4,5,6,7,8,9,10])==[(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9), (9, 10)]


def consecutive_pairs(lst):
    return [(lst[i], lst[i+1]) for i in range(len(lst)-1)]

check(consecutive_pairs)