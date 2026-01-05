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
        
        row_ones = [0] * N
        col_ones = [0] * M
        
        for i in range(N):
            row_ones[i] = sum(matrix[i])
        
        for j in range(M):
            col_ones[j] = sum(matrix[i][j] for i in range(N))
        
        res = []
        for i in range(N):
            for j in range(M):
                if matrix[i][j] == 1:
                    res.append(0)
                else:
                    min_moves = float('inf')
                    # Check if it's possible to make it 1
                    possible = False
                    # Check if there's at least one 1 in the same row or column
                    if any(matrix[i][k] == 1 for k in range(M)):
                        possible = True
                    if any(matrix[k][j] == 1 for k in range(N)):
                        possible = True
                    if not possible:
                        res.append(-1)
                    else:
                        # Calculate minimum moves
                        # If there's at least one 1 in the row, we can use that row
                        if any(matrix[i][k] == 1 for k in range(M)):
                            # We can use the row to make this cell 1 in 1 move
                            min_moves = 1
                        else:
                            # We need to use a column with 1
                            if any(matrix[k][j] == 1 for k in range(N)):
                                min_moves = 1
                            else:
                                # We need to use a row with 1 and a column with 1
                                # So we need 2 moves
                                min_moves = 2
                        res.append(min_moves)
        results.append(' '.join(map(str, res)))
    
    print('\n'.join(results))