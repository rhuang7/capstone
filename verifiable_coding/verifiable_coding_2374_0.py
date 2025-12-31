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
        
        # Directions: 0 - right, 1 - down, 2 - left, 3 - up
        # We'll use BFS to find if there's a path from (1, 0) to (2, n+1)
        
        # For each pipe, we'll store its direction
        # 1 and 2 are straight, 3-6 are curved
        # For straight pipes, they can be rotated to either direction
        # For curved pipes, they can be rotated to two possible directions
        
        # We'll represent the direction of each pipe as a list of possible directions
        # For each cell (i, j), we'll store a list of possible directions
        # 0: right, 1: down, 2: left, 3: up
        
        # For each cell, we'll store the possible directions it can have
        # For straight pipes (1, 2), they can be either horizontal or vertical
        # For curved pipes (3-6), they can be either right-down or left-up (or other combinations)
        
        # Define the possible directions for each pipe type
        pipe_directions = {
            1: [0, 1],  # horizontal or vertical
            2: [0, 1],  # horizontal or vertical
            3: [0, 1],  # right-down or left-up
            4: [0, 1],  # right-down or left-up
            5: [0, 1],  # right-down or left-up
            6: [0, 1],  # right-down or left-up
        }
        
        # Create a grid of possible directions
        dir_grid = [[[] for _ in range(n)] for _ in range(2)]
        for i in range(2):
            for j in range(n):
                pipe_type = top[j] if i == 0 else bottom[j]
                dir_grid[i][j] = pipe_directions[pipe_type]
        
        # BFS from (0, 0) (top left pipe)
        # We'll track visited cells and their direction
        # We'll use a queue of (row, col, direction)
        # We'll also track visited cells and directions to avoid revisiting
        visited = [[set() for _ in range(n)] for _ in range(2)]
        queue = collections.deque()
        queue.append((0, 0, 0))  # start at (0, 0) with direction right
        visited[0][0].add(0)
        
        while queue:
            r, c, d = queue.popleft()
            
            # Check if we've reached the end
            if r == 1 and c == n - 1 and d == 0:
                print("YES")
                break
            if r == 1 and c == n - 1 and d == 1:
                print("YES")
                break
            
            # Try all possible directions from this cell
            for next_d in dir_grid[r][c]:
                # Check if the next cell is valid
                if r == 0:
                    if next_d == 0:  # right
                        if c + 1 < n:
                            if next_d in visited[0][c + 1]:
                                continue
                            visited[0][c + 1].add(next_d)
                            queue.append((0, c + 1, next_d))
                    elif next_d == 1:  # down
                        if r + 1 < 2:
                            if next_d in visited[1][c]:
                                continue
                            visited[1][c].add(next_d)
                            queue.append((1, c, next_d))
                else:
                    if next_d == 0:  # right
                        if c + 1 < n:
                            if next_d in visited[1][c + 1]:
                                continue
                            visited[1][c + 1].add(next_d)
                            queue.append((1, c + 1, next_d))
                    elif next_d == 1:  # down
                        if r + 1 < 2:
                            if next_d in visited[1][c]:
                                continue
                            visited[1][c].add(next_d)
                            queue.append((1, c, next_d))
        else:
            print("NO")