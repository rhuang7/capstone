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
        queries = []
        for _ in range(Q):
            x = int(data[idx])
            y = int(data[idx+1])
            queries.append((x, y))
            idx += 2
        
        # Preprocess the matrix to compute the maximum number of 'a's for each (x, y)
        # We will use dynamic programming
        # dp[i][j] = maximum number of 'a's from (1,1) to (i,j)
        dp = [[0] * (N + 1) for _ in range(N + 1)]
        dp[1][1] = 1 if matrix[0][0] == 'a' else 0
        
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                if i == 1 and j == 1:
                    continue
                max_a = 0
                if i > 1:
                    max_a = max(max_a, dp[i-1][j])
                if j > 1:
                    max_a = max(max_a, dp[i][j-1])
                if matrix[i-1][j-1] == 'a':
                    dp[i][j] = max_a + 1
                else:
                    dp[i][j] = max_a
        
        # Process queries
        for x, y in queries:
            total_chars = (x + y - 1)
            max_a = dp[x][y]
            non_a = total_chars - max_a
            results.append(str(non_a))
    
    print('\n'.join(results))