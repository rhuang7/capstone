import sys
import collections

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    q = int(data[0])
    idx = 1
    
    for _ in range(q):
        n = int(data[idx])
        idx += 1
        top = data[idx]
        idx += 1
        bottom = data[idx]
        idx += 1
        
        # Convert to list of integers
        top = [int(c) for c in top]
        bottom = [int(c) for c in bottom]
        
        # Directions: 0 - left, 1 - up, 2 - right, 3 - down
        # For each pipe, determine its direction based on type
        # 1 and 2 are straight pipes, 3,4,5,6 are curved
        # We'll represent each pipe as a direction (0, 1, 2, 3)
        # For straight pipes, direction is fixed (1 is down, 2 is up)
        # For curved pipes, direction can be changed (we'll try all possibilities)
        
        # Initialize direction for each pipe
        # For top row
        top_dir = [0] * n
        for i in range(n):
            if top[i] == 1:
                top_dir[i] = 1  # down
            elif top[i] == 2:
                top_dir[i] = 3  # up
            else:
                # Curved pipes can be turned to any direction
                # We'll try all possibilities later
                pass
        
        # For bottom row
        bottom_dir = [0] * n
        for i in range(n):
            if bottom[i] == 1:
                bottom_dir[i] = 3  # up
            elif bottom[i] == 2:
                bottom_dir[i] = 1  # down
            else:
                # Curved pipes can be turned to any direction
                pass
        
        # We'll use BFS to find a path from (1, 0) to (2, n+1)
        # We'll represent the state as (row, col, direction)
        # We'll use a queue for BFS
        # We'll also use a visited set to avoid cycles
        
        # Start at (1, 0), direction is left (0)
        queue = collections.deque()
        visited = set()
        queue.append((0, 0, 0))  # (row, col, direction)
        visited.add((0, 0, 0))
        
        found = False
        
        while queue:
            row, col, direction = queue.popleft()
            
            # Check if we've reached the end
            if row == 1 and col == n:
                found = True
                break
            
            # Try all possible directions for the current pipe
            # For straight pipes, only one direction is possible
            # For curved pipes, all four directions are possible
            if row == 0:
                # Top row
                pipe = top[col]
                if pipe in [1, 2]:
                    # Straight pipe
                    if pipe == 1:
                        # Down
                        new_row, new_col = 1, col
                        new_dir = 1
                    else:
                        # Up
                        new_row, new_col = 0, col
                        new_dir = 3
                    if (new_row, new_col, new_dir) not in visited:
                        visited.add((new_row, new_col, new_dir))
                        queue.append((new_row, new_col, new_dir))
                else:
                    # Curved pipe, try all four directions
                    for d in [0, 1, 2, 3]:
                        new_row, new_col = 0, col
                        new_dir = d
                        if (new_row, new_col, new_dir) not in visited:
                            visited.add((new_row, new_col, new_dir))
                            queue.append((new_row, new_col, new_dir))
            else:
                # Bottom row
                pipe = bottom[col]
                if pipe in [1, 2]:
                    # Straight pipe
                    if pipe == 1:
                        # Up
                        new_row, new_col = 0, col
                        new_dir = 3
                    else:
                        # Down
                        new_row, new_col = 1, col
                        new_dir = 1
                    if (new_row, new_col, new_dir) not in visited:
                        visited.add((new_row, new_col, new_dir))
                        queue.append((new_row, new_col, new_dir))
                else:
                    # Curved pipe, try all four directions
                    for d in [0, 1, 2, 3]:
                        new_row, new_col = 1, col
                        new_dir = d
                        if (new_row, new_col, new_dir) not in visited:
                            visited.add((new_row, new_col, new_dir))
                            queue.append((new_row, new_col, new_dir))
        
        print("YES" if found else "NO")

if __name__ == '__main__':
    solve()