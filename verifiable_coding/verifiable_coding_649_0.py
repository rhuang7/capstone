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
            grid.append(row)
            idx += 1
        
        S = data[idx]
        idx += 1
        
        # Process forces
        for direction in S:
            # Create a set of positions of particles
            positions = set()
            for i in range(n):
                for j in range(m):
                    if grid[i][j] == '1':
                        positions.add((i, j))
            
            # Move particles in the given direction
            new_positions = set()
            for (i, j) in positions:
                if direction == 'L':
                    if j > 0 and grid[i][j-1] == '0':
                        new_positions.add((i, j-1))
                elif direction == 'R':
                    if j < m-1 and grid[i][j+1] == '0':
                        new_positions.add((i, j+1))
                elif direction == 'U':
                    if i > 0 and grid[i-1][j] == '0':
                        new_positions.add((i-1, j))
                elif direction == 'D':
                    if i < n-1 and grid[i+1][j] == '0':
                        new_positions.add((i+1, j))
            
            # Update grid
            for i in range(n):
                for j in range(m):
                    if (i, j) in new_positions:
                        grid[i] = grid[i][:j] + '1' + grid[i][j+1:]
                    else:
                        grid[i] = grid[i][:j] + '0' + grid[i][j+1:]
        
        # Prepare output
        result = '\n'.join(grid)
        results.append(result)
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()