def check(candidate):
    assert candidate([(2, 4), (6, 7), (5, 1)],[(5, 4), (8, 10), (8, 14)]) == [(5, 4), (8, 10), (8, 14)]
    assert candidate([(3, 5), (7, 8), (6, 2)],[(6, 5), (9, 11), (9, 15)]) == [(6, 5), (9, 11), (9, 15)]
    assert candidate([(4, 6), (8, 9), (7, 3)],[(7, 6), (10, 12), (10, 16)]) == [(7, 6), (10, 12), (10, 16)]


def max_at_similar_indices(list1, list2):
    if len(list1) != len(list2):
        raise ValueError("Both lists must have the same length.")
    
    max_value = float('-inf')
    for i in range(len(list1)):
        current_max = max(list1[i], list2[i])
        if current_max > max_value:
            max_value = current_max
    return max_value

check(max_at_similar_indices)