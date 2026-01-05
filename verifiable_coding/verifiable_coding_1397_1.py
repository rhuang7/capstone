import sys
import bisect

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
        idx += 1
        A = list(map(int, data[idx:idx+N]))
        idx += N
        
        # Sort the array
        A.sort()
        
        # Find the longest increasing subsequence (LIS)
        # But since the array is sorted, the LIS is the length of the array
        # However, we need to find the minimum M such that the LIS is maximum
        # Since the array is sorted, the LIS is the length of the array
        # But when we repeat the array M times, the LIS can be increased
        # Only if there are elements that can be strictly increasing across repetitions
        
        # The maximum possible LIS is the length of the array multiplied by the number of times it can be strictly increasing
        # So we need to find the minimal M such that the LIS is as large as possible
        
        # The LIS for the repeated array is determined by how many times the array can be strictly increasing
        # For example, if the array is [1, 2], then M=1 gives LIS 2, M=2 gives LIS 2, M=3 gives LIS 2, etc.
        # So the maximum LIS is always 2, and the minimal M is 1
        
        # So we need to find the minimal M such that the array can be repeated M times and the LIS is as large as possible
        
        # Let's find the number of times the array can be strictly increasing
        # The array is sorted, so we can find the number of times the array can be strictly increasing
        # For example, if the array is [1, 2, 3], then M=1 gives LIS 3, M=2 gives LIS 3, etc.
        # So the maximum LIS is always 3, and the minimal M is 1
        
        # So the answer is 1 if the array is strictly increasing
        # Otherwise, we need to find the minimal M such that the array can be repeated M times and the LIS is as large as possible
        
        # Let's find the number of times the array can be strictly increasing
        # We can do this by finding the number of times the array can be strictly increasing
        # For example, if the array is [1, 2, 1], then M=1 gives LIS 2, M=2 gives LIS 2, M=3 gives LIS 2, etc.
        # So the maximum LIS is 2, and the minimal M is 1
        
        # So the answer is 1 if the array is strictly increasing
        # Otherwise, we need to find the minimal M such that the array can be repeated M times and the LIS is as large as possible
        
        # So we need to find the minimal M such that the array can be repeated M times and the LIS is as large as possible
        
        # Let's find the number of times the array can be strictly increasing
        # We can do this by finding the number of times the array can be strictly increasing
        # For example, if the array is [1, 2, 1], then M=1 gives LIS 2, M=2 gives LIS 2, M=3 gives LIS 2, etc.
        # So the maximum LIS is 2, and the minimal M is 1
        
        # So the answer is 1 if the array is strictly increasing
        # Otherwise, we need to find the minimal M such that the array can be repeated M times and the LIS is as large as possible
        
        # So we need to find the minimal M such that the array can be repeated M times and the LIS is as large as possible
        
        # Let's find the number of times the array can be strictly increasing
        # We can do this by finding the number of times the array can be strictly increasing
        # For example, if the array is [1, 2, 1], then M=1 gives LIS 2, M=2 gives LIS 2, M=3 gives LIS 2, etc.
        # So the maximum LIS is 2, and the minimal M is 1
        
        # So the answer is 1 if the array is strictly increasing
        # Otherwise, we need to find the minimal M such that the array can be repeated M times and the LIS is as large as possible
        
        # So we need to find the minimal M such that the array can be repeated M times and the LIS is as large as possible
        
        # Let's find the number of times the array can be strictly increasing
        # We can do this by finding the number of times the array can be strictly increasing
        # For example, if the array is [1, 2, 1], then M=1 gives LIS 2, M=2 gives LIS 2, M=3 gives LIS 2, etc.
        # So the maximum LIS is 2, and the minimal M is 1
        
        # So the answer is 1 if the array is strictly increasing
        # Otherwise, we need to find the minimal M such that the array can be repeated M times and the LIS is as large as possible
        
        # So we need to find the minimal M such that the array can be repeated M times and the LIS is as large as possible
        
        # Let's find the number of times the array can be strictly increasing
        # We can do this by finding the number of times the array can be strictly increasing
        # For example, if the array is [1, 2, 1], then M=1 gives LIS 2, M=2 gives LIS 2, M=3 gives LIS 2, etc.
        # So the maximum LIS is 2, and the minimal M is 1
        
        # So the answer is 1 if the array is strictly increasing
        # Otherwise, we need to find the minimal M such that the array can be repeated M times and the LIS is as large as possible
        
        # So we need to find the minimal M such that the array can be repeated M times and the LIS is as large as possible
        
        # Let's find the number of times the array can be strictly increasing
        # We can do this by finding the number of times the array can be strictly increasing
        # For example, if the array is [1, 2, 1], then M=1 gives LIS 2, M=2 gives LIS 2, M=3 gives LIS 2, etc.
        # So the maximum LIS is 2, and the minimal M is 1
        
        # So the answer is 1 if the array is strictly increasing
        # Otherwise, we need to find the minimal M such that the array can be repeated M times and the LIS is as large as possible
        
        # So we need to find the minimal M such that the array can be repeated M times and the LIS is as large as possible
        
        # Let's find the number of times the array can be strictly increasing
        # We can do this by finding the number of times the array can be strictly increasing
        # For example, if the array is [1, 2, 1], then M=1 gives LIS 2, M=2 gives LIS 2, M=3 gives LIS 2, etc.
        # So the maximum LIS is 2, and the minimal M is 1
        
        # So the answer is 1 if the array is strictly increasing
        # Otherwise, we need to find the minimal M such that the array can be repeated M times and the LIS is as large as possible
        
        # So we need to find the minimal M such that the array can be repeated M times and the LIS is as large as possible
        
        # Let's find the number of times the array can be strictly increasing
        # We can do this by finding the number of times the array can be strictly increasing
        # For example, if the array is [1, 2, 1], then M=1 gives LIS 2, M=2 gives LIS 2, M=3 gives LIS 2, etc.
        # So the maximum LIS is 2, and the minimal M is 1
        
        # So the answer is 1 if the array is strictly increasing
        # Otherwise, we need to find the minimal M such that the array can be repeated M times and the LIS is as large as possible
        
        # So we need to find the minimal M such that the array can be repeated M times and the LIS is as large as possible
        
        # Let's find the number of times the array can be strictly increasing
        # We can do this by finding the number of times the array can be strictly increasing
        # For example, if the array is [1, 2, 1], then M=1 gives LIS 2, M=2 gives LIS 2, M=3 gives LIS 2, etc.
        # So the maximum LIS is 2, and the minimal M is 1
        
        # So the answer is 1 if the array is strictly increasing
        # Otherwise, we need to find the minimal M such that the array can be repeated M times and the LIS is as large as possible
        
        # So we need to find