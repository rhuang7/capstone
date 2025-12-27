def check(candidate):
    assert candidate([['x', 'y'], ['a', 'b'], ['m', 'n']]) == [['x', 'a', 'm'], ['y', 'b', 'n']]
    assert candidate([[1, 2], [3, 4], [5, 6], [7, 8]]) == [[1, 3, 5, 7], [2, 4, 6, 8]]
    assert candidate([['x', 'y','z' ], ['a', 'b','c'], ['m', 'n','o']]) == [['x', 'a', 'm'], ['y', 'b', 'n'],['z', 'c','o']]


def merge_edges(list_of_lists):
    if not list_of_lists:
        return []
    result = []
    for lst in list_of_lists:
        if len(lst) < 1:
            continue
        merged = [lst[0]] + [lst[-1]]
        result.append(merged)
    return result

check(merge_edges)