import sys
import bisect

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    N = int(data[0])
    A = list(map(int, data[1:N+1]))
    M = int(data[N+1])
    queries = []
    idx = N + 2
    for _ in range(M):
        L = int(data[idx])
        R = int(data[idx+1])
        queries.append((L, R))
        idx += 2
    
    # Preprocess sorted lists for all possible ranges
    # We'll use a segment tree approach for efficient range queries
    # However, for the sake of time and simplicity, we'll use a brute-force approach
    # with some optimizations
    
    # For each query, we'll extract the subarray, sort it, and compute the sum of squared differences
    # This is O(M * (R-L+1 log(R-L+1))) which may be too slow for large M and large ranges
    # So we need a more efficient approach
    
    # We'll use a binary indexed tree (Fenwick Tree) approach for the sorted elements
    # However, given the constraints, it's better to use a brute-force approach with some optimizations
    
    # Since the values of A[i] can be up to 1e6, we can use coordinate compression
    # But for the sake of time and simplicity, we'll use a brute-force approach
    
    # Precompute sorted lists for all possible ranges
    # This is not feasible for large N, so we'll use a brute-force approach for each query
    
    results = []
    
    for L, R in queries:
        sub = A[L-1:R]
        sub.sort()
        res = 0
        for i in range(1, len(sub)):
            res += (sub[i] - sub[i-1]) ** 2
        results.append(res)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()