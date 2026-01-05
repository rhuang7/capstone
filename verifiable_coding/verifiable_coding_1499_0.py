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
        
        # Precompute the positions of each character in the string S
        # For each cell (i,j), compute the path from (0,0) to (i,j) and the position in S
        # We'll use dynamic programming to find the minimum cost for each cell
        # The path length from (0,0) to (i,j) is i + j, so the position in S is i + j
        
        # Initialize a DP table with size N x M
        dp = [[float('inf')] * M for _ in range(N)]
        dp[0][0] = 0  # Starting point
        
        # Fill the DP table
        for i in range(N):
            for j in range(M):
                if i == 0 and j == 0:
                    continue
                # The position in S is i + j
                pos = i + j
                if pos >= len(S):
                    # Invalid position, skip
                    continue
                # Current character in S
                target_char = S[pos]
                
                # Cost to change matrix[i][j] to target_char
                cost_matrix = 0
                if matrix[i][j] != target_char:
                    cost_matrix = P
                
                # Cost to change S[pos] to target_char
                cost_string = 0
                if target_char != S[pos]:
                    cost_string = Q
                
                # Choose the minimum cost
                min_cost = min(cost_matrix, cost_string)
                
                # Update dp[i][j]
                if i > 0:
                    dp[i][j] = min(dp[i][j], dp[i-1][j] + min_cost)
                if j > 0:
                    dp[i][j] = min(dp[i][j], dp[i][j-1] + min_cost)
        
        # The answer is the cost to reach the bottom-right corner
        results.append(str(dp[N-1][M-1]))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()