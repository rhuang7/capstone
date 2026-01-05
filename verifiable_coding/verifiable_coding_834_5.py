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
        
        # Precompute for each cell (i,j) the maximum number of 'a's from (1,1) to (i,j)
        # Using dynamic programming
        dp = [[0]*N for _ in range(N)]
        dp[0][0] = 1 if matrix[0][0] == 'a' else 0
        for i in range(N):
            for j in range(N):
                if i == 0 and j == 0:
                    continue
                max_a = 0
                if i > 0:
                    max_a = max(max_a, dp[i-1][j])
                if j > 0:
                    max_a = max(max_a, dp[i][j-1])
                if matrix[i][j] == 'a':
                    dp[i][j] = max_a + 1
                else:
                    dp[i][j] = max_a
        
        # Precompute for each cell (i,j) the total number of characters from (1,1) to (i,j)
        # Using dynamic programming
        total = [[0]*N for _ in range(N)]
        total[0][0] = 1
        for i in range(N):
            for j in range(N):
                if i == 0 and j == 0:
                    continue
                total[i][j] = total[i-1][j] if i > 0 else total[i][j-1]
                if j > 0:
                    total[i][j] += total[i][j-1]
                if i > 0:
                    total[i][j] += total[i-1][j]
        
        # Process queries
        for x, y in queries:
            # Convert to 0-based index
            x -= 1
            y -= 1
            # The number of characters in the path is (x + y + 1)
            # The maximum number of 'a's is dp[x][y]
            # The number of non 'a' characters is (x + y + 1) - dp[x][y]
            results.append(str(x + y + 1 - dp[x][y]))
    
    sys.stdout.write('\n'.join(results) + '\n')

if __name__ == '__main__':
    solve()