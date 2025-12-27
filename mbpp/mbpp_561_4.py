def check(candidate):
    assert candidate([(5, 3), (7, 5), (2, 7), (3, 8), (8, 4)] ) == {3: [8], 5: [3], 7: [5], 2: [7], 8: [4], 4: []}
    assert candidate([(6, 4), (9, 4), (3, 8), (4, 9), (9, 5)] ) == {4: [9], 6: [4], 9: [4, 5], 8: [], 3: [8], 5: []}
    assert candidate([(6, 2), (6, 8), (4, 9), (4, 9), (3, 7)] ) == {2: [], 6: [2, 8], 8: [], 9: [], 4: [9, 9], 7: [], 3: [7]}


def pair_elements(tup):
    result = {}
    for i, val in enumerate(tup):
        if i % 2 == 0:
            result[val] = tup[i + 1] if i + 1 < len(tup) else None
        else:
            result[val] = tup[i - 1] if i - 1 >= 0 else None
    return result

check(pair_elements)