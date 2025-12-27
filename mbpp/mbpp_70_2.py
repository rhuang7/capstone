def check(candidate):
    assert candidate([(11, 22, 33), (44, 55, 66)], 3) == 'All tuples have same length'
    assert candidate([(1, 2, 3), (4, 5, 6, 7)], 3) == 'All tuples do not have same length'
    assert candidate([(1, 2), (3, 4)], 2) == 'All tuples have same length'


def all_tuples_equal_length(tuples_list):
    if not tuples_list:
        return True  # An empty list is considered to have all tuples of equal length (0)
    
    # Get the length of the first tuple
    first_length = len(tuples_list[0])
    
    # Check if all other tuples have the same length
    for t in tuples_list[1:]:
        if len(t) != first_length:
            return False
    
    return True

check(all_tuples_equal_length)