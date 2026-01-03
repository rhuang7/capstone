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
        grid = []
        for _ in range(N):
            row = list(map(int, data[idx:idx+M]))
            grid.append(row)
            idx += M
        S = data[idx]
        idx += 1
        P = int(data[idx])
        Q = int(data[idx+1])
        idx += 2
        
        # Precompute the positions of the characters in S
        # For each cell (i,j), compute the position in S
        # The position in S is i + j
        # So for each cell (i,j), the character in S is S[i + j]
        # We need to check if the path from (0,0) to (N-1,M-1) matches S
        
        # We will use dynamic programming to find the minimum cost
        # dp[i][j] = minimum cost to reach (i,j) such that the path from (0,0) to (i,j) matches S[i+j]
        
        # Initialize dp table
        dp = [[float('inf')] * M for _ in range(N)]
        dp[0][0] = 0 if S[0] == '1' else 0  # Starting point is (0,0), which is S[0]
        
        for i in range(N):
            for j in range(M):
                if i == 0 and j == 0:
                    continue
                # Current position is (i,j), which corresponds to S[i+j]
                current_char = S[i + j]
                # Possible previous positions: (i-1,j) or (i,j-1)
                # Check both and take the minimum
                min_cost = float('inf')
                if i > 0:
                    # From (i-1,j)
                    prev_char = S[(i-1) + j]
                    # Cost to change grid[i-1][j] to match prev_char
                    cost_grid = 0
                    if grid[i-1][j] != int(prev_char):
                        cost_grid = P
                    # Cost to change current character in S
                    cost_S = 0
                    if current_char != prev_char:
                        cost_S = Q
                    min_cost = min(min_cost, dp[i-1][j] + cost_grid + cost_S)
                if j > 0:
                    # From (i,j-1)
                    prev_char = S[i + (j-1)]
                    # Cost to change grid[i][j-1] to match prev_char
                    cost_grid = 0
                    if grid[i][j-1] != int(prev_char):
                        cost_grid = P
                    # Cost to change current character in S
                    cost_S = 0
                    if current_char != prev_char:
                        cost_S = Q
                    min_cost = min(min_cost, dp[i][j-1] + cost_grid + cost_S)
                dp[i][j] = min_cost
        
        # The answer is the minimum cost to reach (N-1, M-1)
        results.append(str(dp[N-1][M-1]))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()