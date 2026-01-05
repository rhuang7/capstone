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
        grid.append(row)
        idx += C
    
    # dp[i][j][k] = number of paths to (i,j) with k consecutive same direction steps
    # We'll use a 2D array for each row, with k up to d
    # Since we only need the current and previous row, we can optimize space
    # But for simplicity, we'll use a 3D array
    
    # Initialize dp
    dp = [[[0] * (d + 1) for _ in range(C)] for _ in range(R)]
    
    # Start position (0,0)
    if grid[0][0] == 1:
        dp[0][0][0] = 1  # 0 consecutive steps in any direction
    
    for i in range(R):
        for j in range(C):
            if grid[i][j] == 0:
                continue
            # Check if we can come from above (up to down)
            if i > 0:
                for k in range(d):
                    if dp[i-1][j][k] > 0:
                        # If we came from above, we can move down
                        # If we already have k consecutive down steps, we can add 1
                        if k < d:
                            dp[i][j][k+1] = (dp[i][j][k+1] + dp[i-1][j][k]) % MOD
                        else:
                            # Can't go further in the same direction
                            pass
            # Check if we can come from left (left to right)
            if j > 0:
                for k in range(d):
                    if dp[i][j-1][k] > 0:
                        # If we came from left, we can move right
                        # If we already have k consecutive right steps, we can add 1
                        if k < d:
                            dp[i][j][k+1] = (dp[i][j][k+1] + dp[i][j-1][k]) % MOD
                        else:
                            # Can't go further in the same direction
                            pass
    
    # Sum all possible ways to reach (R-1, C-1) with any number of consecutive steps
    result = sum(dp[R-1][C-1][k] for k in range(d+1)) % MOD
    print(result)

if __name__ == '__main__':
    solve()