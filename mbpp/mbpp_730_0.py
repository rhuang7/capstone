def check(candidate):
    assert candidate([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4 ])==[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 4]
    assert candidate([10, 10, 15, 19, 18, 18, 17, 26, 26, 17, 18, 10])==[10, 15, 19, 18, 17, 26, 17, 18, 10]
    assert candidate(['a', 'a', 'b', 'c', 'd', 'd'])==['a', 'b', 'c', 'd']


def remove_consecutive_duplicates(lst):
    if not lst:
        return []
    result = [lst[0]]
    for i in range(1, len(lst)):
        if lst[i] != result[-1]:
            result.append(lst[i])
    return result

check(remove_consecutive_duplicates)