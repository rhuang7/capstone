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
        # Using patience sorting approach
        tails = []
        for num in A:
            idx_b = bisect.bisect_left(tails, num)
            if idx_b == len(tails):
                tails.append(num)
            else:
                tails[idx_b] = num
        max_len = len(tails)
        
        # Find the minimum M such that the length of the longest strictly increasing subsequence is maximum possible
        # The maximum possible length is max_len
        # We need to find the smallest M such that the LIS of B is max_len
        # Since B is A repeated M times, the LIS of B is the same as the LIS of A repeated M times
        # The maximum possible LIS length is the length of the longest increasing subsequence in A
        # So we need to find the smallest M such that the LIS of B is max_len
        
        # If the LIS of A is already max_len, then M = 1
        if max_len == 1:
            results.append(1)
            continue
        
        # Otherwise, find the minimum M
        # The LIS of B is the same as the LIS of A repeated M times
        # So we need to find the minimum M such that the LIS of B is max_len
        # We can do this by finding the number of times the last element of the LIS appears in A
        # and then finding the minimum M such that the LIS of B is max_len
        
        # Find the LIS of A
        lis = []
        for num in A:
            idx_b = bisect.bisect_left(lis, num)
            if idx_b == len(lis):
                lis.append(num)
            else:
                lis[idx_b] = num
        max_len_lis = len(lis)
        
        # Find the number of times the last element of the LIS appears in A
        last = lis[-1]
        count = 0
        for num in A:
            if num == last:
                count += 1
        
        # The minimum M is the number of times the last element of the LIS appears in A
        results.append(count)
    
    for res in results:
        print(res)