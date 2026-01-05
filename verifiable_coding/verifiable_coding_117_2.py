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
        m = int(data[idx+1])
        idx += 2
        
        rows = []
        for _ in range(n):
            row = list(map(int, data[idx:idx+m]))
            rows.append(row)
            idx += m
        
        cols = []
        for _ in range(m):
            col = list(map(int, data[idx:idx+n]))
            cols.append(col)
            idx += n
        
        # Create a set of all elements
        all_elements = set()
        for row in rows:
            all_elements.update(row)
        
        # Create a dictionary to map values to their positions
        value_to_pos = {}
        for i in range(n):
            for j in range(m):
                value_to_pos[rows[i][j]] = (i, j)
        
        # Create a grid to store the result
        grid = [[0] * m for _ in range(n)]
        
        # Assign values to the grid
        for val in all_elements:
            i, j = value_to_pos[val]
            grid[i][j] = val
        
        # Now, we need to arrange the rows and columns such that the columns match the given column data
        # We'll find the correct row and column order
        
        # Find the correct row order
        row_order = []
        for i in range(n):
            for j in range(m):
                if grid[i][j] == rows[0][j]:
                    row_order.append(i)
                    break
        
        # Find the correct column order
        col_order = []
        for j in range(m):
            for i in range(n):
                if grid[i][j] == cols[0][i]:
                    col_order.append(j)
                    break
        
        # Reorder the grid according to the row and column orders
        final_grid = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                final_grid[i][j] = grid[row_order[i]][col_order[j]]
        
        # Add the final grid to results
        for row in final_grid:
            results.append(' '.join(map(str, row)) + ' ')
    
    # Print all results
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()