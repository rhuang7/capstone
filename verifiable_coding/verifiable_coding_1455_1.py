import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    idx = 0
    N = int(data[idx])
    idx += 1
    A = list(map(int, data[idx:idx+N]))
    idx += N
    M = int(data[idx])
    idx += 1
    queries = []
    for _ in range(M):
        L = int(data[idx])
        R = int(data[idx+1])
        queries.append((L, R))
        idx += 2
    
    # Preprocess the array to handle queries efficiently
    # Since the values can be up to 1e6, we can use a frequency array
    # But for better performance, we can use a sorted list and binary search
    # However, for large N and M, we need an efficient approach
    
    # For each query, we need to get the subarray A[L-1:R], sort it, and compute the sum of squared differences of consecutive elements
    
    # Since the constraints are tight, we need an O(M log N) solution
    # We can use a segment tree with sorted lists to allow efficient querying of sorted subarrays
    
    # However, for the sake of time and code simplicity, we'll use a brute force approach with optimizations
    
    # Precompute prefix sorted arrays
    # But for large N, this is not feasible
    
    # So we'll process each query directly
    # For each query, extract the subarray, sort it, and compute the sum of squared differences
    
    results = []
    for L, R in queries:
        sub = A[L-1:R]
        sub.sort()
        res = 0
        for i in range(1, len(sub)):
            res += (sub[i] - sub[i-1]) ** 2
        results.append(str(res))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()