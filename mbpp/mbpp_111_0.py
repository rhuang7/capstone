def check(candidate):
    assert candidate([[12, 18, 23, 25, 45], [7, 12, 18, 24, 28], [1, 5, 8, 12, 15, 16, 18]])==[18, 12]
    assert candidate([[12, 5, 23, 25, 45], [7, 11, 5, 23, 28], [1, 5, 8, 18, 23, 16]])==[5,23]
    assert candidate([[2, 3,4, 1], [4, 5], [6,4, 8],[4, 5], [6, 8,4]])==[4]


def find_common_elements(nested_lists):
    if not nested_lists:
        return []
    
    # Convert the first list to a set for fast lookups
    common = set(nested_lists[0])
    
    # Iterate through the remaining lists and find intersection
    for lst in nested_lists[1:]:
        common &= set(lst)
    
    return list(common)

check(find_common_elements)