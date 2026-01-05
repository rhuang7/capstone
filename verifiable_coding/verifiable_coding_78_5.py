import sys
import math

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    idx = 0
    q = int(data[idx])
    idx += 1
    
    results = []
    
    for _ in range(q):
        n = int(data[idx])
        m = int(data[idx+1])
        idx += 2
        
        grid = []
        for i in range(n):
            row = data[idx]
            grid.append(row)
            idx += 1
        
        # Precompute for each row: number of black cells
        row_black = [row.count('*') for row in grid]
        # Precompute for each column: number of black cells
        col_black = [0] * m
        for j in range(m):
            cnt = 0
            for i in range(n):
                if grid[i][j] == '*':
                    cnt += 1
            col_black[j] = cnt
        
        min_paint = float('inf')
        
        # Try each cell as the center of a cross
        for i in range(n):
            for j in range(m):
                # Check if this cell can be the center of a cross
                # All cells in row i must be black, all cells in column j must be black
                # So, we need to paint the white cells in row i and column j
                # But we have to subtract the cell (i,j) once because it's counted twice
                row_white = n - row_black[i]
                col_white = m - col_black[j]
                total = row_white + col_white - 1  # subtract 1 because (i,j) is counted twice
                if total < min_paint:
                    min_paint = total
        
        results.append(str(min_paint))
    
    print('\n'.join(results))