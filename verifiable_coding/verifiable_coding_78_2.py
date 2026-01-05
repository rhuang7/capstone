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
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '*':
                    col_black[j] += 1
        
        min_paint = float('inf')
        
        # Try each row as the horizontal part of the cross
        for i in range(n):
            # The row is already all black: no paint needed
            if row_black[i] == m:
                # Check if any column is all black
                for j in range(m):
                    if col_black[j] == n:
                        min_paint = 0
                        break
                break
            # Paint the row to be all black: m - row_black[i] paints
            # Now check for any column that is all black (already black cells + 0)
            for j in range(m):
                if col_black[j] == n:
                    min_paint = min(min_paint, m - row_black[i])
                    break
        
        # Try each column as the vertical part of the cross
        for j in range(m):
            # The column is already all black: no paint needed
            if col_black[j] == n:
                # Check if any row is all black
                for i in range(n):
                    if row_black[i] == m:
                        min_paint = 0
                        break
                break
            # Paint the column to be all black: n - col_black[j] paints
            # Now check for any row that is all black (already black cells + 0)
            for i in range(n):
                if row_black[i] == m:
                    min_paint = min(min_paint, n - col_black[j])
                    break
        
        results.append(str(min_paint))
    
    print('\n'.join(results))