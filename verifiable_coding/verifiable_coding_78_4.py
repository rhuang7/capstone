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
        for _ in range(n):
            row = data[idx]
            grid.append(row)
            idx += 1
        
        # Precompute for each row the number of white cells
        row_white = [row.count('.') for row in grid]
        
        # Precompute for each column the number of white cells
        col_white = [0] * m
        for j in range(m):
            cnt = 0
            for i in range(n):
                if grid[i][j] == '.':
                    cnt += 1
            col_white[j] = cnt
        
        min_paint = float('inf')
        
        # Try each row as the horizontal part of the cross
        for i in range(n):
            # The row is already all black, so we need to make the column all black
            # The number of white cells in the column is col_white[j]
            # So the cost is col_white[j]
            # We need to find the minimum col_white[j] for this row
            min_col = min(col_white)
            min_paint = min(min_paint, min_col)
        
        # Try each column as the vertical part of the cross
        for j in range(m):
            # The column is already all black, so we need to make the row all black
            # The number of white cells in the row is row_white[i]
            # So the cost is row_white[i]
            # We need to find the minimum row_white[i] for this column
            min_row = min(row_white)
            min_paint = min(min_paint, min_row)
        
        results.append(str(min_paint))
    
    print('\n'.join(results))