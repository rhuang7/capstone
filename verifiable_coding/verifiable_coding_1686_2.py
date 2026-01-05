import sys
MOD = 20011

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    idx = 0
    R = int(data[idx])
    idx += 1
    C = int(data[idx])
    idx += 1
    d = int(data[idx])
    idx += 1
    
    grid = []
    for _ in range(R):
        row = list(map(int, data[idx:idx+C]))
        idx += C
        grid.append(row)
    
    # dp[i][j][k] = number of paths to (i,j) with k consecutive steps in the same direction
    # k can be 0 to d
    # We use a 2D array for each row, and for each cell, we track the number of paths for each possible consecutive step count
    dp = [[[0]*(d+1) for _ in range(C)] for _ in range(R)]
    
    # Start position (0,0)
    dp[0][0][0] = 1  # 0 consecutive steps in the same direction
    
    for i in range(R):
        for j in range(C):
            if grid[i][j] == 0:
                continue
            # Check if we can come from the left (same direction: right)
            if j > 0:
                # If we came from the left, we can move right
                # We need to check if the previous step was in the same direction (right)
                # So for each possible consecutive count, we add to the current cell
                for k in range(d):
                    if dp[i][j-1][k] > 0:
                        # If we move right, the consecutive count increases by 1
                        if k + 1 <= d:
                            dp[i][j][k+1] = (dp[i][j][k+1] + dp[i][j-1][k]) % MOD
            # Check if we can come from above (same direction: down)
            if i > 0:
                # If we came from above, we can move down
                # We need to check if the previous step was in the same direction (down)
                for k in range(d):
                    if dp[i-1][j][k] > 0:
                        # If we move down, the consecutive count increases by 1
                        if k + 1 <= d:
                            dp[i][j][k+1] = (dp[i][j][k+1] + dp[i-1][j][k]) % MOD
    
    # Sum all possible consecutive step counts for the end cell
    result = sum(dp[R-1][C-1][k] for k in range(d+1)) % MOD
    print(result)

if __name__ == '__main__':
    solve()