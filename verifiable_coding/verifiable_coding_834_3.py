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
            matrix.append(row)
            idx += 1
        
        # Preprocess for each cell (i, j) the number of 'a's from (0,0) to (i,j)
        # Using dynamic programming
        dp = [[0]*N for _ in range(N)]
        dp[0][0] = 1 if matrix[0][0] == 'a' else 0
        for i in range(N):
            for j in range(N):
                if i == 0 and j == 0:
                    continue
                if i == 0:
                    dp[i][j] = dp[i][j-1] + (1 if matrix[i][j] == 'a' else 0)
                elif j == 0:
                    dp[i][j] = dp[i-1][j] + (1 if matrix[i][j] == 'a' else 0)
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + (1 if matrix[i][j] == 'a' else 0)
        
        # Preprocess for each cell (i, j) the number of non 'a's from (0,0) to (i,j)
        # Using dynamic programming
        non_a = [[0]*N for _ in range(N)]
        non_a[0][0] = 1 if matrix[0][0] != 'a' else 0
        for i in range(N):
            for j in range(N):
                if i == 0 and j == 0:
                    continue
                if i == 0:
                    non_a[i][j] = non_a[i][j-1] + (1 if matrix[i][j] != 'a' else 0)
                elif j == 0:
                    non_a[i][j] = non_a[i-1][j] + (1 if matrix[i][j] != 'a' else 0)
                else:
                    non_a[i][j] = min(non_a[i-1][j], non_a[i][j-1]) + (1 if matrix[i][j] != 'a' else 0)
        
        for _ in range(Q):
            X = int(data[idx]) - 1
            Y = int(data[idx+1]) - 1
            idx += 2
            
            # The number of non 'a's in the optimal path is the total number of non 'a's in the path
            # which is the total number of non 'a's in the rectangle from (0,0) to (X,Y)
            # minus the number of non 'a's in the paths that are not optimal
            # But since we precomputed the minimum number of non 'a's, we can use that
            results.append(str(non_a[X][Y]))
    
    print('\n'.join(results))