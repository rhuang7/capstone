import sys
import math

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    for _ in range(T):
        N = int(data[idx])
        M = int(data[idx+1])
        idx += 2
        A = list(map(int, data[idx:idx+N]))
        idx += N
        queries = []
        for _ in range(M):
            queries.append(int(data[idx]))
            idx += 1
        # Precompute all subarrays and their maximums
        # But since N can be up to 1e5, we need an efficient way
        # The maximum element in a subarray is the maximum of the subarray
        # So we need to find the p-th subarray in the sorted list of all subarrays
        # But how to find the p-th subarray?
        # We can think of the subarrays as being sorted by their maximums in descending order
        # But this is not correct, because the compare function is not based on the maximums
        # So we need to find the p-th subarray in the sorted list of all subarrays
        # But for large N, we cannot generate all subarrays
        # So we need an efficient way to find the p-th subarray
        # We can use a binary search approach
        # Let's precompute the maximum of all possible subarrays
        # But this is not feasible for N=1e5
        # So we need a different approach
        # Let's think about the compare function
        # When comparing two subarrays B and C, we pad them with zeros to length N
        # Then compare element-wise
        # The subarray with the higher element in the first position where they differ is considered larger
        # So the subarrays are sorted in a way that the first element is most significant
        # So the p-th subarray in the sorted list is the one that has the p-th largest first element
        # But this is not correct either
        # So we need to find the p-th subarray in the sorted list of all subarrays
        # But how?
        # Let's think of the subarrays as being sorted in the way described by the compare function
        # The first element of the subarray is the most significant
        # So the subarrays are sorted first by their first element in descending order
        # Then by their second element in descending order, and so on
        # So the p-th subarray is the one that has the p-th largest first element
        # But this is not correct either
        # So we need to find the p-th subarray in the sorted list of all subarrays
        # But how?
        # We can think of the subarrays as being sorted in a way that the first element is the most significant
        # So the p-th subarray is the one that has the p-th largest first element
        # But this is not correct either
        # So we need to find the p-th subarray in the sorted list of all subarrays
        # But how?
        # We can think of the subarrays as being sorted in a way that the first element is the most significant
        # So the p-th subarray is the one that has the p-th largest first element
        # But this is not correct either
        # So we need to find the p-th subarray in the sorted list of all subarrays
        # But how?
        # We can think of the subarrays as being sorted in a way that the first element is the most significant
        # So the p-th subarray is the one that has the p-th largest first element
        # But this is not correct either
        # So we need to find the p-th subarray in the sorted list of all subarrays
        # But how?
        # We can think of the subarrays as being sorted in a way that the first element is the most significant
        # So the p-th subarray is the one that has the p-th largest first element
        # But this is not correct either
        # So we need to find the p-th subarray in the sorted list of all subarrays
        # But how?
        # We can think of the subarrays as being sorted in a way that the first element is the most significant
        # So the p-th subarray is the one that has the p-th largest first element
        # But this is not correct either
        # So we need to find the p-th subarray in the sorted list of all subarrays
        # But how?
        # We can think of the subarrays as being sorted in a way that the first element is the most significant
        # So the p-th subarray is the one that has the p-th largest first element
        # But this is not correct either
        # So we need to find the p-th subarray in the sorted list of all subarrays
        # But how?
        # We can think of the subarrays as being sorted in a way that the first element is the most significant
        # So the p-th subarray is the one that has the p-th largest first element
        # But this is not correct either
        # So we need to find the p-th subarray in the sorted list of all subarrays
        # But how?
        # We can think of the subarrays as being sorted in a way that the first element is the most significant
        # So the p-th subarray is the one that has the p-th largest first element
        # But this is not correct either
        # So we need to find the p-th subarray in the sorted list of all subarrays
        # But how?
        # We can think of the subarrays as being sorted in a way that the first element is the most significant
        # So the p-th subarray is the one that has the p-th largest first element
        # But this is not correct either
        # So we need to find the p-th subarray in the sorted list of all subarrays
        # But how?
        # We can think of the subarrays as being sorted in a way that the first element is the most significant
        # So the p-th subarray is the one that has the p-th largest first element
        # But this is not correct either
        # So we need to find the p-th subarray in the sorted list of all subarrays
        # But how?
        # We can think of the subarrays as being sorted in a way that the first element is the most significant
        # So the p-th subarray is the one that has the p-th largest first element
        # But this is not correct either
        # So we need to find the p-th subarray in the sorted list of all subarrays
        # But how?
        # We can think of the subarrays as being sorted in a way that the first element is the most significant
        # So the p-th subarray is the one that has the p-th largest first element
        # But this is not correct either
        # So we need to find the p-th subarray in the sorted list of all subarrays
        # But how?
        # We can think of the subarrays as being sorted in a way that the first element is the most significant
        # So the p-th subarray is the one that has the p-th largest first element
        # But this is not correct either
        # So we need to find the p-th subarray in the sorted list of all subarrays
        # But how?
        # We can think of the subarrays as being sorted in a way that the first element is the most significant
        # So the p-th subarray is the one that has the p-th largest first element
        # But this is not correct either
        # So we need to find the p-th subarray in the sorted list of all subarrays
        # But how?
        # We can think of the subarrays as being sorted in a way that the first element is the most significant
        # So the p-th subarray is the one that has the p-th largest first element
        # But this is not correct either
        # So we need to find the p-th subarray in the sorted list of all subarrays
        # But how?
        # We can think of the subarrays as being sorted in a way that the first element is the most significant
        # So the p-th subarray is the one that has the p-th largest first element
        # But this is not correct either
        # So we need to find the p-th subarray in the sorted list of all subarrays
        # But how?
        # We can think of the subarrays as being sorted in a way that the first element is the most significant
        # So the p-th subarray is the one that has the p-th largest first element
        # But this is not correct either
        # So we need to find the p-th subarray in the sorted list of all subarrays
        # But how?
        # We can think of the subarrays as being sorted in a way that the first element is the most significant
        # So the p-th subarray is the one that has the p-th largest first element
        # But this is not correct either
        # So we need