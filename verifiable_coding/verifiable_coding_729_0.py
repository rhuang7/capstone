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
                    min_moves = math.inf
                    # Check if it's possible to make it 1
                    possible = False
                    # Check if there's at least one 1 in the row or column
                    if any(matrix[i][k] == 1 for k in range(M)):
                        possible = True
                    if any(matrix[k][j] == 1 for k in range(N)):
                        possible = True
                    if not possible:
                        res.append(-1)
                    else:
                        # Find the minimum number of moves
                        # For row: need to find the minimum number of other rows to OR with
                        # For column: need to find the minimum number of other columns to OR with
                        # The minimum moves is the minimum between row and column
                        row_min = math.inf
                        col_min = math.inf
                        # Find the minimum row moves
                        for k in range(N):
                            if matrix[k][j] == 1:
                                row_min = min(row_min, 1)
                        # Find the minimum column moves
                        for k in range(M):
                            if matrix[i][k] == 1:
                                col_min = min(col_min, 1)
                        # The minimum moves is the minimum between row and column
                        min_moves = min(row_min, col_min)
                        res.append(min_moves)
        results.append(' '.join(map(str, res)))
    
    print('\n'.join(results))