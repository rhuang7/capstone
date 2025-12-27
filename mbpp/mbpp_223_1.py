def check(candidate):
    assert candidate([1, 2, 3, 3, 3, 3, 10], 7, 3) == True
    assert candidate([1, 1, 2, 4, 4, 4, 6, 6], 8, 4) == False
    assert candidate([1, 1, 1, 2, 2], 5, 1) == True


def find_majority_element(sorted_array):
    if not sorted_array:
        return None
    
    n = len(sorted_array)
    mid = n // 2
    
    # Check if the middle element is majority
    if sorted_array[mid] == sorted_array[mid - 1]:
        return sorted_array[mid]
    
    # Check if the element before mid is majority
    if sorted_array[mid - 1] == sorted_array[mid - 2]:
        return sorted_array[mid - 1]
    
    # Check if the element after mid is majority
    if sorted_array[mid] == sorted_array[mid + 1]:
        return sorted_array[mid]
    
    return None

check(find_majority_element)