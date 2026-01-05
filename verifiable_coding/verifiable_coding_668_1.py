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
            max_sum = max(A)
            results.append(str(max_sum))
            continue
        
        # Case 2: K > 1
        # Compute max subarray sum in A
        max_subarray = 0
        current = 0
        for num in A:
            current = max(num, current + num)
            max_subarray = max(max_subarray, current)
        
        # Compute total sum of A
        total = sum(A)
        
        # If all elements are negative, the max subarray is the least negative
        if total < 0:
            results.append(str(max_subarray))
            continue
        
        # If the max subarray is within one copy of A
        if max_subarray > 0:
            results.append(str(max_subarray))
            continue
        
        # If the max subarray spans across multiple copies of A
        # The max subarray is total * K if all elements are positive
        # Otherwise, it's max_subarray + total * (K - 2)
        # But we need to check if the max subarray can be extended across multiple copies
        # So we need to check the max prefix sum and max suffix sum
        prefix = 0
        max_prefix = -float('inf')
        for num in A:
            prefix += num
            max_prefix = max(max_prefix, prefix)
        
        suffix = 0
        max_suffix = -float('inf')
        for num in reversed(A):
            suffix += num
            max_suffix = max(max_suffix, suffix)
        
        # If the max subarray can be extended across multiple copies
        if max_subarray + max_prefix + max_suffix > 0:
            results.append(str(max_subarray + max_prefix + max_suffix))
        else:
            results.append(str(max_subarray))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()