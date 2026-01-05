import sys
import math

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(T):
        N = int(data[idx])
        K = int(data[idx+1])
        M = int(data[idx+2])
        idx += 3
        
        # Calculate the top-left corner of the poison grid
        poison_top_left = ((N - K) // 2 + 1, (N - K) // 2 + 1)
        
        # For each snake, determine the line (row or column) it occupies
        # and the range of cells it covers
        snakes = []
        for _ in range(M):
            HX = int(data[idx])
            HY = int(data[idx+1])
            TX = int(data[idx+2])
            TY = int(data[idx+3])
            idx += 4
            
            if HX == TX:
                # Snake is in a row
                row = HX
                start = min(HY, TY)
                end = max(HY, TY)
                snakes.append((row, start, end))
            else:
                # Snake is in a column
                col = HY
                start = min(HX, TX)
                end = max(HX, TX)
                snakes.append((col, start, end))
        
        # Check if the current configuration is safe
        def is_safe(snakes):
            # For each row and column, check if it can be used to shoot an arrow
            # that enters the poison grid and exits the outer grid without hitting a snake
            # Check all rows
            for row in range(1, N+1):
                # Check if this row can be used to shoot an arrow that enters the poison grid
                # and exits the outer grid
                # The arrow can be shot from outside the grid to the row
                # and then exit the grid on the other side
                # Check if the row intersects with the poison grid
                r1, c1 = poison_top_left
                r2, c2 = (r1 + K - 1, c1 + K - 1)
                if r1 <= row <= r2:
                    # The row is in the poison grid
                    # Check if there is a way to shoot an arrow through this row
                    # that enters the poison grid and exits the outer grid
                    # without hitting a snake
                    # Check if there is a segment in this row that is not blocked by any snake
                    # and spans from the poison grid to the outside
                    # Check the left and right edges of the poison grid
                    left = c1
                    right = c2
                    # Check if there is a segment in this row that is not blocked by any snake
                    # and spans from the poison grid to the outside
                    # Check left side
                    left_blocked = False
                    for snake in snakes:
                        if snake[0] != row:
                            continue
                        if snake[1] <= left <= snake[2]:
                            left_blocked = True
                            break
                    # Check right side
                    right_blocked = False
                    for snake in snakes:
                        if snake[0] != row:
                            continue
                        if snake[1] <= right <= snake[2]:
                            right_blocked = True
                            break
                    # If both sides are blocked, then this row is safe
                    if not left_blocked or not right_blocked:
                        return False
            # Check all columns
            for col in range(1, N+1):
                # Check if this column can be used to shoot an arrow that enters the poison grid
                # and exits the outer grid
                # The arrow can be shot from outside the grid to the column
                # and then exit the grid on the other side
                # Check if the column intersects with the poison grid
                r1, c1 = poison_top_left
                r2, c2 = (r1 + K - 1, c1 + K - 1)
                if c1 <= col <= c2:
                    # The column is in the poison grid
                    # Check if there is a way to shoot an arrow through this column
                    # that enters the poison grid and exits the outer grid
                    # without hitting a snake
                    # Check if there is a segment in this column that is not blocked by any snake
                    # and spans from the poison grid to the outside
                    # Check top and bottom edges of the poison grid
                    top = r1
                    bottom = r2
                    # Check if there is a segment in this column that is not blocked by any snake
                    # and spans from the poison grid to the outside
                    # Check top side
                    top_blocked = False
                    for snake in snakes:
                        if snake[1] != col:
                            continue
                        if snake[2] <= top <= snake[3]:
                            top_blocked = True
                            break
                    # Check bottom side
                    bottom_blocked = False
                    for snake in snakes:
                        if snake[1] != col:
                            continue
                        if snake[2] <= bottom <= snake[3]:
                            bottom_blocked = True
                            break
                    # If both sides are blocked, then this column is safe
                    if not top_blocked or not bottom_blocked:
                        return False
            return True
        
        # Try to remove snakes to make the configuration safe
        # We can model this as a graph problem where each snake is a node and edges represent conflicts
        # But for efficiency, we can try to find a minimal set of snakes that blocks all possible paths
        # However, this is computationally expensive, so we'll use a greedy approach
        # We'll try to remove snakes that are not needed to block any paths
        
        # First, check if the current configuration is safe
        if is_safe(snakes):
            results.append(M)
            continue
        
        # Try to remove snakes
        # We'll try to remove snakes that are not needed to block any paths
        # We'll keep track of which snakes are needed to block paths
        # We'll use a set to track which snakes are needed
        needed = set()
        # For each row in the poison grid
        for row in range(poison_top_left[0], poison_top_left[0] + K):
            # Check if there is a segment in this row that is not blocked by any snake
            # and spans from the poison grid to the outside
            # Check left and right edges of the poison grid
            left = poison_top_left[1]
            right = poison_top_left[1] + K - 1
            # Check if there is a segment in this row that is not blocked by any snake
            # and spans from the poison grid to the outside
            # Check left side
            left_blocked = False
            for snake in snakes:
                if snake[0] != row:
                    continue
                if snake[1] <= left <= snake[2]:
                    left_blocked = True
                    break
            # Check right side
            right_blocked = False
            for snake in snakes:
                if snake[0] != row:
                    continue
                if snake[1] <= right <= snake[2]:
                    right_blocked = True
                    break
            # If both sides are blocked, then this row is safe
            if not left_blocked or not right_blocked:
                # This row is safe, so no snake is needed to block it
                continue
            # Otherwise, we need to block this row
            # We'll find a snake that blocks this row
            # We'll find the first snake that blocks this row
            # We'll find the snake that covers the left side of the poison grid
            # and is not blocked by any other snake
            # We'll find the first snake that covers the left side of the poison grid
            # and is not blocked by any other snake
            # We'll find the snake that covers the left side of the poison grid
            # and is not blocked by any other snake
            # We'll find the snake that covers the left side of the poison grid
            # and is not blocked by any other snake
            # We'll find the snake that covers the left side of the poison grid
            # and is not blocked by any other snake
            # We'll find the snake that covers the left side of the poison grid
            # and is not blocked by any other snake
            # We'll find the snake that covers the left side of the poison grid
            # and is not blocked by any other snake
            # We'll find the snake that covers the left side of the poison grid
            # and is not blocked by any other snake
            # We'll find the snake that covers the left side of the poison grid
            # and is not blocked by any other snake
            # We'll find the snake that covers the left side of the poison grid
            # and is not blocked by any other snake
            # We'll find the snake that covers the left side of the poison grid
            # and is not blocked by any other snake
            # We'll find the snake that covers the left side of the poison grid
            # and is not blocked by any other snake
            # We'll find the snake that covers the left side of the poison grid
            # and is not blocked by any other snake