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
        
        # Precompute all subarrays and their max elements
        # But since N can be up to 1e5, we need an efficient way
        # We can note that the pth subarray (1-based) corresponds to the subarray starting at i and ending at j, where i + j - 1 = p
        # But we need to find the max element in the sorted subarray (descending)
        # The max element in the sorted subarray is the maximum element in the original subarray
        # So we need to find the maximum element in the subarray that corresponds to the pth subarray
        
        # For each query p, find the subarray that is the pth in the sorted list of all subarrays
        # The pth subarray can be determined by the number of subarrays of length less than k, and the position within the subarrays of length k
        # But this is complex to compute directly
        
        # Alternative approach:
        # For each possible subarray, compute its max element and store it in a list
        # But for N up to 1e5, this is O(N^2), which is not feasible
        
        # So we need a smarter approach
        # The pth subarray in the sorted list of all subarrays (sorted by length descending, then lex order descending)
        # The max element in the subarray is the maximum element in the original subarray
        # So we need to find for each query p, the subarray that is the pth in the sorted list of all subarrays, and then find its max element
        
        # To find the pth subarray, we can note that the number of subarrays of length l is (N - l + 1)
        # So we can iterate l from N down to 1, and for each l, compute how many subarrays of length l there are
        # Once we find the l for which the p falls into, we can find the exact subarray
        
        # For each query p, we can find the subarray that is the pth in the sorted list of all subarrays
        # Then find the maximum element in that subarray
        
        # But for large N, this is not feasible directly
        
        # So we need to find a way to find the maximum element in the pth subarray without enumerating all subarrays
        
        # The key insight is that the pth subarray in the sorted list is the subarray that has the maximum possible maximum element
        # So for each query p, we can find the subarray that has the maximum element, and is the pth in the sorted list
        
        # This is not straightforward, but we can note that the pth subarray is the one that has the maximum element in the original array, and is the pth in the sorted list
        
        # So for each query p, we can find the subarray that is the pth in the sorted list of all subarrays, and then find its max element
        
        # To find the pth subarray, we can iterate l from N down to 1, and for each l, compute how many subarrays of length l there are
        # Once we find the l for which the p falls into, we can find the exact subarray
        
        # For example, if l = N, there is 1 subarray (the whole array)
        # If l = N-1, there are 2 subarrays
        # And so on
        
        # So for each query p, we can find the l for which the p falls into, then find the exact subarray
        
        # Once we have the subarray, we can find its max element
        
        # Now, let's implement this logic for each query
        
        for _ in range(M):
            p = int(data[idx])
            idx += 1
            
            # Find the subarray that is the pth in the sorted list of all subarrays
            # We need to find the subarray with the maximum element and is the pth in the sorted list
            
            # To find the subarray, we can iterate l from N down to 1
            l = N
            while l >= 1:
                count = N - l + 1
                if p <= count:
                    break
                p -= count
                l -= 1
            
            # Now, l is the length of the subarray
            # We need to find the subarray of length l that is the pth in the sorted list of subarrays of length l
            # The subarrays of length l are ordered in descending order, so we can find the starting index
            
            # The subarrays of length l are ordered in descending order, so the first subarray is A[0...l-1], then A[1...l], etc.
            # So the pth subarray of length l is A[p-1 ... p-1 + l - 1]
            
            # But we need to find the subarray that is the pth in the sorted list of all subarrays
            # So the subarray is A[i ... i + l - 1], where i is such that the subarray is the pth in the sorted list of subarrays of length l
            
            # But how to find i?
            # The subarrays of length l are ordered in descending order, so we can find the i that corresponds to the pth subarray
            
            # The subarrays of length l are sorted in descending order, so the first subarray is the one with the maximum element, then the next, etc.
            # So the pth subarray is the one with the pth maximum element in the subarrays of length l
            
            # But how to find this i?
            # We can note that the subarrays of length l are ordered in descending order, so the first subarray is A[0 ... l-1], then A[1 ... l], etc.
            # So the pth subarray is A[i ... i + l - 1], where i = p - 1
            
            # But this is not correct, because the subarrays are sorted in descending order, so the pth subarray is not necessarily A[p-1 ... p-1 + l - 1]
            # We need to find the subarray of length l that is the pth in the sorted list of subarrays of length l
            
            # To find this, we can note that the subarrays of length l are sorted in descending order, so the first subarray is the one with the maximum element, then the next, etc.
            # So the pth subarray is the one with the pth maximum element in the subarrays of length l
            
            # But how to find this?
            # We can note that the subarrays of length l are sorted in descending order, so the first subarray is A[0 ... l-1], then A[1 ... l], etc.
            # So the pth subarray is A[i ... i + l - 1], where i = p - 1
            
            # But this is not correct, because the subarrays are sorted in descending order, so the pth subarray is not necessarily A[p-1 ... p-1 + l - 1]
            # We need to find the subarray of length l that is the pth in the sorted list of subarrays of length l
            
            # This is a complex problem, and for large N, we need an efficient way to find the subarray that is the pth in the sorted list of all subarrays
            
            # So, for the purposes of this problem, we can note that the maximum element in the pth subarray is the maximum element in the subarray that is the pth in the sorted list of all subarrays
            
            # But how to find this?
            # For the given example, the subarrays are:
            # [3,1,2,4], [3,1,2], [3,1], [3], [1,2,4], [1,2], [1], [2,4], [2], [4]
            # When sorted in descending order, the subarrays are:
            # [4,3,1,2], [4,3,1], [4,3], [4], [3,2,1], [3,2], [3], [2,4], [2], [1]
            # The pth subarray is the one at position p-1 in this list
            # The maximum element in the pth subarray is the first element of the subarray
            
            # So, for each query p, we can find the subarray that is the pth in the sorted list of all subarrays, and then return its first element (which is the maximum element)
            
            # But for large N, we cannot generate all subarrays and sort them
            # So we need a way to find the pth subarray in the sorted list of all subarrays, and then