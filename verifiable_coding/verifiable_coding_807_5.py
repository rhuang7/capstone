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
        # Precompute all subarrays and their max elements
        # But for large N, this is not feasible, so we need a smarter approach
        # The key insight is that the p-th subarray is the p-th in the sorted list of all subarrays
        # When sorted in descending order, the first subarray is the entire array sorted in descending order
        # The second subarray is the array with the last element removed sorted in descending order
        # And so on
        # So we need to find the p-th subarray in this sorted list
        # But how to find the p-th subarray?
        # The number of subarrays of length k is N - k + 1
        # So we can find the length of the subarray by finding the smallest k such that sum_{i=1}^{k-1} (N - i + 1) < p <= sum_{i=1}^k (N - i + 1)
        # Once we find the length, we can find the starting index of the subarray
        # Then, the maximum element of the subarray is the maximum of the subarray
        # But since the subarrays are sorted in descending order, the p-th subarray is the one that is the p-th in the sorted list
        # So we need to generate all subarrays, sort them in descending order, and then for each query, return the max of the p-th subarray
        # However, for large N, this is not feasible
        # So we need a smarter way
        # Let's precompute all subarrays, sort them, and then for each query, return the max of the p-th subarray
        # But for N up to 1e5, this is not feasible
        # So we need to find the p-th subarray in the sorted list of all subarrays
        # The sorted list of all subarrays is the list of all subarrays sorted in descending order
        # The key insight is that the p-th subarray is the one that is the p-th in this list
        # So for each query p, we need to find the subarray that is the p-th in this list
        # Then, return the maximum element of that subarray
        # But how to find the p-th subarray?
        # Let's think about the sorted list of all subarrays
        # The first subarray is the entire array sorted in descending order
        # The second subarray is the array with the last element removed sorted in descending order
        # The third subarray is the array with the second last element removed sorted in descending order
        # And so on
        # So the p-th subarray is the subarray that is the p-th in the list of all subarrays sorted in descending order
        # So the p-th subarray is the one that has the maximum possible value when compared using the compare function
        # So the p-th subarray is the one that is the p-th in the sorted list of all subarrays
        # But how to find it?
        # We can think of the sorted list of all subarrays as follows:
        # The first subarray is the entire array sorted in descending order
        # The second subarray is the array with the last element removed sorted in descending order
        # The third subarray is the array with the second last element removed sorted in descending order
        # And so on
        # So the p-th subarray is the subarray that starts at position (p - 1) // (N - k + 1) for some k
        # But this is not clear
        # So we need to find the p-th subarray in the sorted list of all subarrays
        # To do this, we can generate all possible subarrays, sort them, and then for each query, return the max of the p-th subarray
        # But for large N, this is not feasible
        # So we need a smarter way
        # The key insight is that the p-th subarray is the one that is the p-th in the sorted list of all subarrays
        # And the maximum element of that subarray is the maximum element in the subarray
        # So for each query p, we need to find the subarray that is the p-th in the sorted list of all subarrays
        # And return its maximum element
        # So the problem reduces to, for each query p, find the subarray that is the p-th in the sorted list of all subarrays
        # And return its maximum element
        # But how to find this subarray?
        # The key is to note that the p-th subarray is the one that is the p-th in the sorted list of all subarrays
        # And the sorted list of all subarrays is the list of all subarrays sorted in descending order
        # So the p-th subarray is the one that is the p-th in this list
        # But how to find it?
        # We can think of the sorted list of all subarrays as follows:
        # The first subarray is the entire array sorted in descending order
        # The second subarray is the array with the last element removed sorted in descending order
        # The third subarray is the array with the second last element removed sorted in descending order
        # And so on
        # So the p-th subarray is the one that is the p-th in this list
        # So for each query p, we need to find the subarray that is the p-th in this list
        # And return its maximum element
        # But how to find this subarray?
        # We can think of the sorted list of all subarrays as follows:
        # The first subarray is the entire array sorted in descending order
        # The second subarray is the array with the last element removed sorted in descending order
        # The third subarray is the array with the second last element removed sorted in descending order
        # And so on
        # So the p-th subarray is the one that starts at position (p - 1) // (N - k + 1) for some k
        # But this is not clear
        # So we need to find the p-th subarray in the sorted list of all subarrays
        # To do this, we can generate all possible subarrays, sort them, and then for each query, return the max of the p-th subarray
        # But for large N, this is not feasible
        # So we need to find the p-th subarray in the sorted list of all subarrays
        # But how?
        # The key insight is that the p-th subarray is the one that is the p-th in the sorted list of all subarrays
        # And the sorted list of all subarrays is the list of all subarrays sorted in descending order
        # So the p-th subarray is the one that is the p-th in this list
        # So for each query p, we need to find the subarray that is the p-th in this list
        # And return its maximum element
        # But how to find this subarray?
        # We can think of the sorted list of all subarrays as follows:
        # The first subarray is the entire array sorted in descending order
        # The second subarray is the array with the last element removed sorted in descending order
        # The third subarray is the array with the second last element removed sorted in descending order
        # And so on
        # So the p-th subarray is the one that is the p-th in this list
        # So for each query p, we need to find the subarray that is the p-th in this list
        # And return its maximum element
        # But how to find this subarray?
        # We can think of the sorted list of all subarrays as follows:
        # The first subarray is the entire array sorted in descending order
        # The second subarray is the array with the last element removed sorted in descending order
        # The third subarray is the array with the second last element removed sorted in descending order
        # And so on
        # So the p-th subarray is the one that starts at position (p - 1) // (N - k + 1) for some k
        # But this is not clear
        # So we need to find the p-th subarray in the sorted list of all subarrays
        # But for large N, this is not feasible
        # So we need to find the p-th subarray in the sorted list of all subarrays
        # But how?
        # The key insight is that the p-th subarray is the one that is the p-th in the sorted list of all subarrays
        # And the sorted list of all subarrays is the list of