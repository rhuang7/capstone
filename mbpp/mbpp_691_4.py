def check(candidate):
    assert candidate([(6, 5), (2, 7), (2, 5), (8, 7), (9, 8), (3, 7)]) == {5: [6, 2], 7: [2, 8, 3], 8: [9]}
    assert candidate([(7, 6), (3, 8), (3, 6), (9, 8), (10, 9), (4, 8)]) == {6: [7, 3], 8: [3, 9, 4], 9: [10]}
    assert candidate([(8, 7), (4, 9), (4, 7), (10, 9), (11, 10), (5, 9)]) == {7: [8, 4], 9: [4, 10, 5], 10: [11]}


def group_by_second_element(tuples_list):
    grouped = {}
    for item in tuples_list:
        key = item[1]
        if key not in grouped:
            grouped[key] = []
        grouped[key].append(item[0])
    return grouped

check(group_by_second_element)