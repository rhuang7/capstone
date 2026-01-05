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
        # Case 1: K == 1
        if K == 1:
            max_sub = max(A)
            results.append(str(max_sub))
            continue
        
        # Case 2: K > 1
        # Compute maximum subarray sum for A
        max_sub = -float('inf')
        current_sum = 0
        for num in A:
            current_sum = max(num, current_sum + num)
            max_sub = max(max_sub, current_sum)
        
        # Compute total sum of A
        total_sum = sum(A)
        
        # If all elements are negative, the maximum subarray is the least negative
        if total_sum < 0:
            results.append(str(max_sub))
            continue
        
        # Compute maximum subarray that wraps around the array
        # This is the maximum subarray that starts in the first part and ends in the second part
        # So we need to find the maximum prefix sum and the maximum suffix sum
        max_prefix = 0
        current_sum = 0
        for num in A:
            current_sum = max(num, current_sum + num)
            max_prefix = max(max_prefix, current_sum)
        
        max_suffix = 0
        current_sum = 0
        for num in reversed(A):
            current_sum = max(num, current_sum + num)
            max_suffix = max(max_suffix, current_sum)
        
        # If K >= 2, we can take the max_sub that wraps around
        # So the maximum subarray could be max_sub, max_prefix + max_suffix, or total_sum
        max_wrap = max_prefix + max_suffix
        if K >= 2:
            max_sub = max(max_sub, max_wrap)
        
        # If K >= 2 and total_sum is positive, we can take the total_sum
        if K >= 2 and total_sum > 0:
            max_sub = max(max_sub, total_sum)
        
        results.append(str(max_sub))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()