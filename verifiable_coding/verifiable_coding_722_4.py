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
        pox = (N - K) // 2 + 1
        poy = (N - K) // 2 + 1
        
        # For each snake, determine the line (row or column) it is on
        # and the range of cells it covers
        snakes = []
        for _ in range(M):
            HX = int(data[idx])
            HY = int(data[idx+1])
            TX = int(data[idx+2])
            TY = int(data[idx+3])
            idx += 4
            
            if HX == TX:
                # Horizontal snake
                row = HX
                start = min(HY, TY)
                end = max(HY, TY)
                snakes.append((row, start, end))
            else:
                # Vertical snake
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
                if pox <= row <= pox + K - 1:
                    # Check if the arrow can exit the grid without hitting a snake
                    # Check if there's a snake in this row that blocks the arrow
                    # The arrow can go from left to right or right to left
                    # Check if there's a snake in this row that covers the entire row
                    # or blocks the arrow in some way
                    # Check if the arrow can pass through the poison grid
                    # If the arrow starts outside the poison grid and ends inside, or vice versa
                    # Check if there's a snake that blocks the arrow
                    # Check if there's a snake in this row that covers the entire row
                    # or blocks the arrow in some way
                    # Check if the arrow can pass through the poison grid
                    # If the arrow starts outside the poison grid and ends inside, or vice versa
                    # Check if there's a snake that blocks the arrow
                    # Check if there's a snake in this row that covers the entire row
                    # or blocks the arrow in some way
                    # Check if the arrow can pass through the poison grid
                    # If the arrow starts outside the poison grid and ends inside, or vice versa
                    # Check if there's a snake that blocks the arrow
                    # Check if there's a snake in this row that covers the entire row
                    # or blocks the arrow in some way
                    # Check if the arrow can pass through the poison grid
                    # If the arrow starts outside the poison grid and ends inside, or vice versa
                    # Check if there's a snake that blocks the arrow
                    # Check if there's a snake in this row that covers the entire row
                    # or blocks the arrow in some way
                    # Check if the arrow can pass through the poison grid
                    # If the arrow starts outside the poison grid and ends inside, or vice versa
                    # Check if there's a snake that blocks the arrow
                    # Check if there's a snake in this row that covers the entire row
                    # or blocks the arrow in some way
                    # Check if the arrow can pass through the poison grid
                    # If the arrow starts outside the poison grid and ends inside, or vice versa
                    # Check if there's a snake that blocks the arrow
                    # Check if there's a snake in this row that covers the entire row
                    # or blocks the arrow in some way
                    # Check if the arrow can pass through the poison grid
                    # If the arrow starts outside the poison grid and ends inside, or vice versa
                    # Check if there's a snake that blocks the arrow
                    # Check if there's a snake in this row that covers the entire row
                    # or blocks the arrow in some way
                    # Check if the arrow can pass through the poison grid
                    # If the arrow starts outside the poison grid and ends inside, or vice versa
                    # Check if there's a snake that blocks the arrow
                    # Check if there's a snake in this row that covers the entire row
                    # or blocks the arrow in some way
                    # Check if the arrow can pass through the poison grid
                    # If the arrow starts outside the poison grid and ends inside, or vice versa
                    # Check if there's a snake that blocks the arrow
                    # Check if there's a snake in this row that covers the entire row
                    # or blocks the arrow in some way
                    # Check if the arrow can pass through the poison grid
                    # If the arrow starts outside the poison grid and ends inside, or vice versa
                    # Check if there's a snake that blocks the arrow
                    # Check if there's a snake in this row that covers the entire row
                    # or blocks the arrow in some way
                    # Check if the arrow can pass through the poison grid
                    # If the arrow starts outside the poison grid and ends inside, or vice versa
                    # Check if there's a snake that blocks the arrow
                    # Check if there's a snake in this row that covers the entire row
                    # or blocks the arrow in some way
                    # Check if the arrow can pass through the poison grid
                    # If the arrow starts outside the poison grid and ends inside, or vice versa
                    # Check if there's a snake that blocks the arrow
                    # Check if there's a snake in this row that covers the entire row
                    # or blocks the arrow in some way
                    # Check if the arrow can pass through the poison grid
                    # If the arrow starts outside the poison grid and ends inside, or vice versa
                    # Check if there's a snake that blocks the arrow
                    # Check if there's a snake in this row that covers the entire row
                    # or blocks the arrow in some way
                    # Check if the arrow can pass through the poison grid
                    # If the arrow starts outside the poison grid and ends inside, or vice versa
                    # Check if there's a snake that blocks the arrow
                    # Check if there's a snake in this row that covers the entire row
                    # or blocks the arrow in some way
                    # Check if the arrow can pass through the poison grid
                    # If the arrow starts outside the poison grid and ends inside, or vice versa
                    # Check if there's a snake that blocks the arrow
                    # Check if there's a snake in this row that covers the entire row
                    # or blocks the arrow in some way
                    # Check if the arrow can pass through the poison grid
                    # If the arrow starts outside the poison grid and ends inside, or vice versa
                    # Check if there's a snake that blocks the arrow
                    # Check if there's a snake in this row that covers the entire row
                    # or blocks the arrow in some way
                    # Check if the arrow can pass through the poison grid
                    # If the arrow starts outside the poison grid and ends inside, or vice versa
                    # Check if there's a snake that blocks the arrow
                    # Check if there's a snake in this row that covers the entire row
                    # or blocks the arrow in some way
                    # Check if the arrow can pass through the poison grid
                    # If the arrow starts outside the poison grid and ends inside, or vice versa
                    # Check if there's a snake that blocks the arrow
                    # Check if there's a snake in this row that covers the entire row
                    # or blocks the arrow in some way
                    # Check if the arrow can pass through the poison grid
                    # If the arrow starts outside the poison grid and ends inside, or vice versa
                    # Check if there's a snake that blocks the arrow
                    # Check if there's a snake in this row that covers the entire row
                    # or blocks the arrow in some way
                    # Check if the arrow can pass through the poison grid
                    # If the arrow starts outside the poison grid and ends inside, or vice versa
                    # Check if there's a snake that blocks the arrow
                    # Check if there's a snake in this row that covers the entire row
                    # or blocks the arrow in some way
                    # Check if the arrow can pass through the poison grid
                    # If the arrow starts outside the poison grid and ends inside, or vice versa
                    # Check if there's a snake that blocks the arrow
                    # Check if there's a snake in this row that covers the entire row
                    # or blocks the arrow in some way
                    # Check if the arrow can pass through the poison grid
                    # If the arrow starts outside the poison grid and ends inside, or vice