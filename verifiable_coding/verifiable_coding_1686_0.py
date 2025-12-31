import sys
MOD = 20011

def solve():
    import sys
    sys.setrecursionlimit(1 << 25)
    data = sys.stdin.buffer.read().split()
    idx = 0
    R = int(data[idx]); idx +=1
    C = int(data[idx]); idx +=1
    d = int(data[idx]); idx +=1

    grid = []
    for _ in range(R):
        row = list(map(int, data[idx:idx+C]))
        idx += C
        grid.append(row)

    # dp[i][j][k] = number of paths to (i,j) with k consecutive steps in the same direction
    # k can be 0 to d
    # We'll use a 2D array for each row, and track for each cell the number of paths with different k values
    # Since we can only move right or down, we can process row by row

    # Initialize dp
    dp = [[ [0]*(d+1) for _ in range(C)] for _ in range(R)]
    # Starting point (0,0)
    if grid[0][0] == 1:
        dp[0][0][0] = 1  # 0 consecutive steps in same direction

    for i in range(R):
        for j in range(C):
            if grid[i][j] == 0:
                continue
            # If it's the starting point, skip
            if i == 0 and j == 0:
                continue
            # Check from above (i-1,j)
            if i > 0:
                for k in range(d):
                    if dp[i-1][j][k] > 0:
                        # If we came from above, we can move down
                        # If we have k consecutive steps in the same direction (down), then we can add 1 step
                        if k < d:
                            dp[i][j][k+1] = (dp[i][j][k+1] + dp[i-1][j][k]) % MOD
                        else:
                            # If k == d, we can't add another step
                            pass
                        # If we have k consecutive steps in the same direction (down), then we can turn right
                        # So we reset the count to 1 (since we just turned)
                        dp[i][j][0] = (dp[i][j][0] + dp[i-1][j][k]) % MOD
            # Check from left (i,j-1)
            if j > 0:
                for k in range(d):
                    if dp[i][j-1][k] > 0:
                        # If we came from left, we can move right
                        # If we have k consecutive steps in the same direction (right), then we can add 1 step
                        if k < d:
                            dp[i][j][k+1] = (dp[i][j][k+1] + dp[i][j-1][k]) % MOD
                        else:
                            # If k == d, we can't add another step
                            pass
                        # If we have k consecutive steps in the same direction (right), then we can turn down
                        # So we reset the count to 1 (since we just turned)
                        dp[i][j][0] = (dp[i][j][0] + dp[i][j-1][k]) % MOD

    # Sum all possible k values for the end point
    result = sum(dp[R-1][C-1][k] for k in range(d+1)) % MOD
    print(result)

if __name__ == '__main__':
    solve()