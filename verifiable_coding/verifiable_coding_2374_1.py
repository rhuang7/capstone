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
        row1 = data[idx]
        idx += 1
        row2 = data[idx]
        idx += 1
        
        # Convert rows to lists of integers
        row1 = [int(c) for c in row1]
        row2 = [int(c) for c in row2]
        
        # Define the pipe types and their possible orientations
        # Each pipe can be rotated 0, 90, 180, or 270 degrees
        # For each type, we define the possible directions it can connect
        # Directions are represented as tuples (dx, dy)
        # 0: straight horizontal
        # 1: straight vertical
        # 2: curved left
        # 3: curved right
        # 4: curved up
        # 5: curved down
        
        # For each pipe type, define the possible orientations
        pipe_orientations = {
            1: [(0, 1), (1, 0)],  # straight horizontal or vertical
            2: [(0, 1), (1, 0)],  # same as above
            3: [(0, 1), (1, 0)],  # same as above
            4: [(0, 1), (1, 0)],  # same as above
            5: [(0, 1), (1, 0)],  # same as above
            6: [(0, 1), (1, 0)],  # same as above
        }
        
        # For each pipe, determine the possible directions it can connect
        # We'll use BFS to find a path from (1, 0) to (2, n+1)
        
        # Directions: (dx, dy)
        directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]
        
        # For each position, we'll track the possible directions it can connect
        # We'll use BFS to find a path from (1, 0) to (2, n+1)
        
        # Start from (1, 0) which is to the left of the top left pipe
        # We can only enter the top left pipe from the left
        # So we start by checking the top left pipe
        # The top left pipe is at (1, 1)
        # We need to check if it can connect to the left (from (1, 0))
        # So we check the possible orientations of the top left pipe
        
        # For each pipe, we'll check all possible orientations
        # We'll use BFS to find a path from (1, 0) to (2, n+1)
        
        # We'll use a queue to perform BFS
        # Each element in the queue is a tuple (x, y, dir)
        # dir is the direction the pipe is facing (0: right, 1: down, 2: left, 3: up)
        
        # We'll also use a visited set to avoid revisiting the same position with the same direction
        
        # We start from (1, 0), which is to the left of the top left pipe
        # We can only enter the top left pipe from the left
        # So we check the top left pipe's possible orientations
        
        # Initialize the queue
        queue = collections.deque()
        visited = set()
        
        # The top left pipe is at (1, 1)
        # We can enter it from the left (direction 2)
        # So we check if the top left pipe can connect to the left
        # For each possible orientation of the top left pipe, check if it can connect to the left
        
        # For each possible orientation of the top left pipe
        for dir in pipe_orientations[row1[0]]:
            # Check if the pipe can connect to the left (direction 2)
            # The pipe is at (1, 1)
            # If the pipe is facing right (dir 0), it can connect to the left
            # If the pipe is facing down (dir 1), it can connect to the left
            # If the pipe is facing left (dir 2), it can connect to the left
            # If the pipe is facing up (dir 3), it can connect to the left
            # So all orientations can connect to the left
            # So we add (1, 1, dir) to the queue
            queue.append((1, 1, dir))
            visited.add((1, 1, dir))
        
        # Perform BFS
        found = False
        while queue:
            x, y, dir = queue.popleft()
            
            # Check if we've reached the end
            if x == 2 and y == n + 1:
                found = True
                break
            
            # For each possible direction the pipe can connect
            # We need to check the next cell in that direction
            # For example, if the pipe is facing right (dir 0), the next cell is (x, y+1)
            # If the pipe is facing down (dir 1), the next cell is (x+1, y)
            # If the pipe is facing left (dir 2), the next cell is (x, y-1)
            # If the pipe is facing up (dir 3), the next cell is (x-1, y)
            next_x, next_y = x + directions[dir][0], y + directions[dir][1]
            
            # Check if the next cell is within the grid
            if 1 <= next_x <= 2 and 1 <= next_y <= n:
                # Check if the next cell is in the same row or adjacent row
                if next_x == x:
                    # Same row, check the pipe at (x, next_y)
                    # The pipe at (x, next_y) is in the same row as (x, y)
                    # So we need to check if the pipe can connect to the current direction
                    # The pipe at (x, next_y) can connect to the current direction
                    # So we check all possible orientations of the pipe at (x, next_y)
                    for next_dir in pipe_orientations[row1[next_y-1]] if x == 1 else pipe_orientations[row2[next_y-1]]:
                        # Check if the next pipe can connect to the current direction
                        # The next pipe is at (next_x, next_y)
                        # The current direction is dir
                        # The next pipe's direction must be such that it connects to the current direction
                        # For example, if the current pipe is facing right (dir 0), the next pipe must be facing left (dir 2)
                        # So we check if the next pipe's direction is opposite to the current direction
                        if next_dir == (0 - dir) % 4:
                            # Add the next pipe to the queue
                            queue.append((next_x, next_y, next_dir))
                            visited.add((next_x, next_y, next_dir))
                else:
                    # Different row, check the pipe at (next_x, next_y)
                    # The pipe at (next_x, next_y) is in the other row
                    # So we need to check if the pipe can connect to the current direction
                    # The pipe at (next_x, next_y) can connect to the current direction
                    # So we check all possible orientations of the pipe at (next_x, next_y)
                    for next_dir in pipe_orientations[row1[next_y-1]] if next_x == 1 else pipe_orientations[row2[next_y-1]]:
                        # Check if the next pipe can connect to the current direction
                        # The next pipe is at (next_x, next_y)
                        # The current direction is dir
                        # The next pipe's direction must be such that it connects to the current direction
                        # For example, if the current pipe is facing right (dir 0), the next pipe must be facing left (dir 2)
                        if next_dir == (0 - dir) % 4:
                            # Add the next pipe to the queue
                            queue.append((next_x, next_y, next_dir))
                            visited.add((next_x, next_y, next_dir))
        
        # Output the result
        print("YES" if found else "NO")

if __name__ == '__main__':
    solve()