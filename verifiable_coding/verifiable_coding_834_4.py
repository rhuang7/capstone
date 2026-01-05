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
        
        # Precompute the number of 'a's for each cell (i, j)
        # We'll use dynamic programming
        # dp[i][j] = max number of 'a's from (0,0) to (i,j)
        dp = [[0]*N for _ in range(N)]
        dp[0][0] = 1 if matrix[0][0] == 'a' else 0
        
        for i in range(N):
            for j in range(N):
                if i == 0 and j == 0:
                    continue
                max_val = 0
                if i > 0:
                    max_val = max(max_val, dp[i-1][j])
                if j > 0:
                    max_val = max(max_val, dp[i][j-1])
                if matrix[i][j] == 'a':
                    dp[i][j] = max_val + 1
                else:
                    dp[i][j] = max_val
        
        # Process queries
        for _ in range(Q):
            X = int(data[idx]) - 1
            Y = int(data[idx+1]) - 1
            idx += 2
            
            # The maximum number of 'a's is dp[X][Y]
            # The total length of the path is (X + Y + 1)
            # So the number of non 'a' characters is (X + Y + 1) - dp[X][Y]
            res = (X + Y + 1) - dp[X][Y]
            results.append(str(res))
    
    print('\n'.join(results))