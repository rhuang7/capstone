def check(candidate):
    assert candidate([(6, 7), (2, 3), (7, 6), (9, 8), (10, 2), (8, 9)] ) == {(8, 9), (6, 7)}
    assert candidate([(7, 8), (3, 4), (8, 7), (10, 9), (11, 3), (9, 10)] ) == {(9, 10), (7, 8)}
    assert candidate([(8, 9), (4, 5), (9, 8), (11, 10), (12, 4), (10, 11)] ) == {(8, 9), (10, 11)}


def find_symmetric_pairs(tuple_list):
    symmetric_pairs = []
    seen = set()
    
    for t in tuple_list:
        if t in seen:
            symmetric_pairs.append(t)
        else:
            seen.add(t)
    
    return symmetric_pairs

check(find_symmetric_pairs)