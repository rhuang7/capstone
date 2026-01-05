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
        M = int(data[idx+1])
        idx += 2
        matrix = []
        for _ in range(N):
            row = list(map(int, data[idx:idx+M]))
            matrix.append(row)
            idx += M
        S = data[idx]
        idx += 1
        P = int(data[idx])
        Q = int(data[idx+1])
        idx += 2
        
        # Precompute the required string for each path
        # Since all paths have the same length, we can use dynamic programming
        # to find the minimum cost to make the matrix match the string along any path
        
        # Create a 2D DP table where dp[i][j] is the minimum cost to make the path
        # from (0,0) to (i,j) match the string S up to position (i+j)
        dp = [[float('inf')] * M for _ in range(N)]
        dp[0][0] = 0 if matrix[0][0] == S[0] else P
        
        for i in range(N):
            for j in range(M):
                if i == 0 and j == 0:
                    continue
                # Possible moves: from top or left
                cost = float('inf')
                if i > 0:
                    # From top
                    pos = i + j - 1
                    if pos < len(S):
                        if matrix[i][j] == S[pos]:
                            cost = dp[i-1][j]
                        else:
                            cost = dp[i-1][j] + P
                if j > 0:
                    # From left
                    pos = i + j - 1
                    if pos < len(S):
                        if matrix[i][j] == S[pos]:
                            cost = min(cost, dp[i][j-1])
                        else:
                            cost = min(cost, dp[i][j-1] + P)
                dp[i][j] = cost
        
        # The answer is the minimum cost to reach (N-1, M-1)
        results.append(str(dp[N-1][M-1]))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()