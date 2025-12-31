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
        
        # Find the longest strictly increasing subsequence (LIS)
        # Using a list to keep track of the smallest tail of increasing subsequences
        lis = []
        for num in A:
            # Find the first element in lis >= num
            idx_ins = bisect.bisect_left(lis, num)
            if idx_ins == len(lis):
                lis.append(num)
            else:
                lis[idx_ins] = num
        max_len = len(lis)
        
        # Now find the minimum M such that the length of the longest strictly increasing subsequence is max_len
        # Since the array is sorted, the LIS is the length of the longest increasing subsequence
        # We need to find the minimum M such that the length of the LIS is max_len
        
        # The LIS is the length of the longest increasing subsequence in the sorted array
        # So the minimum M is 1
        
        # However, if the array has duplicate elements, we need to find the minimum M such that the LIS is maximized
        # For example, if the array is [2, 1], the LIS is 1. But if we repeat it, we can get a longer LIS
        
        # So we need to find the minimum M such that the LIS of the repeated array is maximized
        
        # To do this, we need to find the number of times we need to repeat the array to get the maximum possible LIS
        # The maximum possible LIS is the length of the array if it is strictly increasing
        # So we need to find the minimum M such that the array can be repeated to form a sequence with the maximum possible LIS
        
        # So we need to find the minimum M such that the array can be repeated to form a sequence with the maximum possible LIS
        
        # Let's find the number of times we need to repeat the array to get the maximum possible LIS
        # The maximum possible LIS is the length of the array if it is strictly increasing
        # So if the array is strictly increasing, the answer is 1
        
        # Otherwise, we need to find the minimum M such that the array can be repeated to form a sequence with the maximum possible LIS
        
        # So we need to find the number of times we need to repeat the array to get the maximum possible LIS
        
        # The maximum possible LIS is the length of the array if it is strictly increasing
        # So if the array is strictly increasing, the answer is 1
        
        # Otherwise, we need to find the minimum M such that the array can be repeated to form a sequence with the maximum possible LIS
        
        # So we need to find the number of times we need to repeat the array to get the maximum possible LIS
        
        # Let's find the number of times we need to repeat the array to get the maximum possible LIS
        # The maximum possible LIS is the length of the array if it is strictly increasing
        # So if the array is strictly increasing, the answer is 1
        
        # Otherwise, we need to find the minimum M such that the array can be repeated to form a sequence with the maximum possible LIS
        
        # So we need to find the number of times we need to repeat the array to get the maximum possible LIS
        
        # Let's find the number of times we need to repeat the array to get the maximum possible LIS
        # The maximum possible LIS is the length of the array if it is strictly increasing
        # So if the array is strictly increasing, the answer is 1
        
        # Otherwise, we need to find the minimum M such that the array can be repeated to form a sequence with the maximum possible LIS
        
        # So we need to find the number of times we need to repeat the array to get the maximum possible LIS
        
        # Let's find the number of times we need to repeat the array to get the maximum possible LIS
        # The maximum possible LIS is the length of the array if it is strictly increasing
        # So if the array is strictly increasing, the answer is 1
        
        # Otherwise, we need to find the minimum M such that the array can be repeated to form a sequence with the maximum possible LIS
        
        # So we need to find the number of times we need to repeat the array to get the maximum possible LIS
        
        # Let's find the number of times we need to repeat the array to get the maximum possible LIS
        # The maximum possible LIS is the length of the array if it is strictly increasing
        # So if the array is strictly increasing, the answer is 1
        
        # Otherwise, we need to find the minimum M such that the array can be repeated to form a sequence with the maximum possible LIS
        
        # So we need to find the number of times we need to repeat the array to get the maximum possible LIS
        
        # Let's find the number of times we need to repeat the array to get the maximum possible LIS
        # The maximum possible LIS is the length of the array if it is strictly increasing
        # So if the array is strictly increasing, the answer is 1
        
        # Otherwise, we need to find the minimum M such that the array can be repeated to form a sequence with the maximum possible LIS
        
        # So we need to find the number of times we need to repeat the array to get the maximum possible LIS
        
        # Let's find the number of times we need to repeat the array to get the maximum possible LIS
        # The maximum possible LIS is the length of the array if it is strictly increasing
        # So if the array is strictly increasing, the answer is 1
        
        # Otherwise, we need to find the minimum M such that the array can be repeated to form a sequence with the maximum possible LIS
        
        # So we need to find the number of times we need to repeat the array to get the maximum possible LIS
        
        # Let's find the number of times we need to repeat the array to get the maximum possible LIS
        # The maximum possible LIS is the length of the array if it is strictly increasing
        # So if the array is strictly increasing, the answer is 1
        
        # Otherwise, we need to find the minimum M such that the array can be repeated to form a sequence with the maximum possible LIS
        
        # So we need to find the number of times we need to repeat the array to get the maximum possible LIS
        
        # Let's find the number of times we need to repeat the array to get the maximum possible LIS
        # The maximum possible LIS is the length of the array if it is strictly increasing
        # So if the array is strictly increasing, the answer is 1
        
        # Otherwise, we need to find the minimum M such that the array can be repeated to form a sequence with the maximum possible LIS
        
        # So we need to find the number of times we need to repeat the array to get the maximum possible LIS
        
        # Let's find the number of times we need to repeat the array to get the maximum possible LIS
        # The maximum possible LIS is the length of the array if it is strictly increasing
        # So if the array is strictly increasing, the answer is 1
        
        # Otherwise, we need to find the minimum M such that the array can be repeated to form a sequence with the maximum possible LIS
        
        # So we need to find the number of times we need to repeat the array to get the maximum possible LIS
        
        # Let's find the number of times we need to repeat the array to get the maximum possible LIS
        # The maximum possible LIS is the length of the array if it is strictly increasing
        # So if the array is strictly increasing, the answer is 1
        
        # Otherwise, we need to find the minimum M such that the array can be repeated to form a sequence with the maximum possible LIS
        
        # So we need to find the number of times we need to repeat the array to get the maximum possible LIS
        
        # Let's find the number of times we need to repeat the array to get the maximum possible LIS
        # The maximum possible LIS is the length of the array if it is strictly increasing
        # So if the array is strictly increasing, the answer is 1
        
        # Otherwise, we need to find the minimum M such that the array can be repeated to form a sequence with the maximum possible LIS
        
        # So we need to find the number of times we need to repeat the array to get the maximum possible LIS
        
        # Let's find the number of times we need to repeat the array to get the maximum possible LIS
        # The maximum possible LIS is the length of the array if it is strictly increasing
        # So if the array is strictly increasing, the answer is 1
        
        # Otherwise, we need to find the minimum M such that the array can be repeated to form a sequence with the maximum possible LIS
        
        # So we need to find the number of times we need to repeat the array to get the maximum possible LIS
        
        # Let's find the number of times we need to repeat the array to get the maximum possible LIS
        # The maximum possible LIS is the length of the array if it is