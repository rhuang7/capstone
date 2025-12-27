def check(candidate):
    assert candidate([(3, 4), (5, 6), (9, 10), (4, 5)] , [(5, 4), (3, 4), (6, 5), (9, 11)]) == {(4, 5), (3, 4), (5, 6)}
    assert candidate([(4, 1), (7, 4), (11, 13), (17, 14)] , [(1, 4), (7, 4), (16, 12), (10, 13)]) == {(4, 7), (1, 4)}
    assert candidate([(2, 1), (3, 2), (1, 3), (1, 4)] , [(11, 2), (2, 3), (6, 2), (1, 3)]) == {(1, 3), (2, 3)}


def tuple_intersection(tuples_list):
    if not tuples_list:
        return ()
    
    # Convert the first tuple to a set for fast lookups
    common_elements = set(tuples_list[0])
    
    # Iterate through the remaining tuples and find common elements
    for t in tuples_list[1:]:
        common_elements.intersection_update(t)
        if not common_elements:
            break  # No elements in common, can exit early
    
    return tuple(common_elements)

check(tuple_intersection)