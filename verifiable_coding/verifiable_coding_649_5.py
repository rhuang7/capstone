import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    for _ in range(T):
        n = int(data[idx])
        m = int(data[idx+1])
        idx += 2
        grid = []
        for i in range(n):
            row = data[idx]
            grid.append(row)
            idx += 1
        S = data[idx]
        idx += 1
        
        # Convert grid to set of positions
        positions = set()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    positions.add((i, j))
        
        # Process each force
        for direction in S:
            new_positions = set()
            if direction == 'L':
                # Move left
                for (i, j) in positions:
                    if j > 0 and (i, j-1) not in positions:
                        new_positions.add((i, j-1))
                for (i, j) in positions:
                    if (i, j-1) not in new_positions:
                        new_positions.add((i, j))
            elif direction == 'R':
                # Move right
                for (i, j) in positions:
                    if j < m-1 and (i, j+1) not in positions:
                        new_positions.add((i, j+1))
                for (i, j) in positions:
                    if (i, j+1) not in new_positions:
                        new_positions.add((i, j))
            elif direction == 'U':
                # Move up
                for (i, j) in positions:
                    if i > 0 and (i-1, j) not in positions:
                        new_positions.add((i-1, j))
                for (i, j) in positions:
                    if (i-1, j) not in new_positions:
                        new_positions.add((i, j))
            elif direction == 'D':
                # Move down
                for (i, j) in positions:
                    if i < n-1 and (i+1, j) not in positions:
                        new_positions.add((i+1, j))
                for (i, j) in positions:
                    if (i+1, j) not in new_positions:
                        new_positions.add((i, j))
            positions = new_positions
        
        # Convert back to grid
        result = []
        for i in range(n):
            row = ['0'] * m
            for (x, y) in positions:
                if x == i:
                    row[y] = '1'
            result.append(''.join(row))
        for line in result:
            print(line)