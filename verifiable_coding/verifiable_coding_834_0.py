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
        # Precompute the number of 'a's from (1,1) to (i,j)
        dp = [[0]*N for _ in range(N)]
        dp[0][0] = 1 if matrix[0][0] == 'a' else 0
        for i in range(N):
            for j in range(N):
                if i == 0 and j == 0:
                    continue
                current = 1 if matrix[i][j] == 'a' else 0
                if i > 0:
                    dp[i][j] = max(dp[i][j], dp[i-1][j] + current)
                if j > 0:
                    dp[i][j] = max(dp[i][j], dp[i][j-1] + current)
        # Process queries
        for _ in range(Q):
            X = int(data[idx]) - 1
            Y = int(data[idx+1]) - 1
            idx += 2
            # The path from (0,0) to (X,Y) has (X+Y+1) characters
            # The maximum number of 'a's is dp[X][Y]
            # The number of non 'a' characters is (X+Y+1) - dp[X][Y]
            results.append(str((X + Y + 1) - dp[X][Y]))
    print('\n'.join(results))