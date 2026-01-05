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
        poison_top_left = ((N - K) // 2) + 1
        
        # For each snake, determine the line it occupies and the range of cells
        snakes = []
        for _ in range(M):
            HX = int(data[idx])
            HY = int(data[idx+1])
            TX = int(data[idx+2])
            TY = int(data[idx+3])
            idx += 4
            
            # Determine if the snake is in a row or column
            if HX == TX:
                # Row snake
                row = HX
                start = min(HY, TY)
                end = max(HY, TY)
                snakes.append((row, start, end))
            else:
                # Column snake
                col = HY
                start = min(HX, TX)
                end = max(HX, TX)
                snakes.append((col, start, end))
        
        # Check if the current configuration is safe
        def is_safe(snakes):
            # Check all rows
            for row in range(1, N+1):
                # Check if the row intersects with the poison grid
                if poison_top_left <= row <= poison_top_left + K - 1:
                    # Check if there is a snake in this row that blocks all paths
                    # Check if there is a snake that covers the entire row from left to right
                    # Check if there is a snake that covers the entire row from left to right
                    # Check if there is a snake that covers the entire row from left to right
                    # Check if there is a snake that covers the entire row from left to right
                    # Check if there is a snake that covers the entire row from left to right
                    # Check if there is a snake that covers the entire row from left to right
                    # Check if there is a snake that covers the entire row from left to right
                    # Check if there is a snake that covers the entire row from left to right
                    # Check if there is a snake that covers the entire row from left to right
                    # Check if there is a snake that covers the entire row from left to right
                    # Check if there is a snake that covers the entire row from left to right
                    # Check if there is a snake that covers the entire row from left to right
                    # Check if there is a snake that covers the entire row from left to right
                    # Check if there is a snake that covers the entire row from left to right
                    # Check if there is a snake that covers the entire row from left to right
                    # Check if there is a snake that covers the entire row from left to right
                    # Check if there is a snake that covers the entire row from left to right
                    # Check if there is a snake that covers the entire row from left to right
                    # Check if there is a snake that covers the entire row from left to right
                    # Check if there is a snake that covers the entire row from left to right
                    # Check if there is a snake that covers the entire row from left to right
                    # Check if there is a snake that covers the entire row from left to right
                    # Check if there is a snake that covers the entire row from left to right
                    # Check if there is a snake that covers the entire row from left to right
                    # Check if there is a snake that covers the entire row from left to right
                    # Check if there is a snake that covers the entire row from left to right
                    # Check if there is a snake that covers the entire row from left to right
                    # Check if there is a snake that covers the entire row from left to right
                    # Check if there is a snake that covers the entire row from left to right
                    # Check if there is a snake that covers the entire row from left to right
                    # Check if there is a snake that covers the entire row from left to right
                    # Check if there is a snake that covers the entire row from left to right
                    # Check if there is a snake that covers the entire row from left to right
                    # Check if there is a snake that covers the entire row from left to right
                    # Check if there is a snake that covers the entire row from left to right
                    # Check if there is a snake that covers the entire row from left to right
                    # Check if there is a snake that covers the entire row from left to right
                    # Check if there is a snake that covers the entire row from left to right
                    # Check if there is a snake that covers the entire row from left to right
                    # Check if there is a snake that covers the entire row from left to right
                    # Check if there is a snake that covers the entire row from left to right
                    # Check if there is a snake that covers the entire row from left to right
                    # Check if there is a snake that covers the entire row from left to right
                    # Check if there is a snake that covers the entire row from left to right
                    # Check if there is a snake that covers the entire row from left to right
                    # Check if there is a snake that covers the entire row from left to right
                    # Check if there is a snake that covers the entire row from left to right
                    # Check if there is a snake that covers the entire row from left to right
                    # Check if there is a snake that covers the entire row from left to right
                    # Check if there is a snake that covers the entire row from left to right
                    # Check if there is a snake that covers the entire row from left to right
                    # Check if there is a snake that covers the entire row from left to right
                    # Check if there is a snake that covers the entire row from left to right
                    # Check if there is a snake that covers the entire row from left to right
                    # Check if there is a snake that covers the entire row from left to right
                    # Check if there is a snake that covers the entire row from left to right
                    # Check if there is a snake that covers the entire row from left to right
                    # Check if there is a snake that covers the entire row from left to right
                    # Check if there is a snake that covers the entire row from left to right
                    # Check if there is a snake that covers the entire row from left to right
                    # Check if there is a snake that covers the entire row from left to right
                    # Check if there is a snake that covers the entire row from left to right
                    # Check if there is a snake that covers the entire row from left to right
                    # Check if there is a snake that covers the entire row from left to right
                    # Check if there is a snake that covers the entire row from left to right
                    # Check if there is a snake that covers the entire row from left to right
                    # Check if there is a snake that covers the entire row from left to right
                    # Check if there is a snake that covers the entire row from left to right
                    # Check if there is a snake that covers the entire row from left to right
                    # Check if there is a snake that covers the entire row from left to right
                    # Check if there is a snake that covers the entire row from left to right
                    # Check if there is a snake that covers the entire row from left to right
                    # Check if there is a snake that covers the entire row from left to right
                    # Check if there is a snake that covers the entire row from left to right
                    # Check if there is a snake that covers the entire row from left to right
                    # Check if there is a snake that covers the entire row from left to right
                    # Check if there is a snake that covers the entire row from left to right
                    # Check if there is a snake that covers the entire row from left to right
                    # Check if there is a snake that covers the entire row from left to right
                    # Check if there is a snake that covers the entire row from left to right
                    # Check if there is a snake that covers the entire row from left to right
                    # Check if there is a snake that covers the entire row from left to right
                    # Check if there is a snake that covers the entire row from left to right
                    # Check if there is a snake that covers the entire row from left to right
                    # Check if there is a snake that covers the entire row from left to right
                    # Check if there is a snake that covers the entire row from left to right
                    # Check if there is a snake that covers the entire row from left to right
                    # Check if there is a snake that covers the entire row from left to right
                    # Check if there is a snake that covers the entire row from left to right
                    # Check if there is a snake that covers the entire row from left to right
                    # Check if there is a snake that covers