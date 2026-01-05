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
        N = int(data[idx])
        Q = int(data[idx+1])
        idx += 2
        matrix = []
        for _ in range(N):
            row = data[idx:idx+N]
            matrix.append(row)
            idx += N
        queries = []
        for _ in range(Q):
            x = int(data[idx])
            y = int(data[idx+1])
            queries.append((x, y))
            idx += 2
        
        # Precompute prefix sums for a's
        prefix = [[0]*(N+1) for _ in range(N+1)]
        for i in range(1, N+1):
            for j in range(1, N+1):
                prefix[i][j] = prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1] + (1 if matrix[i-1][j-1] == 'a' else 0)
        
        # Process queries
        for x, y in queries:
            total_a = prefix[x][y] - prefix[0][y] - prefix[x][0] + prefix[0][0]
            non_a = (x + y - 1) - total_a
            results.append(str(non_a))
    
    sys.stdout.write('\n'.join(results) + '\n')

if __name__ == '__main__':
    solve()