def check(candidate):
    assert candidate([1,23,4,5,6,7,8]) == [1, 4, 5, 6, 7, 8, 23]
    assert candidate([12, 9, 28, 33, 69, 45]) == [9, 12, 28, 33, 45, 69]
    assert candidate([8, 4, 14, 3, 2, 1]) == [1, 2, 3, 4, 8, 14]


def counting_sort(arr):
    if not arr:
        return []
    
    # Find the maximum value in the array
    max_val = max(arr)
    
    # Initialize count array
    count = [0] * (max_val + 1)
    
    # Count occurrences of each element
    for num in arr:
        count[num] += 1
    
    # Build the sorted array
    sorted_arr = []
    for i in range(len(count)):
        sorted_arr.extend([i] * count[i])
    
    return sorted_arr

check(counting_sort)