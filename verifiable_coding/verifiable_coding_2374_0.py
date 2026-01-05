import sys
import re

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
        idx += 1
        top = data[idx]
        idx += 1
        bottom = data[idx]
        idx += 1
        
        # Convert to integers
        top = [int(c) for c in top]
        bottom = [int(c) for c in bottom]
        
        # Check if it's possible to form a valid path
        # We need to check if there's a path from (1, 0) to (2, n+1)
        # This is a graph problem where each cell is a node and edges represent connections
        # We can model this as a graph and perform BFS or DFS
        
        # Directions: (dx, dy)
        # 0: right
        # 1: down
        # 2: left
        # 3: up
        # For each cell, we can determine the possible directions it can flow to
        # Based on the pipe type and its orientation
        
        # We'll use BFS to check if there's a path from (1, 0) to (2, n+1)
        # We'll represent the grid as a 2D array and track visited cells
        
        # Create a grid of size 2 x (n+2) to handle the extra cells
        grid = [[0] * (n + 2) for _ in range(2)]
        grid[0][0] = top[0]
        grid[1][n] = bottom[0]
        
        # We'll use a queue for BFS
        from collections import deque
        queue = deque()
        queue.append((0, 0))  # Starting at (1, 0)
        visited = [[False] * (n + 2) for _ in range(2)]
        visited[0][0] = True
        
        # Directions: right, down, left, up
        directions = [(0, 1), (1, 0), (0, -1), (0, 0)]  # (dx, dy)
        
        # For each cell, we'll determine the possible directions it can flow to
        # Based on the pipe type and its orientation
        # We'll use a helper function to determine the possible directions
        def get_directions(pipe_type, orientation):
            # orientation: 0 (original), 1 (90 degrees clockwise), 2 (180 degrees), 3 (270 degrees)
            # For each pipe type, determine the possible directions it can flow to
            # Based on the pipe's shape
            # For straight pipes (types 1 and 2), they can flow in two directions
            # For curved pipes (types 3, 4, 5, 6), they can flow in two directions
            # We'll return a list of possible directions (0, 1, 2, 3)
            if pipe_type in [1, 2]:
                # Straight pipes can flow right or left
                if orientation == 0:
                    return [0, 2]
                elif orientation == 1:
                    return [1, 3]
                elif orientation == 2:
                    return [0, 2]
                elif orientation == 3:
                    return [1, 3]
            elif pipe_type in [3, 4, 5, 6]:
                # Curved pipes can flow in two directions
                if orientation == 0:
                    return [0, 1]
                elif orientation == 1:
                    return [1, 2]
                elif orientation == 2:
                    return [2, 3]
                elif orientation == 3:
                    return [3, 0]
        
        # We'll perform BFS
        while queue:
            x, y = queue.popleft()
            if x == 1 and y == n + 1:
                results.append("YES")
                break
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < 2 and 0 <= ny < (n + 2):
                    if not visited[nx][ny]:
                        # Determine the possible directions the current cell can flow to
                        pipe_type = grid[x][y]
                        # Try all possible orientations
                        for orientation in range(4):
                            directions_out = get_directions(pipe_type, orientation)
                            if dy in directions_out:
                                # Check if the next cell is connected
                                if nx == 0 and ny == y + 1:
                                    # Current cell is (0, y), next is (0, y+1)
                                    # Check if the pipe can flow right
                                    if 0 in directions_out:
                                        visited[nx][ny] = True
                                        queue.append((nx, ny))
                                        break
                                elif nx == 1 and ny == y + 1:
                                    # Current cell is (1, y), next is (1, y+1)
                                    # Check if the pipe can flow right
                                    if 0 in directions_out:
                                        visited[nx][ny] = True
                                        queue.append((nx, ny))
                                        break
                                elif nx == 0 and ny == y - 1:
                                    # Current cell is (0, y), next is (0, y-1)
                                    # Check if the pipe can flow left
                                    if 2 in directions_out:
                                        visited[nx][ny] = True
                                        queue.append((nx, ny))
                                        break
                                elif nx == 1 and ny == y - 1:
                                    # Current cell is (1, y), next is (1, y-1)
                                    # Check if the pipe can flow left
                                    if 2 in directions_out:
                                        visited[nx][ny] = True
                                        queue.append((nx, ny))
                                        break
                                elif nx == 1 and ny == y + 1:
                                    # Current cell is (0, y), next is (1, y)
                                    # Check if the pipe can flow down
                                    if 1 in directions_out:
                                        visited[nx][ny] = True
                                        queue.append((nx, ny))
                                        break
                                elif nx == 0 and ny == y + 1:
                                    # Current cell is (1, y), next is (0, y)
                                    # Check if the pipe can flow up
                                    if 3 in directions_out:
                                        visited[nx][ny] = True
                                        queue.append((nx, ny))
                                        break
            else:
                continue
            break
        else:
            results.append("NO")
    
    print("\n".join(results))