def check(candidate):
    assert candidate(8,5) == 2
    assert candidate(7,2) == 3
    assert candidate(5,2) == 3


def find_kth_element(arr, k):
    # Separate the array into odd and even elements
    odds = [x for x in arr if x % 2 != 0]
    evens = [x for x in arr if x % 2 == 0]
    
    # Combine them: odds first, then evens
    combined = odds + evens
    
    # Check if k is within the bounds of the combined array
    if k > len(combined):
        raise ValueError("k is out of range")
    
    # Return the kth element (1-based index)
    return combined[k - 1]

check(find_kth_element)