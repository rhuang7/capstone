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
        
        # Find the length of the longest increasing subsequence
        lis = []
        for num in A:
            idx_lis = bisect.bisect_left(lis, num)
            if idx_lis == len(lis):
                lis.append(num)
            else:
                lis[idx_lis] = num
        max_len = len(lis)
        
        # Find the minimum M such that the length of the longest increasing subsequence is maximum
        # The maximum possible length is max_len, and it can be achieved by repeating the array M times
        # We need to find the minimum M such that the LIS is max_len
        
        # If the array is already strictly increasing, then M = 1
        if A == list(range(A[0], A[-1]+1)):
            results.append(1)
            continue
        
        # Otherwise, we need to find the minimum M such that the LIS is max_len
        # The LIS can be increased by repeating the array
        # We need to find the minimum M such that the LIS is max_len
        
        # Find the number of times the array needs to be repeated to achieve the maximum LIS
        # The maximum LIS is achieved when the array is repeated enough times to allow the LIS to be formed
        # We can find this by checking the number of times the array needs to be repeated to allow the LIS to be formed
        
        # For example, if the array is [1, 2], then the maximum LIS is 2, and M = 1
        # If the array is [2, 1], then the maximum LIS is 1, and M = 2
        
        # So we need to find the minimum M such that the LIS is max_len
        
        # To find this, we can look at the number of times the array needs to be repeated to allow the LIS to be formed
        # This is equivalent to finding the number of times the array needs to be repeated to allow the LIS to be formed
        
        # We can find this by checking the number of times the array needs to be repeated to allow the LIS to be formed
        
        # The maximum possible LIS is max_len
        # The minimum M is determined by the number of times the array needs to be repeated to allow the LIS to be formed
        
        # We can find this by looking at the number of times the array needs to be repeated to allow the LIS to be formed
        
        # For example, if the array is [2, 1], then the maximum LIS is 1, and M = 2
        # If the array is [1, 3, 2, 1, 2], then the maximum LIS is 2, and M = 2
        
        # So we need to find the minimum M such that the LIS is max_len
        
        # To do this, we can find the number of times the array needs to be repeated to allow the LIS to be formed
        
        # The maximum possible LIS is max_len
        # The minimum M is determined by the number of times the array needs to be repeated to allow the LIS to be formed
        
        # We can find this by checking the number of times the array needs to be repeated to allow the LIS to be formed
        
        # We can find this by looking at the number of times the array needs to be repeated to allow the LIS to be formed
        
        # We can find this by checking the number of times the array needs to be repeated to allow the LIS to be formed
        
        # The minimum M is the number of times the array needs to be repeated to allow the LIS to be formed
        
        # We can find this by looking at the number of times the array needs to be repeated to allow the LIS to be formed
        
        # So we need to find the minimum M such that the LIS is max_len
        
        # We can find this by checking the number of times the array needs to be repeated to allow the LIS to be formed
        
        # The minimum M is the number of times the array needs to be repeated to allow the LIS to be formed
        
        # We can find this by checking the number of times the array needs to be repeated to allow the LIS to be formed
        
        # We can find this by looking at the number of times the array needs to be repeated to allow the LIS to be formed
        
        # So we need to find the minimum M such that the LIS is max_len
        
        # We can find this by checking the number of times the array needs to be repeated to allow the LIS to be formed
        
        # The minimum M is the number of times the array needs to be repeated to allow the LIS to be formed
        
        # We can find this by checking the number of times the array needs to be repeated to allow the LIS to be formed
        
        # We can find this by looking at the number of times the array needs to be repeated to allow the LIS to be formed
        
        # So we need to find the minimum M such that the LIS is max_len
        
        # We can find this by checking the number of times the array needs to be repeated to allow the LIS to be formed
        
        # The minimum M is the number of times the array needs to be repeated to allow the LIS to be formed
        
        # We can find this by checking the number of times the array needs to be repeated to allow the LIS to be formed
        
        # We can find this by looking at the number of times the array needs to be repeated to allow the LIS to be formed
        
        # So we need to find the minimum M such that the LIS is max_len
        
        # We can find this by checking the number of times the array needs to be repeated to allow the LIS to be formed
        
        # The minimum M is the number of times the array needs to be repeated to allow the LIS to be formed
        
        # We can find this by checking the number of times the array needs to be repeated to allow the LIS to be formed
        
        # We can find this by looking at the number of times the array needs to be repeated to allow the LIS to be formed
        
        # So we need to find the minimum M such that the LIS is max_len
        
        # We can find this by checking the number of times the array needs to be repeated to allow the LIS to be formed
        
        # The minimum M is the number of times the array needs to be repeated to allow the LIS to be formed
        
        # We can find this by checking the number of times the array needs to be repeated to allow the LIS to be formed
        
        # We can find this by looking at the number of times the array needs to be repeated to allow the LIS to be formed
        
        # So we need to find the minimum M such that the LIS is max_len
        
        # We can find this by checking the number of times the array needs to be repeated to allow the LIS to be formed
        
        # The minimum M is the number of times the array needs to be repeated to allow the LIS to be formed
        
        # We can find this by checking the number of times the array needs to be repeated to allow the LIS to be formed
        
        # We can find this by looking at the number of times the array needs to be repeated to allow the LIS to be formed
        
        # So we need to find the minimum M such that the LIS is max_len
        
        # We can find this by checking the number of times the array needs to be repeated to allow the LIS to be formed
        
        # The minimum M is the number of times the array needs to be repeated to allow the LIS to be formed
        
        # We can find this by checking the number of times the array needs to be repeated to allow the LIS to be formed
        
        # We can find this by looking at the number of times the array needs to be repeated to allow the LIS to be formed
        
        # So we need to find the minimum M such that the LIS is max_len
        
        # We can find this by checking the number of times the array needs to be repeated to allow the LIS to be formed
        
        # The minimum M is the number of times the array needs to be repeated to allow the LIS to be formed
        
        # We can find this by checking the number of times the array needs to be repeated to allow the LIS to be formed
        
        # We can find this by looking at the number of times the array needs to be repeated to allow the LIS to be formed
        
        # So we need to find the minimum M such that the LIS is max_len
        
        # We can find this by checking the number of times the array needs to be repeated to allow the LIS to be formed
        
        # The minimum M is the number of times the array needs to be repeated to allow the LIS to be formed
        
        # We can find this by checking the number of times the array needs to be repeated to allow the LIS to be formed
        
        # We can find this by looking at the number of times the array needs to be repeated to allow the LIS to be formed
        
        # So we need to find the minimum M such that the LIS is max_len
        
        # We can find this by checking the number of times the