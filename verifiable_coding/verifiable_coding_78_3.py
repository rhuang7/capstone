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
        
        # Precompute for each row: number of black cells
        row_black = [row.count('*') for row in grid]
        
        # Precompute for each column: number of black cells
        col_black = [0] * m
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '*':
                    col_black[j] += 1
        
        min_paint = float('inf')
        
        # Try each row as the horizontal part of the cross
        for i in range(n):
            # The row is already all black: no need to paint
            if row_black[i] == m:
                # Check if any column is all black
                for j in range(m):
                    if col_black[j] == n:
                        min_paint = 0
                        break
                break
            # Number of cells to paint in this row: m - row_black[i]
            row_paint = m - row_black[i]
            
            # Try each column as the vertical part of the cross
            for j in range(m):
                # Number of cells to paint in this column: n - col_black[j]
                col_paint = n - col_black[j]
                # Total paint needed for this cross
                total = row_paint + col_paint
                if total < min_paint:
                    min_paint = total
        
        results.append(str(min_paint))
    
    print('\n'.join(results))