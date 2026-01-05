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
    # We'll use two 2D arrays for current and next state
    # Since d can be up to 300, we need to track up to d steps in each direction
    # We'll use a 2D array for each direction and step count
    
    # Initialize dp arrays
    dp_right = [[0] * (d + 1) for _ in range(R)]
    dp_down = [[0] * (d + 1) for _ in range(R)]
    
    # Start at (0,0)
    if grid[0][0] == 1:
        dp_right[0][0] = 1  # 0 steps right, starting point
    
    for i in range(R):
        for j in range(C):
            # If current cell is blocked, skip
            if grid[i][j] == 0:
                continue
            
            # Update right direction
            if j > 0:
                # From (i, j-1) to (i, j) is a right move
                # If previous was right, increment step count
                # If previous was down, reset to 1
                if j - 1 >= 0:
                    if dp_right[i][j-1] > 0:
                        dp_right[i][j] = (dp_right[i][j] + dp_right[i][j-1]) % MOD
                    if dp_down[i][j-1] > 0:
                        dp_right[i][j] = (dp_right[i][j] + dp_down[i][j-1]) % MOD
                # If previous was right and step count < d, increment
                if j - 1 >= 0 and dp_right[i][j-1] > 0:
                    if dp_right[i][j-1] < d:
                        dp_right[i][j] = (dp_right[i][j] + dp_right[i][j-1]) % MOD
                # If previous was down and step count < d, increment
                if i - 1 >= 0 and dp_down[i][j-1] > 0:
                    if dp_down[i][j-1] < d:
                        dp_right[i][j] = (dp_right[i][j] + dp_down[i][j-1]) % MOD
            
            # Update down direction
            if i > 0:
                # From (i-1, j) to (i, j) is a down move
                # If previous was down, increment step count
                # If previous was right, reset to 1
                if i - 1 >= 0:
                    if dp_down[i-1][j] > 0:
                        dp_down[i][j] = (dp_down[i][j] + dp_down[i-1][j]) % MOD
                    if dp_right[i-1][j] > 0:
                        dp_down[i][j] = (dp_down[i][j] + dp_right[i-1][j]) % MOD
                # If previous was down and step count < d, increment
                if i - 1 >= 0 and dp_down[i-1][j] > 0:
                    if dp_down[i-1][j] < d:
                        dp_down[i][j] = (dp_down[i][j] + dp_down[i-1][j]) % MOD
                # If previous was right and step count < d, increment
                if j - 1 >= 0 and dp_right[i-1][j] > 0:
                    if dp_right[i-1][j] < d:
                        dp_down[i][j] = (dp_down[i][j] + dp_right[i-1][j]) % MOD
    
    # The answer is the sum of paths to (R-1, C-1) with any step count
    result = (dp_right[R-1][C-1] + dp_down[R-1][C-1]) % MOD
    print(result)

if __name__ == '__main__':
    solve()