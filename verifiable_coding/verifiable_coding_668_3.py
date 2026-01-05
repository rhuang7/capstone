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
        
        # Compute maximum subarray sum for B
        # Case 1: K == 1, B is A, so max subarray is just max subarray of A
        if K == 1:
            max_sub = max(A)
            max_subarray = max(A)
            results.append(str(max_subarray))
            continue
        
        # Case 2: K > 1
        # Compute max subarray that starts in one copy of A and ends in another
        # Also consider the max subarray that is entirely within one copy of A
        # Compute prefix sums
        prefix = [0] * (N + 1)
        for i in range(N):
            prefix[i+1] = prefix[i] + A[i]
        
        # Compute max subarray sum within one copy of A
        max_subarray = max(A)
        current_max = A[0]
        max_subarray = max(max_subarray, current_max)
        for i in range(1, N):
            current_max = max(A[i], current_max + A[i])
            max_subarray = max(max_subarray, current_max)
        
        # Compute max subarray that wraps around
        # It starts at some index i in the first copy and ends at some index j in the second copy
        # So sum is prefix[j+1] - prefix[i] + (prefix[N] - prefix[0]) * (K - 2)
        # We need to find the maximum (prefix[j+1] - prefix[i]) + (prefix[N] - prefix[0]) * (K - 2)
        # So we need to find the maximum (prefix[j+1] - prefix[i]) for j+1 > i
        # Which is the same as max(prefix[j+1]) - min(prefix[i]) for i < j+1
        max_wrap = -float('inf')
        max_prefix = -float('inf')
        min_prefix = float('inf')
        for i in range(N):
            max_prefix = max(max_prefix, prefix[i+1])
            min_prefix = min(min_prefix, prefix[i])
        max_wrap = max_prefix - min_prefix + (prefix[N] - prefix[0]) * (K - 2)
        
        # The overall maximum is the max of the two cases
        result = max(max_subarray, max_wrap)
        results.append(str(result))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()