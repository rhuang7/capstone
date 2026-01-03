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
        
        # Try each row as the horizontal part of the cross
        for i in range(n):
            # The row is already all black: no need to paint
            if row_black[i] == m:
                min_paint = 0
                break
            # Need to paint (m - row_black[i]) cells in this row
            # Then find a column that has (n - col_black[j]) cells to paint
            # The total is (m - row_black[i]) + (n - col_black[j])
            # We want to minimize this
            # So find the column with maximum col_black[j]
            max_col_black = max(col_black)
            min_paint = min(min_paint, (m - row_black[i]) + (n - max_col_black))
        
        # Try each column as the vertical part of the cross
        for j in range(m):
            # The column is already all black: no need to paint
            if col_black[j] == n:
                min_paint = 0
                break
            # Need to paint (n - col_black[j]) cells in this column
            # Then find a row that has (m - row_black[i]) cells to paint
            # The total is (n - col_black[j]) + (m - row_black[i])
            # We want to minimize this
            # So find the row with maximum row_black[i]
            max_row_black = max(row_black)
            min_paint = min(min_paint, (n - col_black[j]) + (m - max_row_black))
        
        results.append(str(min_paint))
    
    print('\n'.join(results))