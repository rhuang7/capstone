import sys
MOD = 20011

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    idx = 0
    R = int(data[idx]); idx += 1
    C = int(data[idx]); idx += 1
    d = int(data[idx]); idx += 1
    
    grid = []
    for _ in range(R):
        row = list(map(int, data[idx:idx+C]))
        grid.append(row)
        idx += C
    
    # Directions: right (east), down (south)
    # We'll track the number of consecutive steps in each direction
    # dp[i][j][k] = number of paths to (i,j) with k consecutive steps in the last direction
    # Since R and C can be up to 300, and d up to 300, this is manageable
    # We'll use a 2D array for each direction, with size (R x C x (d+1))
    
    # Initialize dp arrays for right and down directions
    dp_right = [[[0]*(d+1) for _ in range(C)] for _ in range(R)]
    dp_down = [[[0]*(d+1) for _ in range(C)] for _ in range(R)]
    
    # Start at (0,0)
    if grid[0][0] == 1:
        dp_right[0][0][1] = 1  # 1 step right (but we're at the start)
        dp_down[0][0][1] = 1   # 1 step down (but we're at the start)
    
    for i in range(R):
        for j in range(C):
            if i == 0 and j == 0:
                continue
            if grid[i][j] == 0:
                continue
            
            # Check right direction
            if j > 0 and grid[i][j-1] == 1:
                # From (i, j-1) to (i, j)
                for k in range(1, d+1):
                    if k == 1:
                        dp_right[i][j][k] = (dp_right[i][j][k] + dp_right[i][j-1][k-1]) % MOD
                    else:
                        dp_right[i][j][k] = (dp_right[i][j][k] + dp_right[i][j-1][k-1]) % MOD
            # Check down direction
            if i > 0 and grid[i-1][j] == 1:
                # From (i-1, j) to (i, j)
                for k in range(1, d+1):
                    if k == 1:
                        dp_down[i][j][k] = (dp_down[i][j][k] + dp_down[i-1][k-1][j]) % MOD
                    else:
                        dp_down[i][j][k] = (dp_down[i][j][k] + dp_down[i-1][k-1][j]) % MOD
    
    # Total paths is the sum of all possible ways to reach (R-1, C-1)
    total = 0
    for k in range(1, d+1):
        total = (total + dp_right[R-1][C-1][k] + dp_down[R-1][C-1][k]) % MOD
    
    print(total)

if __name__ == '__main__':
    solve()