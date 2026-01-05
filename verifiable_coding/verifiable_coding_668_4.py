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
        # Case 1: K == 1, B is same as A
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
        
        # Otherwise, the max subarray spans across multiple copies of A
        # So it's total * (K - 1) + max_subarray
        results.append(str(total * (K - 1) + max_subarray))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()