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
    # directions: 0 = right, 1 = down
    # We'll use a 3D array: dp[i][j][0] = paths with last move right, dp[i][j][1] = paths with last move down
    # Also, we need to track the number of consecutive steps in the same direction
    # So we'll use a 3D array: dp[i][j][k] = number of paths to (i,j) with k consecutive steps in the same direction
    
    # Since d can be up to 300, and R and C up to 300, the total size is 300*300*300 = 27,000,000 which is manageable
    dp = [[[0] * (d + 1) for _ in range(C)] for _ in range(R)]
    
    # Starting point (0,0)
    if grid[0][0] == 1:
        dp[0][0][0] = 1  # 0 consecutive steps in the same direction (just starting)
    
    for i in range(R):
        for j in range(C):
            if grid[i][j] == 0:
                continue
            # Check right direction
            if j > 0:
                # From (i, j-1) to (i, j) is a right move
                # We can add to dp[i][j][1] the number of paths that ended with 0 consecutive right steps
                # Or if the previous step was a right move, we can add to dp[i][j][k+1]
                # So for each k in 0..d-1, we can add dp[i][j-1][k] to dp[i][j][k+1]
                for k in range(d):
                    dp[i][j][k+1] = (dp[i][j][k+1] + dp[i][j-1][k]) % MOD
            # Check down direction
            if i > 0:
                # From (i-1, j) to (i, j) is a down move
                # We can add to dp[i][j][1] the number of paths that ended with 0 consecutive down steps
                # Or if the previous step was a down move, we can add to dp[i][j][k+1]
                # So for each k in 0..d-1, we can add dp[i-1][j][k] to dp[i][j][k+1]
                for k in range(d):
                    dp[i][j][k+1] = (dp[i][j][k+1] + dp[i-1][j][k]) % MOD
    
    # Sum all possible ways to reach (R-1, C-1)
    result = sum(dp[R-1][C-1][k] for k in range(d + 1)) % MOD
    print(result)

if __name__ == '__main__':
    solve()