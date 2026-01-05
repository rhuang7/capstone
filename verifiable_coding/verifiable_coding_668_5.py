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
        # Compute max subarray sum in A
        max_sub = -float('inf')
        current = 0
        total = 0
        for num in A:
            current = max(num, current + num)
            max_sub = max(max_sub, current)
            total += num
        
        # If all elements are negative, the max subarray is the least negative
        if max_sub < 0:
            results.append(str(max_sub))
            continue
        
        # Compute the sum of the entire array
        total = sum(A)
        
        # Compute the maximum subarray that wraps around the array
        # This is the maximum prefix sum + maximum suffix sum
        max_prefix = max_suffix = 0
        current_prefix = 0
        current_suffix = 0
        for num in A:
            current_prefix = max(num, current_prefix + num)
            max_prefix = max(max_prefix, current_prefix)
        for num in reversed(A):
            current_suffix = max(num, current_suffix + num)
            max_suffix = max(max_suffix, current_suffix)
        
        # The maximum subarray could be:
        # 1. The max subarray in one copy of A
        # 2. The max prefix + max suffix (wrapping around)
        # 3. The total sum (if all elements are positive)
        max_total = max(max_sub, max_prefix + max_suffix, total)
        results.append(str(max_total))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()