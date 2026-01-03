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
        
        # Calculate the top-left corner of the poison square
        poison_top_left = ((N - K) // 2 + 1, (N - K) // 2 + 1)
        
        # For each snake, determine the row or column it occupies
        # and whether it blocks any potential arrow path
        # We'll track which rows and columns are blocked
        blocked_rows = set()
        blocked_cols = set()
        
        for _ in range(M):
            HX = int(data[idx])
            HY = int(data[idx+1])
            TX = int(data[idx+2])
            TY = int(data[idx+3])
            idx += 4
            
            if HX == TX:  # Same row
                row = HX
                start = min(HY, TY)
                end = max(HY, TY)
                for y in range(start, end + 1):
                    if poison_top_left[0] <= row <= poison_top_left[0] + K - 1 and poison_top_left[1] <= y <= poison_top_left[1] + K - 1:
                        # This snake blocks a potential arrow path through the poison square
                        blocked_rows.add(row)
                    else:
                        # This snake is outside the poison square, so it doesn't block any arrow path
                        pass
            else:  # Same column
                col = HY
                start = min(HX, TX)
                end = max(HX, TX)
                for x in range(start, end + 1):
                    if poison_top_left[0] <= x <= poison_top_left[0] + K - 1 and poison_top_left[1] <= col <= poison_top_left[1] + K - 1:
                        # This snake blocks a potential arrow path through the poison square
                        blocked_cols.add(col)
                    else:
                        # This snake is outside the poison square, so it doesn't block any arrow path
                        pass
        
        # Check if the configuration is safe
        # An arrow can enter the poison square and exit the grid if it doesn't hit a snake
        # So, for every row that could potentially enter the poison square, it must be blocked
        # Similarly for every column that could potentially enter the poison square
        
        # Check all rows that could potentially enter the poison square
        for row in range(poison_top_left[0], poison_top_left[0] + K):
            if row not in blocked_rows:
                # This row is not blocked, so an arrow can enter the poison square and exit without hitting a snake
                results.append(-1)
                break
        else:
            # Check all columns that could potentially enter the poison square
            for col in range(poison_top_left[1], poison_top_left[1] + K):
                if col not in blocked_cols:
                    # This column is not blocked, so an arrow can enter the poison square and exit without hitting a snake
                    results.append(-1)
                    break
            else:
                # All rows and columns are blocked, so the configuration is safe
                # Count the number of snakes that are blocking the poison square
                # We need to count how many snakes are blocking the poison square
                # We'll do this by checking each snake again
                count = 0
                for _ in range(M):
                    HX = int(data[idx])
                    HY = int(data[idx+1])
                    TX = int(data[idx+2])
                    TY = int(data[idx+3])
                    idx += 4
                    
                    if HX == TX:  # Same row
                        row = HX
                        start = min(HY, TY)
                        end = max(HY, TY)
                        for y in range(start, end + 1):
                            if poison_top_left[0] <= row <= poison_top_left[0] + K - 1 and poison_top_left[1] <= y <= poison_top_left[1] + K - 1:
                                count += 1
                                break
                    else:  # Same column
                        col = HY
                        start = min(HX, TX)
                        end = max(HX, TX)
                        for x in range(start, end + 1):
                            if poison_top_left[0] <= x <= poison_top_left[0] + K - 1 and poison_top_left[1] <= col <= poison_top_left[1] + K - 1:
                                count += 1
                                break
                results.append(count)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()