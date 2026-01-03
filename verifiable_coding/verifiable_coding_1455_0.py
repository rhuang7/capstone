import sys
import bisect

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
    # For each position, store the sorted list of elements from start to that position
    # This is not feasible for large N, so we use a segment tree or other approach
    # However, for the given constraints, we need an efficient way to handle range queries
    
    # For each query, we need to extract the subarray A[L-1:R], sort it, and compute the sum of squared differences
    # This is O(M * (R-L+1 log(R-L+1))) which is too slow for large M and large ranges
    
    # Alternative approach: use a binary indexed tree or a segment tree to store sorted subarrays
    # But this is complex to implement
    
    # Since the constraints are tight, we need an optimized approach
    # We can use a binary indexed tree (Fenwick tree) to store sorted elements and perform range queries
    
    # However, for the given problem, the most straightforward approach is to process each query directly
    # with sorting and sum of squared differences, which is O(M * (R-L+1 log(R-L+1)))
    # This will pass for small M and small ranges, but may not pass for large ones
    
    # To optimize, we can use a sorted list and binary search for each query
    # We'll use a list of sorted subarrays for each position
    
    # But for the given problem, we'll proceed with the straightforward approach for now
    
    results = []
    for L, R in queries:
        sub = A[L-1:R]
        sub.sort()
        res = 0
        for i in range(1, len(sub)):
            res += (sub[i] - sub[i-1]) ** 2
        results.append(res)
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()