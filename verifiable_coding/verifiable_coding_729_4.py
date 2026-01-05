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
        
        # For each cell (i,j)
        output = []
        for i in range(N):
            line = []
            for j in range(M):
                if matrix[i][j] == 1:
                    line.append(0)
                else:
                    # Check if there's a row with 1 in column j
                    has_row_1 = any(matrix[r][j] == 1 for r in range(N))
                    # Check if there's a column with 1 in row i
                    has_col_1 = any(matrix[i][c] == 1 for c in range(M))
                    
                    if not has_row_1 and not has_col_1:
                        line.append(-1)
                    else:
                        # Minimum moves: min between row and column
                        min_moves = min(
                            math.ceil(math.log2(row_ones[i] + 1)) if row_ones[i] > 0 else float('inf'),
                            math.ceil(math.log2(col_ones[j] + 1)) if col_ones[j] > 0 else float('inf')
                        )
                        line.append(min_moves)
            output.append(' '.join(map(str, line)))
        
        results.append('\n'.join(output))
    
    print('\n'.join(results))