def check(candidate):
    assert candidate([2,2,2,2],4,3) == 0
    assert candidate([4,2,6,8],4,3) == -1
    assert candidate([21,33,9,45,63],5,6) == 24


def min_operations_to_equal(arr, k):
    from collections import Counter

    # Count the frequency of each element
    freq = Counter(arr)
    
    # Sort the elements based on their frequency
    sorted_elements = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    
    # Calculate the number of operations needed
    operations = 0
    for i in range(len(sorted_elements)):
        if i < k:
            # If we need to make at least k elements equal, we take the most frequent element
            operations += (sorted_elements[i][0] - sorted_elements[k-1][0]) * sorted_elements[i][1]
        else:
            # For elements beyond k, we don't need to consider them
            break
    
    return operations

check(min_operations_to_equal)