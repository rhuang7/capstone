def check(candidate):
    assert candidate([1, 1, 3, 4, 5, 6, 7],[0, 1, 2, 3, 4, 5, 7],[0, 1, 2, 3, 4, 5, 7])==[1, 7]
    assert candidate([1, 1, 3, 4, 5, 6, 7],[0, 1, 2, 3, 4, 6, 5],[0, 1, 2, 3, 4, 6, 7])==[1, 6]
    assert candidate([1, 1, 3, 4, 6, 5, 6],[0, 1, 2, 3, 4, 5, 7],[0, 1, 2, 3, 4, 5, 7])==[1, 5]


def find_common_indices(list1, list2, list3):
    # Create sets of elements for each list
    set1 = set(list1)
    set2 = set(list2)
    set3 = set(list3)
    
    # Find the intersection of the three sets
    common_elements = set1 & set2 & set3
    
    # Return the common elements as a list
    return list(common_elements)

check(find_common_indices)