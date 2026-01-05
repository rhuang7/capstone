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
        
        # Convert grid to set of positions
        particles = set()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    particles.add((i, j))
        
        # Process each force
        for direction in S:
            new_particles = set()
            moved = set()
            if direction == 'L':
                # Move left
                for (i, j) in particles:
                    if j > 0 and (i, j-1) not in particles:
                        moved.add((i, j))
                        new_particles.add((i, j-1))
                for (i, j) in particles:
                    if (i, j) not in moved:
                        new_particles.add((i, j))
            elif direction == 'R':
                # Move right
                for (i, j) in particles:
                    if j < m-1 and (i, j+1) not in particles:
                        moved.add((i, j))
                        new_particles.add((i, j+1))
                for (i, j) in particles:
                    if (i, j) not in moved:
                        new_particles.add((i, j))
            elif direction == 'U':
                # Move up
                for (i, j) in particles:
                    if i > 0 and (i-1, j) not in particles:
                        moved.add((i, j))
                        new_particles.add((i-1, j))
                for (i, j) in particles:
                    if (i, j) not in moved:
                        new_particles.add((i, j))
            elif direction == 'D':
                # Move down
                for (i, j) in particles:
                    if i < n-1 and (i+1, j) not in particles:
                        moved.add((i, j))
                        new_particles.add((i+1, j))
                for (i, j) in particles:
                    if (i, j) not in moved:
                        new_particles.add((i, j))
            particles = new_particles
        
        # Convert back to grid
        result = []
        for i in range(n):
            row = ['0'] * m
            for (x, y) in particles:
                if x == i:
                    row[y] = '1'
            result.append(''.join(row))
        results.append('\n'.join(result))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()