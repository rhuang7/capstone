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
    
    # dp[i][j][k] = number of paths to (i,j) with k consecutive same direction steps
    # We'll use a 2D array for each row, with a list of size d+1
    # Since we only need the previous row, we can optimize space
    prev = [ [0]*(d+1) for _ in range(C) ]
    curr = [ [0]*(d+1) for _ in range(C) ]
    
    # Start at (0,0)
    prev[0][0] = 1
    
    for i in range(R):
        for j in range(C):
            if grid[i][j] == 0:
                continue
            # If we are at the last row or last column, we can't move further
            if i == R-1 and j == C-1:
                continue
            # Try moving right
            if j < C-1 and grid[i][j+1] == 1:
                # If we came from the left, we can move right
                for k in range(d):
                    curr[j+1][k+1] = (curr[j+1][k+1] + prev[j][k]) % MOD
                # If we came from the right, we can move right only if we have not exceeded d
                # But since we are moving right, we can only do it if we came from the left
                # So we add the paths from the left
            # Try moving down
            if i < R-1 and grid[i+1][j] == 1:
                # If we came from above, we can move down
                for k in range(d):
                    curr[j][k+1] = (curr[j][k+1] + prev[j][k]) % MOD
                # If we came from below, we can move down only if we have not exceeded d
                # But since we are moving down, we can only do it if we came from above
                # So we add the paths from above
            # Update prev for next iteration
            prev, curr = curr, [[0]*(d+1) for _ in range(C)]
    
    # Sum all paths to the end
    result = 0
    for k in range(d+1):
        result = (result + prev[C-1][k]) % MOD
    
    print(result)

if __name__ == '__main__':
    solve()