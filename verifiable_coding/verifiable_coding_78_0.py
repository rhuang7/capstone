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
            # The row is already all black: no need to paint
            if row_black[i] == m:
                # Check if any column is all black
                for j in range(m):
                    if col_black[j] == n:
                        min_paint = 0
                        break
                if min_paint == 0:
                    break
            # Paint the row to all black: cost is (m - row_black[i])
            row_cost = m - row_black[i]
            # Now find the column that has the most black cells
            max_col_black = max(col_black)
            # The cost to make this column all black is (n - max_col_black)
            col_cost = n - max_col_black
            total_cost = row_cost + col_cost
            if total_cost < min_paint:
                min_paint = total_cost
        
        # Try each column as the vertical part of the cross
        for j in range(m):
            # The column is already all black: no need to paint
            if col_black[j] == n:
                # Check if any row is all black
                for i in range(n):
                    if row_black[i] == m:
                        min_paint = 0
                        break
                if min_paint == 0:
                    break
            # Paint the column to all black: cost is (n - col_black[j])
            col_cost = n - col_black[j]
            # Now find the row that has the most black cells
            max_row_black = max(row_black)
            # The cost to make this row all black is (m - max_row_black)
            row_cost = m - max_row_black
            total_cost = col_cost + row_cost
            if total_cost < min_paint:
                min_paint = total_cost
        
        results.append(str(min_paint))
    
    print('\n'.join(results))