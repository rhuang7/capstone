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
        # Create a dictionary to map columns to their values
        col_to_values = {}
        for i in range(m):
            col = cols[i]
            col_to_values[i] = col
        # Create a dictionary to map rows to their values
        row_to_values = {}
        for i in range(n):
            row = rows[i]
            row_to_values[i] = row
        # Create a grid
        grid = [[0]*m for _ in range(n)]
        # Fill the grid
        for i in range(n):
            for j in range(m):
                val = rows[i][j]
                grid[i][j] = val
        # Check if the grid is correct
        # We need to ensure that the columns match
        for i in range(m):
            col = []
            for j in range(n):
                col.append(grid[j][i])
            if col != cols[i]:
                # Find the correct column
                for k in range(m):
                    if col == cols[k]:
                        # Swap the columns
                        for j in range(n):
                            grid[j][i], grid[j][k] = grid[j][k], grid[j][i]
                        break
        # Output the grid
        for row in grid:
            results.append(' '.join(map(str, row)) + ' ')
    print('\n'.join(results))

if __name__ == '__main__':
    solve()