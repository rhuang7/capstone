import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(T):
        n = int(data[idx])
        m = int(data[idx+1])
        idx += 2
        grid = []
        for i in range(n):
            row = data[idx]
            grid.append([c == '1' for c in row])
            idx += 1
        S = data[idx]
        idx += 1
        
        # Process each force
        for direction in S:
            # Create a copy of the grid to track positions
            new_grid = [[False for _ in range(m)] for _ in range(n)]
            positions = []
            
            # Collect all positions with particles
            for i in range(n):
                for j in range(m):
                    if grid[i][j]:
                        positions.append((i, j))
            
            # Move particles in the given direction
            if direction == 'L':
                # Move left
                for i, j in positions:
                    if j > 0 and not grid[i][j-1]:
                        new_grid[i][j-1] = True
            elif direction == 'R':
                # Move right
                for i, j in positions:
                    if j < m-1 and not grid[i][j+1]:
                        new_grid[i][j+1] = True
            elif direction == 'U':
                # Move up
                for i, j in positions:
                    if i > 0 and not grid[i-1][j]:
                        new_grid[i-1][j] = True
            elif direction == 'D':
                # Move down
                for i, j in positions:
                    if i < n-1 and not grid[i+1][j]:
                        new_grid[i+1][j] = True
            
            # Update the grid
            for i in range(n):
                for j in range(m):
                    grid[i][j] = new_grid[i][j]
        
        # Convert grid to binary strings
        output = []
        for i in range(n):
            row = ''.join(['1' if grid[i][j] else '0' for j in range(m)])
            output.append(row)
        results.append('\n'.join(output))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()