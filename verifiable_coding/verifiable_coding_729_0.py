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
        for i in range(N):
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
                    row_has_one = row_ones[i] > 0
                    col_has_one = col_ones[j] > 0
                    if not row_has_one and not col_has_one:
                        res.append(-1)
                    else:
                        if row_has_one or col_has_one:
                            res.append(1)
                        else:
                            res.append(-1)
        
        results.append(' '.join(map(str, res)))
    
    print('\n'.join(results))