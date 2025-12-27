def check(candidate):
    assert candidate([1,1,2,3,4,4,5,1],3)==([1, 1, 2], [3, 4, 4, 5, 1])
    assert candidate(['a', 'b', 'c', 'd'],2)==(['a', 'b'], ['c', 'd'])
    assert candidate(['p', 'y', 't', 'h', 'o', 'n'],4)==(['p', 'y', 't', 'h'], ['o', 'n'])


def split_list(lst, length):
    if length < 0:
        return [], lst
    if length > len(lst):
        return lst, []
    return lst[:length], lst[length:]

check(split_list)