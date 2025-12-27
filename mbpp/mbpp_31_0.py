def check(candidate):
    assert candidate([[1, 2, 6], [1, 3, 4, 5, 7, 8], [1, 3, 5, 6, 8, 9], [2, 5, 7, 11], [1, 4, 7, 8, 12]],3)==[5, 7, 1]
    assert candidate([[1, 2, 6], [1, 3, 4, 5, 7, 8], [1, 3, 5, 6, 8, 9], [2, 5, 7, 11], [1, 4, 7, 8, 12]],1)==[1]
    assert candidate([[1, 2, 6], [1, 3, 4, 5, 7, 8], [1, 3, 5, 6, 8, 9], [2, 5, 7, 11], [1, 4, 7, 8, 12]],5)==[6, 5, 7, 8, 1]


def top_k_most_frequent(nums, k):
    from collections import Counter
    from heapq import nlargest

    # Count frequency of each number
    freq = Counter(nums)
    
    # Get the k most frequent elements
    top_k = nlargest(k, freq.items(), key=lambda x: x[1])
    
    # Extract the numbers from the tuples
    result = [num for num, count in top_k]
    
    return result

check(top_k_most_frequent)