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
            row = data[idx]
            matrix.append(list(row))
            idx += 1
        # Precompute prefix sums for a's
        prefix = [[0]*(N+1) for _ in range(N+1)]
        for i in range(1, N+1):
            for j in range(1, N+1):
                prefix[i][j] = prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1] + (1 if matrix[i-1][j-1] == 'a' else 0)
        # Process queries
        for _ in range(Q):
            X = int(data[idx])
            Y = int(data[idx+1])
            idx += 2
            # The maximum number of a's is the sum of a's in the path
            # The minimum number of non-a's is total characters - max a's
            total_chars = (X-1) + (Y-1) + 1
            max_a = prefix[X][Y]
            non_a = total_chars - max_a
            results.append(str(non_a))
    
    print('\n'.join(results))