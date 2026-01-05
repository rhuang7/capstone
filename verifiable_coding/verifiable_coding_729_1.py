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
        M = int(data[idx+1])
        idx += 2
        matrix = []
        for _ in range(N):
            row = data[idx]
            idx += 1
            matrix.append([int(c) for c in row])
        
        # Precompute row and column ORs
        row_or = [0] * N
        col_or = [0] * M
        for i in range(N):
            row_or[i] = 0
            for j in range(M):
                row_or[i] |= matrix[i][j]
        for j in range(M):
            col_or[j] = 0
            for i in range(N):
                col_or[j] |= matrix[i][j]
        
        # For each cell, compute min moves
        output = []
        for i in range(N):
            line = []
            for j in range(M):
                if matrix[i][j] == 1:
                    line.append(0)
                else:
                    # Check if it's possible
                    if row_or[i] == 0 and col_or[j] == 0:
                        line.append(-1)
                    else:
                        # Find min moves
                        # If row_or[i] is 1, then we can do 1 move (OR with row)
                        # If col_or[j] is 1, then we can do 1 move (OR with column)
                        # But we need to find the minimum between row and column
                        # Also, if both are 1, we can do 1 move (either row or column)
                        # If neither is 1, then we need to find a row and column to combine
                        # For example, if there is a row with 1 and a column with 1, then we can do 2 moves
                        # But if there is a row with 1, then we can do 1 move
                        # So the minimum is 1 if either row or column has 1
                        # Else, it's 2 if there is at least one row with 1 and one column with 1
                        # Else, it's -1
                        if row_or[i] == 1 or col_or[j] == 1:
                            line.append(1)
                        else:
                            # Check if there is at least one row with 1 and one column with 1
                            has_row = any(row_or[r] == 1 for r in range(N))
                            has_col = any(col_or[c] == 1 for c in range(M))
                            if has_row and has_col:
                                line.append(2)
                            else:
                                line.append(-1)
            output.append(' '.join(map(str, line)))
        
        results.append('\n'.join(output))
    
    print('\n'.join(results))