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
        
        # Precompute for rows
        row_ones = [0] * N
        for i in range(N):
            row_ones[i] = sum(matrix[i])
        
        # Precompute for columns
        col_ones = [0] * M
        for j in range(M):
            col_ones[j] = sum(matrix[i][j] for i in range(N))
        
        # For each cell, compute min moves
        output = []
        for i in range(N):
            line = []
            for j in range(M):
                if matrix[i][j] == 1:
                    line.append(0)
                else:
                    # Check if there's at least one 1 in the row or column
                    if row_ones[i] == 0 and col_ones[j] == 0:
                        line.append(-1)
                    else:
                        # Minimum moves: either 1 row operation or 1 column operation
                        line.append(1)
            output.append(line)
        
        # Convert to string and add to results
        results.append('\n'.join(' '.join(map(str, row)) for row in output))
    
    print('\n'.join(results))