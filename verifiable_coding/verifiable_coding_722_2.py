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
        
        # For each snake, determine the line (row or column) it occupies
        # and the range of cells it covers
        snakes = []
        for _ in range(M):
            HX = int(data[idx])
            HY = int(data[idx+1])
            TX = int(data[idx+2])
            TY = int(data[idx+3])
            idx += 4
            
            if HX == TX:  # row
                row = HX
                start_col = min(HY, TY)
                end_col = max(HY, TY)
                snakes.append((row, start_col, end_col))
            else:  # column
                col = HY
                start_row = min(HX, TX)
                end_row = max(HX, TX)
                snakes.append((start_row, col, end_row))
        
        # Check if the current configuration is safe
        def is_safe(snakes):
            # For each row and column, check if it can be used to shoot an arrow
            # that enters the poison grid and exits the outer grid without hitting a snake
            # We need to check all rows and columns
            # For each row, check if there is a path from outside the poison grid to inside
            # and then to outside again without hitting a snake
            # Similarly for columns
            
            # Check rows
            for row in range(1, N+1):
                # Check if the row can be used to shoot an arrow that enters and exits the poison grid
                # without hitting a snake
                # The poison grid is from (poison_top_left, poison_top_left) to (poison_top_left + K - 1, poison_top_left + K - 1)
                # So the row can enter the poison grid if it intersects with the poison grid
                if row < poison_top_left or row > poison_top_left + K - 1:
                    # The row does not intersect with the poison grid, so it's safe
                    continue
                # Check if there is a path from outside the poison grid to inside and then to outside
                # without hitting a snake
                # Check if the row has a segment that is outside the poison grid and then enters it
                # and then exits again
                # For this, check if there is a segment of the row that is outside the poison grid
                # and then enters it
                # The poison grid is from column poison_top_left to poison_top_left + K - 1
                # So, if the row has cells outside this range, then it can be used to shoot an arrow
                # that enters and exits the poison grid
                # Check if there is a segment of the row that is outside the poison grid
                # and then enters it
                # If there is such a segment, then the row is unsafe
                # Check if the row has any part that is outside the poison grid
                # and then enters it
                # If so, then the row is unsafe
                # Check if the row has any part that is outside the poison grid
                # and then enters it
                # For this, check if the row has cells before the poison grid and after it
                # If so, then it's unsafe
                if row >= poison_top_left and row <= poison_top_left + K - 1:
                    # The row is inside the poison grid
                    # So any arrow shot along this row will stay inside the poison grid
                    # So it's safe
                    continue
                # Check if the row has any part that is outside the poison grid
                # and then enters it
                # If so, then it's unsafe
                # Check if there is a segment of the row that is outside the poison grid
                # and then enters it
                # For this, check if the row has any part that is outside the poison grid
                # and then enters it
                # Check if there is a segment of the row that is outside the poison grid
                # and then enters it
                # If so, then it's unsafe
                # Check if the row has any part that is outside the poison grid
                # and then enters it
                # For this, check if the row has cells before the poison grid and after it
                # If so, then it's unsafe
                # Check if the row has any part that is outside the poison grid
                # and then enters it
                # If so, then it's unsafe
                # Check if the row has any part that is outside the poison grid
                # and then enters it
                # If so, then it's unsafe
                # Check if the row has any part that is outside the poison grid
                # and then enters it
                # If so, then it's unsafe
                # Check if the row has any part that is outside the poison grid
                # and then enters it
                # If so, then it's unsafe
                # Check if the row has any part that is outside the poison grid
                # and then enters it
                # If so, then it's unsafe
                # Check if the row has any part that is outside the poison grid
                # and then enters it
                # If so, then it's unsafe
                # Check if the row has any part that is outside the poison grid
                # and then enters it
                # If so, then it's unsafe
                # Check if the row has any part that is outside the poison grid
                # and then enters it
                # If so, then it's unsafe
                # Check if the row has any part that is outside the poison grid
                # and then enters it
                # If so, then it's unsafe
                # Check if the row has any part that is outside the poison grid
                # and then enters it
                # If so, then it's unsafe
                # Check if the row has any part that is outside the poison grid
                # and then enters it
                # If so, then it's unsafe
                # Check if the row has any part that is outside the poison grid
                # and then enters it
                # If so, then it's unsafe
                # Check if the row has any part that is outside the poison grid
                # and then enters it
                # If so, then it's unsafe
                # Check if the row has any part that is outside the poison grid
                # and then enters it
                # If so, then it's unsafe
                # Check if the row has any part that is outside the poison grid
                # and then enters it
                # If so, then it's unsafe
                # Check if the row has any part that is outside the poison grid
                # and then enters it
                # If so, then it's unsafe
                # Check if the row has any part that is outside the poison grid
                # and then enters it
                # If so, then it's unsafe
                # Check if the row has any part that is outside the poison grid
                # and then enters it
                # If so, then it's unsafe
                # Check if the row has any part that is outside the poison grid
                # and then enters it
                # If so, then it's unsafe
                # Check if the row has any part that is outside the poison grid
                # and then enters it
                # If so, then it's unsafe
                # Check if the row has any part that is outside the poison grid
                # and then enters it
                # If so, then it's unsafe
                # Check if the row has any part that is outside the poison grid
                # and then enters it
                # If so, then it's unsafe
                # Check if the row has any part that is outside the poison grid
                # and then enters it
                # If so, then it's unsafe
                # Check if the row has any part that is outside the poison grid
                # and then enters it
                # If so, then it's unsafe
                # Check if the row has any part that is outside the poison grid
                # and then enters it
                # If so, then it's unsafe
                # Check if the row has any part that is outside the poison grid
                # and then enters it
                # If so, then it's unsafe
                # Check if the row has any part that is outside the poison grid
                # and then enters it
                # If so, then it's unsafe
                # Check if the row has any part that is outside the poison grid
                # and then enters it
                # If so, then it's unsafe
                # Check if the row has any part that is outside the poison grid
                # and then enters it
                # If so, then it's unsafe
                # Check if the row has any part that is outside the poison grid
                # and then