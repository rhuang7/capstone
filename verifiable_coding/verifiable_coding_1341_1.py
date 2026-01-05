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
        N = int(data[idx])
        idx += 1
        A = list(map(int, data[idx:idx+N]))
        idx += N
        
        # Compute the number of valid contiguous subsequences
        # that when removed leave a strictly increasing sequence
        # We'll use a greedy approach to find increasing runs
        # and calculate the number of valid subarrays
        
        # Find the length of the longest increasing subarray
        # and use that to compute the number of valid subarrays
        # to remove
        
        # Initialize variables
        inc = 1
        max_inc = 1
        for i in range(1, N):
            if A[i] > A[i-1]:
                inc += 1
                max_inc = max(max_inc, inc)
            else:
                inc = 1
        
        # The number of valid subarrays to remove is
        # (max_inc * (max_inc + 1)) // 2 - max_inc
        # because we subtract the case where the entire increasing subarray is removed
        # which would leave an empty sequence
        # However, this approach is incorrect as it only considers the longest increasing subarray
        
        # Correct approach:
        # For each position, find the length of the longest increasing subarray ending at that position
        # and accumulate the number of valid subarrays
        
        # Initialize variables
        res = 0
        inc = 1
        for i in range(1, N):
            if A[i] > A[i-1]:
                inc += 1
            else:
                inc = 1
            res += inc
        
        # Subtract the cases where the entire array is removed (which is 1 case)
        # and the cases where the remaining sequence is empty (which is 1 case)
        # But the problem says the resulting sequence must be non-empty
        # So we subtract 1 for the case where the entire array is removed
        
        # Also, we need to ensure that the remaining sequence is non-empty
        # So we subtract 1 for the case where the entire array is removed
        
        # The correct formula is:
        # res = sum of lengths of increasing runs
        # minus 1 (for the case where the entire array is removed)
        # but we also need to ensure that the remaining sequence is non-empty
        
        # So the final answer is res - 1
        
        results.append(str(res - 1))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()