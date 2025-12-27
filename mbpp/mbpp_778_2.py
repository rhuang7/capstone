def check(candidate):
    assert candidate([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4])==[[0, 0], [1], [2], [3], [4, 4], [5], [6, 6, 6], [7], [8], [9], [4, 4]]
    assert candidate([10, 10, 15, 19, 18, 18, 17, 26, 26, 17, 18, 10])==[[10, 10], [15], [19], [18, 18], [17], [26, 26], [17], [18], [10]]
    assert candidate(['a', 'a', 'b', 'c', 'd', 'd'])==[['a', 'a'], ['b'], ['c'], ['d', 'd']]


def pack_consecutive_duplicates(lst):
    if not lst:
        return []
    
    result = []
    current = [lst[0]]
    
    for item in lst[1:]:
        if item == current[-1]:
            current.append(item)
        else:
            result.append(current)
            current = [item]
    
    result.append(current)
    return result

check(pack_consecutive_duplicates)