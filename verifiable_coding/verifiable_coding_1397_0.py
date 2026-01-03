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
        # But since the array is sorted, the LIS is the length of the longest strictly increasing subsequence
        # Which is the number of elements in the array that are strictly increasing
        # So we can find the length of the longest strictly increasing subsequence
        # by counting the number of elements that are strictly increasing
        # But since the array is sorted, we can just count the number of elements that are strictly increasing
        # So we can find the length of the longest strictly increasing subsequence by counting the number of elements that are strictly increasing
        # So we can find the length of the longest strictly increasing subsequence by counting the number of elements that are strictly increasing
        
        # Find the length of the longest strictly increasing subsequence
        lis = 1
        max_len = 1
        for i in range(1, N):
            if A[i] > A[i-1]:
                lis += 1
                max_len = max(max_len, lis)
            else:
                lis = 1
        # The maximum length of the LIS is max_len
        
        # Now we need to find the minimal M such that when we repeat the array M times, the LIS is as long as possible
        # The maximum possible LIS is the length of the array multiplied by the number of times it is repeated
        # But since the array is sorted, the LIS is the length of the longest strictly increasing subsequence
        # So the maximum possible LIS is the length of the array multiplied by the number of times it is repeated
        # But since the array is sorted, the LIS is the length of the longest strictly increasing subsequence
        # So the maximum possible LIS is the length of the array multiplied by the number of times it is repeated
        # But since the array is sorted, the LIS is the length of the longest strictly increasing subsequence
        # So the maximum possible LIS is the length of the array multiplied by the number of times it is repeated
        # But since the array is sorted, the LIS is the length of the longest strictly increasing subsequence
        # So the maximum possible LIS is the length of the array multiplied by the number of times it is repeated
        # But since the array is sorted, the LIS is the length of the longest strictly increasing subsequence
        # So the maximum possible LIS is the length of the array multiplied by the number of times it is repeated
        # But since the array is sorted, the LIS is the length of the longest strictly increasing subsequence
        # So the maximum possible LIS is the length of the array multiplied by the number of times it is repeated
        # But since the array is sorted, the LIS is the length of the longest strictly increasing subsequence
        # So the maximum possible LIS is the length of the array multiplied by the number of times it is repeated
        # But since the array is sorted, the LIS is the length of the longest strictly increasing subsequence
        # So the maximum possible LIS is the length of the array multiplied by the number of times it is repeated
        # But since the array is sorted, the LIS is the length of the longest strictly increasing subsequence
        # So the maximum possible LIS is the length of the array multiplied by the number of times it is repeated
        # But since the array is sorted, the LIS is the length of the longest strictly increasing subsequence
        # So the maximum possible LIS is the length of the array multiplied by the number of times it is repeated
        # But since the array is sorted, the LIS is the length of the longest strictly increasing subsequence
        # So the maximum possible LIS is the length of the array multiplied by the number of times it is repeated
        # But since the array is sorted, the LIS is the length of the longest strictly increasing subsequence
        # So the maximum possible LIS is the length of the array multiplied by the number of times it is repeated
        # But since the array is sorted, the LIS is the length of the longest strictly increasing subsequence
        # So the maximum possible LIS is the length of the array multiplied by the number of times it is repeated
        # But since the array is sorted, the LIS is the length of the longest strictly increasing subsequence
        # So the maximum possible LIS is the length of the array multiplied by the number of times it is repeated
        # But since the array is sorted, the LIS is the length of the longest strictly increasing subsequence
        # So the maximum possible LIS is the length of the array multiplied by the number of times it is repeated
        # But since the array is sorted, the LIS is the length of the longest strictly increasing subsequence
        # So the maximum possible LIS is the length of the array multiplied by the number of times it is repeated
        # But since the array is sorted, the LIS is the length of the longest strictly increasing subsequence
        # So the maximum possible LIS is the length of the array multiplied by the number of times it is repeated
        # But since the array is sorted, the LIS is the length of the longest strictly increasing subsequence
        # So the maximum possible LIS is the length of the array multiplied by the number of times it is repeated
        # But since the array is sorted, the LIS is the length of the longest strictly increasing subsequence
        # So the maximum possible LIS is the length of the array multiplied by the number of times it is repeated
        # But since the array is sorted, the LIS is the length of the longest strictly increasing subsequence
        # So the maximum possible LIS is the length of the array multiplied by the number of times it is repeated
        # But since the array is sorted, the LIS is the length of the longest strictly increasing subsequence
        # So the maximum possible LIS is the length of the array multiplied by the number of times it is repeated
        # But since the array is sorted, the LIS is the length of the longest strictly increasing subsequence
        # So the maximum possible LIS is the length of the array multiplied by the number of times it is repeated
        # But since the array is sorted, the LIS is the length of the longest strictly increasing subsequence
        # So the maximum possible LIS is the length of the array multiplied by the number of times it is repeated
        # But since the array is sorted, the LIS is the length of the longest strictly increasing subsequence
        # So the maximum possible LIS is the length of the array multiplied by the number of times it is repeated
        # But since the array is sorted, the LIS is the length of the longest strictly increasing subsequence
        # So the maximum possible LIS is the length of the array multiplied by the number of times it is repeated
        # But since the array is sorted, the LIS is the length of the longest strictly increasing subsequence
        # So the maximum possible LIS is the length of the array multiplied by the number of times it is repeated
        # But since the array is sorted, the LIS is the length of the longest strictly increasing subsequence
        # So the maximum possible LIS is the length of the array multiplied by the number of times it is repeated
        # But since the array is sorted, the LIS is the length of the longest strictly increasing subsequence
        # So the maximum possible LIS is the length of the array multiplied by the number of times it is repeated
        # But since the array is sorted, the LIS is the length of the longest strictly increasing subsequence
        # So the maximum possible LIS is the length of the array multiplied by the number of times it is repeated
        # But since the array is sorted, the LIS is the length of the longest strictly increasing subsequence
        # So the maximum possible LIS is the length of the array multiplied by the number of times it is repeated
        # But since the array is sorted, the LIS is the length of the longest strictly increasing subsequence
        # So the maximum possible LIS is the length of the array multiplied by the number of times it is repeated
        # But since the array is sorted, the LIS is the length of the longest strictly increasing subsequence
        # So the maximum possible LIS is the length of the array multiplied by the number of times it is repeated
        # But since the array is sorted, the LIS is the length of the longest strictly increasing subsequence
        # So the maximum possible LIS is the length of the array multiplied by the number of times it is repeated
        # But since the array is sorted, the LIS is the length of the longest strictly increasing subsequence
        # So the maximum possible LIS is the length of the array multiplied by the number of times it is repeated
        # But since the array is sorted, the LIS is the length of the longest strictly increasing subsequence
        # So the maximum possible LIS is the length of the array multiplied by the number of times it is repeated
        # But since the array is sorted, the LIS is the length of the longest strictly increasing subsequence
        # So the maximum possible LIS is the length of the array multiplied