import sys
import math

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
        
        # Function to generate all possible OR values
        def generate_or_values(arr):
            or_set = set()
            n = len(arr)
            for mask in range(1 << n):
                or_val = 0
                for i in range(n):
                    if mask & (1 << i):
                        or_val |= arr[i]
                or_set.add(or_val)
            return or_set
        
        # Function to find the minimum number of elements to insert
        def min_insertions(arr, K):
            current = set(arr)
            while True:
                next_set = generate_or_values(current)
                if len(next_set) == (1 << K):
                    return 0
                if len(next_set) == len(current):
                    return len(current) - len(next_set)
                current = next_set
        
        res = min_insertions(A, K)
        results.append(str(res))
    
    print('\n'.join(results))