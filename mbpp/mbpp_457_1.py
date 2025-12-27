def check(candidate):
    assert candidate([[1],[1,2],[1,2,3]]) == [1]
    assert candidate([[1,1],[1,1,1],[1,2,7,8]]) == [1,1]
    assert candidate([['x'],['x','y'],['x','y','z']]) == ['x']


def find_min_length_sublist(lst):
    if not lst:
        return None
    min_len = float('inf')
    min_sublist = []
    for sublist in lst:
        if len(sublist) < min_len:
            min_len = len(sublist)
            min_sublist = sublist
    return min_sublist

check(find_min_length_sublist)