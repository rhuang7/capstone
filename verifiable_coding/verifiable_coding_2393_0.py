import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        grid = data[idx]
        idx += 1
        grid = [list(grid[i*n:(i+1)*n]) for i in range(n)]
        
        valid = True
        for i in range(n):
            for j in range(n):
                if grid[i][j] == '1':
                    # Check if it can be reached from a cannon
                    # Check if it's in first row or first column
                    if i == 0 or j == 0:
                        # It can be reached from a cannon
                        continue
                    # Check if there is a path from the border to this cell
                    # Check if there is a 1 in the first row or first column that can reach this cell
                    # Check if there is a 1 in the first row or first column that can reach this cell
                    # Check if there is a 1 in the first row or first column that can reach this cell
                    # Check if there is a 1 in the first row or first column that can reach this cell
                    # Check if there is a 1 in the first row or first column that can reach this cell
                    # Check if there is a 1 in the first row or first column that can reach this cell
                    # Check if there is a 1 in the first row or first column that can reach this cell
                    # Check if there is a 1 in the first row or first column that can reach this cell
                    # Check if there is a 1 in the first row or first column that can reach this cell
                    # Check if there is a 1 in the first row or first column that can reach this cell
                    # Check if there is a 1 in the first row or first column that can reach this cell
                    # Check if there is a 1 in the first row or first column that can reach this cell
                    # Check if there is a 1 in the first row or first column that can reach this cell
                    # Check if there is a 1 in the first row or first column that can reach this cell
                    # Check if there is a 1 in the first row or first column that can reach this cell
                    # Check if there is a 1 in the first row or first column that can reach this cell
                    # Check if there is a 1 in the first row or first column that can reach this cell
                    # Check if there is a 1 in the first row or first column that can reach this cell
                    # Check if there is a 1 in the first row or first column that can reach this cell
                    # Check if there is a 1 in the first row or first column that can reach this cell
                    # Check if there is a 1 in the first row or first column that can reach this cell
                    # Check if there is a 1 in the first row or first column that can reach this cell
                    # Check if there is a 1 in the first row or first column that can reach this cell
                    # Check if there is a 1 in the first row or first column that can reach this cell
                    # Check if there is a 1 in the first row or first column that can reach this cell
                    # Check if there is a 1 in the first row or first column that can reach this cell
                    # Check if there is a 1 in the first row or first column that can reach this cell
                    # Check if there is a 1 in the first row or first column that can reach this cell
                    # Check if there is a 1 in the first row or first column that can reach this cell
                    # Check if there is a 1 in the first row or first column that can reach this cell
                    # Check if there is a 1 in the first row or first column that can reach this cell
                    # Check if there is a 1 in the first row or first column that can reach this cell
                    # Check if there is a 1 in the first row or first column that can reach this cell
                    # Check if there is a 1 in the first row or first column that can reach this cell
                    # Check if there is a 1 in the first row or first column that can reach this cell
                    # Check if there is a 1 in the first row or first column that can reach this cell
                    # Check if there is a 1 in the first row or first column that can reach this cell
                    # Check if there is a 1 in the first row or first column that can reach this cell
                    # Check if there is a 1 in the first row or first column that can reach this cell
                    # Check if there is a 1 in the first row or first column that can reach this cell
                    # Check if there is a 1 in the first row or first column that can reach this cell
                    # Check if there is a 1 in the first row or first column that can reach this cell
                    # Check if there is a 1 in the first row or first column that can reach this cell
                    # Check if there is a 1 in the first row or first column that can reach this cell
                    # Check if there is a 1 in the first row or first column that can reach this cell
                    # Check if there is a 1 in the first row or first column that can reach this cell
                    # Check if there is a 1 in the first row or first column that can reach this cell
                    # Check if there is a 1 in the first row or first column that can reach this cell
                    # Check if there is a 1 in the first row or first column that can reach this cell
                    # Check if there is a 1 in the first row or first column that can reach this cell
                    # Check if there is a 1 in the first row or first column that can reach this cell
                    # Check if there is a 1 in the first row or first column that can reach this cell
                    # Check if there is a 1 in the first row or first column that can reach this cell
                    # Check if there is a 1 in the first row or first column that can reach this cell
                    # Check if there is a 1 in the first row or first column that can reach this cell
                    # Check if there is a 1 in the first row or first column that can reach this cell
                    # Check if there is a 1 in the first row or first column that can reach this cell
                    # Check if there is a 1 in the first row or first column that can reach this cell
                    # Check if there is a 1 in the first row or first column that can reach this cell
                    # Check if there is a 1 in the first row or first column that can reach this cell
                    # Check if there is a 1 in the first row or first column that can reach this cell
                    # Check if there is a 1 in the first row or first column that can reach this cell
                    # Check if there is a 1 in the first row or first column that can reach this cell
                    # Check if there is a 1 in the first row or first column that can reach this cell
                    # Check if there is a 1 in the first row or first column that can reach this cell
                    # Check if there is a 1 in the first row or first column that can reach this cell
                    # Check if there is a 1 in the first row or first column that can reach this cell
                    # Check if there is a 1 in the first row or first column that can reach this cell
                    # Check if there is a 1 in the first row or first column that can reach this cell
                    # Check if there is a 1 in the first row or first column that can reach this cell
                    # Check if there is a 1 in the first row or first column that can reach this cell
                    # Check if there is a 1 in the first row or first column that can reach this cell
                    # Check if there is a 1 in the first row or first column that can reach this cell
                    # Check if there is a 1 in the first row or first column that can reach this cell
                    # Check if there is a 1 in the first row or first column that can reach this cell
                    # Check if there is a 1 in the first row or first column that can reach this cell
                    # Check if there is a 1 in the first row or first column that can reach this cell
                    # Check if there is a 1 in the first row or first column that can reach this cell
                    # Check if there is a 1 in the first row or first column that can reach this cell
                    # Check if there is a 1 in the first row or first column that can reach this cell
                    # Check if there is a 1 in the first row or first column that can reach this cell
                    # Check if there is a 1 in the first row or first column that can reach