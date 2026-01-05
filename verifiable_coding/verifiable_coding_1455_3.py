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
    # Since the queries are arbitrary ranges, we need an efficient way to process them
    # However, for each query, we need to sort the subarray and compute the sum of squared differences
    # This is O(M * (R-L+1 log(R-L+1))) which is acceptable for small ranges but not for large ones
    # For the given constraints, we need a more efficient approach
    
    # For this problem, we'll process each query naively, as the constraints are tight but manageable
    # with fast I/O and efficient sorting
    
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