import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    idx = 0
    T = int(data[idx])
    idx += 1
    
    results = []
    
    for _ in range(T):
        N, K = int(data[idx]), int(data[idx+1])
        idx += 2
        A = list(map(int, data[idx:idx+N]))
        idx += N
        
        # Compute max subarray sum for B
        # Case 1: K == 1
        if K == 1:
            max_sum = max(A)
            results.append(str(max_sum))
            continue
        
        # Case 2: K >= 2
        # Compute max subarray sum for A
        max_subarray = 0
        current_sum = 0
        for num in A:
            current_sum = max(num, current_sum + num)
            max_subarray = max(max_subarray, current_sum)
        
        # Compute prefix sum of A
        prefix_sum = [0] * (N + 1)
        for i in range(N):
            prefix_sum[i+1] = prefix_sum[i] + A[i]
        
        # Compute suffix sum of A
        suffix_sum = [0] * (N + 1)
        for i in range(N-1, -1, -1):
            suffix_sum[i] = suffix_sum[i+1] + A[i]
        
        # If all elements are negative, the max subarray is the least negative
        if max_subarray < 0:
            results.append(str(max_subarray))
            continue
        
        # If K >= 2, check for the case where the max subarray wraps around
        # The max subarray could be the sum of the entire array (if all elements are positive)
        # Or it could be the sum of a prefix and a suffix
        total_sum = prefix_sum[N]
        if total_sum > 0:
            max_sum = total_sum * K
        else:
            max_sum = max_subarray
        
        # Check for the case where the max subarray wraps around
        # The max subarray could be the sum of a prefix and a suffix
        # We need to find the minimum prefix sum and minimum suffix sum
        min_prefix = prefix_sum[0]
        for i in range(1, N+1):
            min_prefix = min(min_prefix, prefix_sum[i])
        
        min_suffix = suffix_sum[N]
        for i in range(N-1, -1, -1):
            min_suffix = min(min_suffix, suffix_sum[i])
        
        # The max subarray that wraps around is (total_sum - min_prefix - min_suffix) + (K-2)*total_sum
        # But if total_sum is negative, this is not useful
        if total_sum > 0:
            wrap_sum = (total_sum - min_prefix - min_suffix) + (K-2)*total_sum
            max_sum = max(max_sum, wrap_sum)
        
        results.append(str(max_sum))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()