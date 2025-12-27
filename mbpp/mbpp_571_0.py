def check(candidate):
    assert candidate([3, 5, 10, 15, 17, 12, 9], 7, 4) == 62
    assert candidate([5, 15, 10, 300], 4, 12) == 25
    assert candidate([1, 2, 3, 4, 5, 6], 6, 6) == 21


def max_disjoint_pairs_sum(arr, k):
    if not arr or k <= 0:
        return 0
    
    n = len(arr)
    if n < 2:
        return 0
    
    # Sort the array
    arr.sort()
    
    # Initialize variables
    max_sum = 0
    i = 0
    
    # Iterate through the array
    while i < n:
        # Find the next element that is at least k away from the current element
        j = i + 1
        while j < n and arr[j] - arr[i] < k:
            j += 1
        
        # If a valid pair is found, add their sum to max_sum
        if j < n:
            max_sum += arr[i] + arr[j]
            i = j + 1
        else:
            # No valid pair found, move to next element
            i += 1
    
    return max_sum

check(max_disjoint_pairs_sum)