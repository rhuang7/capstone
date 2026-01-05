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
            matrix.append([int(c) for c in row])
            idx += 1
        
        # Precompute for rows and columns
        row_or = [0] * N
        col_or = [0] * M
        
        # Compute row ORs
        for i in range(N):
            row_or[i] = 0
            for j in range(M):
                row_or[i] |= matrix[i][j]
        
        # Compute column ORs
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
                    # Check if it's possible to make it 1
                    if row_or[i] == 0 and col_or[j] == 0:
                        line.append(-1)
                    else:
                        # Find the minimum number of moves
                        # If row has 1, can be done in 1 move (OR with row)
                        # If column has 1, can be done in 1 move (OR with column)
                        # If neither, then need to find a row or column with 1 and OR with it
                        # But since we can choose any row or column, the minimum is 1
                        # Because if row_or[i] or col_or[j] is 1, then it can be done in 1 move
                        # If both are 0, then it's impossible
                        # So the answer is 1 if either row_or[i] or col_or[j] is 1
                        # Otherwise -1
                        if row_or[i] == 0 and col_or[j] == 0:
                            line.append(-1)
                        else:
                            line.append(1)
            output.append(' '.join(map(str, line)))
        
        results.append('\n'.join(output))
    
    print('\n'.join(results))