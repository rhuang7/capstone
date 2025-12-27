def check(candidate):
    assert candidate([0 , 8 , 4, 12, 2, 10 , 6 , 14 , 1 , 9 , 5 , 13, 3, 11 , 7 , 15]) == 7
    assert candidate([1, 11, 2, 10, 4, 5, 2, 1]) == 6
    assert candidate([80, 60, 30, 40, 20, 10]) == 5


def longest_bitonic_subsequence(arr):
    n = len(arr)
    if n == 0:
        return []
    
    # Initialize arrays for increasing and decreasing subsequences
    inc = [1] * n
    dec = [1] * n
    
    # Build increasing subsequence array
    for i in range(n):
        for j in range(i):
            if arr[j] < arr[i]:
                inc[i] = max(inc[i], inc[j] + 1)
    
    # Build decreasing subsequence array
    for i in range(n-1, -1, -1):
        for j in range(i+1, n):
            if arr[j] < arr[i]:
                dec[i] = max(dec[i], dec[j] + 1)
    
    # Find the maximum length of bitonic subsequence
    max_len = 0
    max_index = 0
    for i in range(n):
        if inc[i] + dec[i] - 1 > max_len:
            max_len = inc[i] + dec[i] - 1
            max_index = i
    
    # Reconstruct the bitonic subsequence
    subseq = []
    i = max_index
    while i >= 0 and inc[i] > 0:
        subseq.append(arr[i])
        i -= 1
    i = max_index
    while i < n and dec[i] > 0:
        subseq.append(arr[i])
        i += 1
    subseq.reverse()
    
    return subseq

check(longest_bitonic_subsequence)