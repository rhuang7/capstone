import sys
MOD = 20011

def solve():
    import sys
    sys.setrecursionlimit(1 << 25)
    data = sys.stdin.buffer.read().split()
    idx = 0
    R = int(data[idx]); idx += 1
    C = int(data[idx]); idx += 1
    d = int(data[idx]); idx += 1
    
    grid = []
    for _ in range(R):
        row = list(map(int, data[idx:idx+C]))
        grid.append(row)
        idx += C
    
    # dp[i][j][k] = number of paths to (i,j) with k consecutive steps in the same direction
    # directions: 0 = right, 1 = down
    # We'll use two separate dp tables for each direction
    dp_right = [[ [0]*(d+1) for _ in range(C)] for _ in range(R)]
    dp_down = [[ [0]*(d+1) for _ in range(C)] for _ in range(R)]
    
    # Initialize starting point
    if grid[0][0] == 1:
        dp_right[0][0][1] = 1  # 1 step right (but we're at start)
        dp_down[0][0][1] = 1   # 1 step down (but we're at start)
    
    for i in range(R):
        for j in range(C):
            if grid[i][j] == 0:
                continue
            # Right direction
            if j > 0:
                # From (i, j-1) to (i, j) is right
                for k in range(1, d+1):
                    if dp_right[i][j-1][k] > 0:
                        dp_right[i][j][k+1] = (dp_right[i][j][k+1] + dp_right[i][j-1][k]) % MOD
                        if k+1 > d:
                            dp_right[i][j][1] = (dp_right[i][j][1] + dp_right[i][j-1][k]) % MOD
            # Down direction
            if i > 0:
                # From (i-1, j) to (i, j) is down
                for k in range(1, d+1):
                    if dp_down[i-1][j][k] > 0:
                        dp_down[i][j][k+1] = (dp_down[i][j][k+1] + dp_down[i-1][j][k]) % MOD
                        if k+1 > d:
                            dp_down[i][j][1] = (dp_down[i][j][1] + dp_down[i-1][j][k]) % MOD
    
    # Sum all possible ways to reach (R-1, C-1)
    total = (dp_right[R-1][C-1][1] + dp_down[R-1][C-1][1]) % MOD
    print(total)

if __name__ == '__main__':
    solve()