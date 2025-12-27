def check(candidate):
    assert candidate([(5, 6), (5, 7), (6, 8), (6, 10), (7, 13)] ) == [(5, 6, 7), (6, 8, 10), (7, 13)]
    assert candidate([(6, 7), (6, 8), (7, 9), (7, 11), (8, 14)] ) == [(6, 7, 8), (7, 9, 11), (8, 14)]
    assert candidate([(7, 8), (7, 9), (8, 10), (8, 12), (9, 15)] ) == [(7, 8, 9), (8, 10, 12), (9, 15)]


def join_similar_tuples(tuples_list):
    if not tuples_list:
        return []
    
    result = []
    current = tuples_list[0]
    result.append(current)
    
    for t in tuples_list[1:]:
        if t[0] == current[0]:
            current = current + t
        else:
            result.append(t)
            current = t
    
    return result

check(join_similar_tuples)