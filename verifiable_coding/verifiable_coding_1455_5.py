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
    # Since the queries are arbitrary ranges and we need sorted subarrays,
    # we cannot preprocess in a way that allows O(1) or O(logN) per query.
    # Thus, we process each query directly.
    
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