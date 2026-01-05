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
        
        # Precompute the positions of the characters in S
        # For each cell (i,j), the position in S is i + j
        # So we can map each cell to its corresponding position in S
        # We'll create a 2D array of the same size as the matrix
        # where each cell contains the character from S at position i + j
        S_chars = []
        for i in range(N):
            row = []
            for j in range(M):
                pos = i + j
                row.append(S[pos])
            S_chars.append(row)
        
        # We need to find for each cell (i,j) whether it should be 0 or 1
        # based on the path from (0,0) to (N-1,M-1)
        # We'll use dynamic programming to find the minimum cost
        
        # dp[i][j] = minimum cost to reach (i,j) with the correct character
        # We'll use a 2D array of size N x M
        # We'll also track the required character for each cell
        # which is S[i + j]
        
        # Initialize the dp array
        dp = [[0] * M for _ in range(N)]
        # Initialize the first cell
        dp[0][0] = 0 if matrix[0][0] == int(S[0]) else P
        
        # Fill the first row
        for j in range(1, M):
            pos = 0 + j
            required = int(S[pos])
            if matrix[0][j] == required:
                dp[0][j] = dp[0][j-1]
            else:
                dp[0][j] = dp[0][j-1] + P
        
        # Fill the first column
        for i in range(1, N):
            pos = i + 0
            required = int(S[pos])
            if matrix[i][0] == required:
                dp[i][0] = dp[i-1][0]
            else:
                dp[i][0] = dp[i-1][0] + P
        
        # Fill the rest of the dp table
        for i in range(1, N):
            for j in range(1, M):
                pos = i + j
                required = int(S[pos])
                # Cost to change current cell
                cost_cell = 0
                if matrix[i][j] != required:
                    cost_cell = P
                # Cost to reach here from top or left
                cost_top = dp[i-1][j]
                cost_left = dp[i][j-1]
                # Choose the minimum cost
                dp[i][j] = min(cost_top, cost_left) + cost_cell
        
        # The answer is the cost to reach the bottom-right corner
        results.append(dp[N-1][M-1])
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()