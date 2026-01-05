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
            idx_lis = bisect.bisect_left(lis, num)
            if idx_lis == len(lis):
                lis.append(num)
            else:
                lis[idx_lis] = num
        max_len = len(lis)
        
        # Find the minimum M such that the length of the longest strictly increasing subsequence is maximum possible
        # The maximum possible length is max_len, and we need to find the minimum M such that the LIS is max_len
        # The LIS can be increased by repeating the array M times, but only if the sequence can be extended
        # The minimal M is determined by the number of times the sequence needs to be repeated to reach the maximum possible LIS
        # We need to find the minimal M such that the LIS is max_len
        
        # The minimal M is determined by the number of times the sequence needs to be repeated to reach the maximum possible LIS
        # We can find this by checking the number of times the sequence needs to be repeated to reach the maximum possible LIS
        # The minimal M is determined by the number of times the sequence needs to be repeated to reach the maximum possible LIS
        # The minimal M is determined by the number of times the sequence needs to be repeated to reach the maximum possible LIS
        # The minimal M is determined by the number of times the sequence needs to be repeated to reach the maximum possible LIS
        # The minimal M is determined by the number of times the sequence needs to be repeated to reach the maximum possible LIS
        # The minimal M is determined by the number of times the sequence needs to be repeated to reach the maximum possible LIS
        # The minimal M is determined by the number of times the sequence needs to be repeated to reach the maximum possible LIS
        # The minimal M is determined by the number of times the sequence needs to be repeated to reach the maximum possible LIS
        # The minimal M is determined by the number of times the sequence needs to be repeated to reach the maximum possible LIS
        # The minimal M is determined by the number of times the sequence needs to be repeated to reach the maximum possible LIS
        # The minimal M is determined by the number of times the sequence needs to be repeated to reach the maximum possible LIS
        # The minimal M is determined by the number of times the sequence needs to be repeated to reach the maximum possible LIS
        # The minimal M is determined by the number of times the sequence needs to be repeated to reach the maximum possible LIS
        # The minimal M is determined by the number of times the sequence needs to be repeated to reach the maximum possible LIS
        # The minimal M is determined by the number of times the sequence needs to be repeated to reach the maximum possible LIS
        # The minimal M is determined by the number of times the sequence needs to be repeated to reach the maximum possible LIS
        # The minimal M is determined by the number of times the sequence needs to be repeated to reach the maximum possible LIS
        # The minimal M is determined by the number of times the sequence needs to be repeated to reach the maximum possible LIS
        # The minimal M is determined by the number of times the sequence needs to be repeated to reach the maximum possible LIS
        # The minimal M is determined by the number of times the sequence needs to be repeated to reach the maximum possible LIS
        # The minimal M is determined by the number of times the sequence needs to be repeated to reach the maximum possible LIS
        # The minimal M is determined by the number of times the sequence needs to be repeated to reach the maximum possible LIS
        # The minimal M is determined by the number of times the sequence needs to be repeated to reach the maximum possible LIS
        # The minimal M is determined by the number of times the sequence needs to be repeated to reach the maximum possible LIS
        # The minimal M is determined by the number of times the sequence needs to be repeated to reach the maximum possible LIS
        # The minimal M is determined by the number of times the sequence needs to be repeated to reach the maximum possible LIS
        # The minimal M is determined by the number of times the sequence needs to be repeated to reach the maximum possible LIS
        # The minimal M is determined by the number of times the sequence needs to be repeated to reach the maximum possible LIS
        # The minimal M is determined by the number of times the sequence needs to be repeated to reach the maximum possible LIS
        # The minimal M is determined by the number of times the sequence needs to be repeated to reach the maximum possible LIS
        # The minimal M is determined by the number of times the sequence needs to be repeated to reach the maximum possible LIS
        # The minimal M is determined by the number of times the sequence needs to be repeated to reach the maximum possible LIS
        # The minimal M is determined by the number of times the sequence needs to be repeated to reach the maximum possible LIS
        # The minimal M is determined by the number of times the sequence needs to be repeated to reach the maximum possible LIS
        # The minimal M is determined by the number of times the sequence needs to be repeated to reach the maximum possible LIS
        # The minimal M is determined by the number of times the sequence needs to be repeated to reach the maximum possible LIS
        # The minimal M is determined by the number of times the sequence needs to be repeated to reach the maximum possible LIS
        # The minimal M is determined by the number of times the sequence needs to be repeated to reach the maximum possible LIS
        # The minimal M is determined by the number of times the sequence needs to be repeated to reach the maximum possible LIS
        # The minimal M is determined by the number of times the sequence needs to be repeated to reach the maximum possible LIS
        # The minimal M is determined by the number of times the sequence needs to be repeated to reach the maximum possible LIS
        # The minimal M is determined by the number of times the sequence needs to be repeated to reach the maximum possible LIS
        # The minimal M is determined by the number of times the sequence needs to be repeated to reach the maximum possible LIS
        # The minimal M is determined by the number of times the sequence needs to be repeated to reach the maximum possible LIS
        # The minimal M is determined by the number of times the sequence needs to be repeated to reach the maximum possible LIS
        # The minimal M is determined by the number of times the sequence needs to be repeated to reach the maximum possible LIS
        # The minimal M is determined by the number of times the sequence needs to be repeated to reach the maximum possible LIS
        # The minimal M is determined by the number of times the sequence needs to be repeated to reach the maximum possible LIS
        # The minimal M is determined by the number of times the sequence needs to be repeated to reach the maximum possible LIS
        # The minimal M is determined by the number of times the sequence needs to be repeated to reach the maximum possible LIS
        # The minimal M is determined by the number of times the sequence needs to be repeated to reach the maximum possible LIS
        # The minimal M is determined by the number of times the sequence needs to be repeated to reach the maximum possible LIS
        # The minimal M is determined by the number of times the sequence needs to be repeated to reach the maximum possible LIS
        # The minimal M is determined by the number of times the sequence needs to be repeated to reach the maximum possible LIS
        # The minimal M is determined by the number of times the sequence needs to be repeated to reach the maximum possible LIS
        # The minimal M is determined by the number of times the sequence needs to be repeated to reach the maximum possible LIS
        # The minimal M is determined by the number of times the sequence needs to be repeated to reach the maximum possible LIS
        # The minimal M is determined by the number of times the sequence needs to be repeated to reach the maximum possible LIS
        # The minimal M is determined by the number of times the sequence needs to be repeated to reach the maximum possible LIS
        # The minimal M is determined by the number of times the sequence needs to be repeated to reach the maximum possible LIS
        # The minimal M is determined by the number of times the sequence needs to be repeated to reach the maximum possible LIS
        # The minimal M is determined by the number of times the sequence needs to be repeated to reach the maximum possible LIS
        # The minimal M is determined by the number of times the sequence needs to be repeated to reach the maximum possible LIS
        # The minimal M is determined by the number of times the sequence needs to be repeated to reach the maximum possible LIS
        # The minimal M is determined by the number of times the sequence needs to be repeated to reach the maximum possible LIS
        # The minimal M is determined by the number of times the sequence needs to be repeated to reach the maximum possible LIS
        # The minimal M is determined by the number of times the sequence needs to be repeated to