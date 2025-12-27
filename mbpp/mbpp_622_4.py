def check(candidate):
    assert candidate([1, 12, 15, 26, 38], [2, 13, 17, 30, 45], 5) == 16.0
    assert candidate([2, 4, 8, 9], [7, 13, 19, 28], 4) == 8.5
    assert candidate([3, 6, 14, 23, 36, 42], [2, 18, 27, 39, 49, 55], 6) == 25.0


def find_median_of_two_sorted_arrays(arr1, arr2):
    # Merge the two sorted arrays
    merged = []
    i = j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1
    # Add remaining elements
    while i < len(arr1):
        merged.append(arr1[i])
        i += 1
    while j < len(arr2):
        merged.append(arr2[j])
        j += 1
    
    # Find the median
    n = len(merged)
    if n % 2 == 1:
        return merged[n // 2]
    else:
        return (merged[n // 2 - 1] + merged[n // 2]) / 2

check(find_median_of_two_sorted_arrays)