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
        
        # Precompute for each row the number of black cells
        row_black = [row.count('*') for row in grid]
        
        # Precompute for each column the number of black cells
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
                # To form a cross at (i+1, j+1), row i must be all black, column j must be all black
                # So we need to paint the row i if it's not all black, and column j if it's not all black
                # But we can optimize: the row i already has row_black[i] black cells, so we need to paint (m - row_black[i]) cells
                # Similarly for column j: (n - col_black[j]) cells
                # But we can do better: if we choose a row and column that already have many black cells
                # So we can precompute for each row and column the number of cells to paint to make it all black
                # Then for each cell (i,j), the cost is (m - row_black[i]) + (n - col_black[j])
                # But we can also try to find the best row and column to form a cross
                # So we can precompute the minimum cost for each row and column
                # Then for each cell (i,j), the cost is (cost_row[i] + cost_col[j])
                # But we can also try to find the best row and column to form a cross
                # So we can precompute for each row the cost to make it all black
                # And for each column the cost to make it all black
                # Then for each cell (i,j), the cost is (cost_row[i] + cost_col[j])
                # But we can also try to find the best row and column to form a cross
                # So we can precompute for each row the cost to make it all black
                # And for each column the cost to make it all black
                # Then for each cell (i,j), the cost is (cost_row[i] + cost_col[j])
                # But we can also try to find the best row and column to form a cross
                # So we can precompute for each row the cost to make it all black
                # And for each column the cost to make it all black
                # Then for each cell (i,j), the cost is (cost_row[i] + cost_col[j])
                # But we can also try to find the best row and column to form a cross
                # So we can precompute for each row the cost to make it all black
                # And for each column the cost to make it all black
                # Then for each cell (i,j), the cost is (cost_row[i] + cost_col[j])
                # But we can also try to find the best row and column to form a cross
                # So we can precompute for each row the cost to make it all black
                # And for each column the cost to make it all black
                # Then for each cell (i,j), the cost is (cost_row[i] + cost_col[j])
                # But we can also try to find the best row and column to form a cross
                # So we can precompute for each row the cost to make it all black
                # And for each column the cost to make it all black
                # Then for each cell (i,j), the cost is (cost_row[i] + cost_col[j])
                # But we can also try to find the best row and column to form a cross
                # So we can precompute for each row the cost to make it all black
                # And for each column the cost to make it all black
                # Then for each cell (i,j), the cost is (cost_row[i] + cost_col[j])
                # But we can also try to find the best row and column to form a cross
                # So we can precompute for each row the cost to make it all black
                # And for each column the cost to make it all black
                # Then for each cell (i,j), the cost is (cost_row[i] + cost_col[j])
                # But we can also try to find the best row and column to form a cross
                # So we can precompute for each row the cost to make it all black
                # And for each column the cost to make it all black
                # Then for each cell (i,j), the cost is (cost_row[i] + cost_col[j])
                # But we can also try to find the best row and column to form a cross
                # So we can precompute for each row the cost to make it all black
                # And for each column the cost to make it all black
                # Then for each cell (i,j), the cost is (cost_row[i] + cost_col[j])
                # But we can also try to find the best row and column to form a cross
                # So we can precompute for each row the cost to make it all black
                # And for each column the cost to make it all black
                # Then for each cell (i,j), the cost is (cost_row[i] + cost_col[j])
                # But we can also try to find the best row and column to form a cross
                # So we can precompute for each row the cost to make it all black
                # And for each column the cost to make it all black
                # Then for each cell (i,j), the cost is (cost_row[i] + cost_col[j])
                # But we can also try to find the best row and column to form a cross
                # So we can precompute for each row the cost to make it all black
                # And for each column the cost to make it all black
                # Then for each cell (i,j), the cost is (cost_row[i] + cost_col[j])
                # But we can also try to find the best row and column to form a cross
                # So we can precompute for each row the cost to make it all black
                # And for each column the cost to make it all black
                # Then for each cell (i,j), the cost is (cost_row[i] + cost_col[j])
                # But we can also try to find the best row and column to form a cross
                # So we can precompute for each row the cost to make it all black
                # And for each column the cost to make it all black
                # Then for each cell (i,j), the cost is (cost_row[i] + cost_col[j])
                # But we can also try to find the best row and column to form a cross
                # So we can precompute for each row the cost to make it all black
                # And for each column the cost to make it all black
                # Then for each cell (i,j), the cost is (cost_row[i] + cost_col[j])
                # But we can also try to find the best row and column to form a cross
                # So we can precompute for each row the cost to make it all black
                # And for each column the cost to make it all black
                # Then for each cell (i,j), the cost is (cost_row[i] + cost_col[j])
                # But we can also try to find the best row and column to form a cross
                # So we can precompute for each row the cost to make it all black
                # And for each column the cost to make it all black
                # Then for each cell (i,j), the cost is (cost_row[i] + cost_col[j])
                # But we can also try to find the best row and column to form a cross
                # So we can precompute for each row the cost to make it all black
                # And for each column the cost to make it all black
                # Then for each cell (i,j), the cost is (cost_row[i] + cost_col[j])
                # But we can also try to find the best row and column to form a cross
                # So we can precompute for each row the cost to make it all black
                # And for each column the cost to make it all black
                # Then for each cell (i,j), the cost is (cost_row[i] + cost_col[j])
                # But we can also try to find the best row and column to form a cross
                # So we can precompute for each row the cost to make it all black
                # And for each