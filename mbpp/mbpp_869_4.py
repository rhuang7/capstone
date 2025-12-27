def check(candidate):
    assert candidate([[2], [0], [1, 2, 3], [0, 1, 2, 3, 6, 7], [9, 11], [13, 14, 15, 17]],13,17)==[[13, 14, 15, 17]]
    assert candidate([[2], [0], [1, 2, 3], [0, 1, 2, 3, 6, 7], [9, 11], [13, 14, 15, 17]],1,3)==[[2], [1, 2, 3]]
    assert candidate([[2], [0], [1, 2, 3], [0, 1, 2, 3, 6, 7], [9, 11], [13, 14, 15, 17]],0,7)==[[2], [0], [1, 2, 3], [0, 1, 2, 3, 6, 7]]


def remove_outside_sublists(lst, min_val, max_val):
    return [sub for sub in lst if min_val <= min(sub) and max_val >= max(sub)]

check(remove_outside_sublists)