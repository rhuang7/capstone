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
        # Precompute for each cell (i,j) the maximum number of 'a's from (0,0) to (i,j)
        # and the minimum number of non-'a's
        dp_a = [[0]*N for _ in range(N)]
        dp_non_a = [[0]*N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                if i == 0 and j == 0:
                    dp_a[i][j] = 1 if matrix[i][j] == 'a' else 0
                    dp_non_a[i][j] = 1 if matrix[i][j] != 'a' else 0
                else:
                    dp_a[i][j] = 0
                    dp_non_a[i][j] = 0
                    if i > 0:
                        dp_a[i][j] = dp_a[i-1][j]
                        dp_non_a[i][j] = dp_non_a[i-1][j]
                    if j > 0:
                        if dp_a[i][j] < dp_a[i][j-1]:
                            dp_a[i][j] = dp_a[i][j-1]
                            dp_non_a[i][j] = dp_non_a[i][j-1]
                    if matrix[i][j] == 'a':
                        dp_a[i][j] += 1
                        dp_non_a[i][j] = dp_non_a[i][j] - 1
        # Process queries
        for _ in range(Q):
            X = int(data[idx]) - 1
            Y = int(data[idx+1]) - 1
            idx += 2
            # The maximum number of 'a's is dp_a[X][Y]
            # The minimum number of non-'a's is dp_non_a[X][Y]
            results.append(str(dp_non_a[X][Y]))
    print('\n'.join(results))