import sys
import math

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    idx = 0
    N = int(data[idx])
    idx += 1
    M = int(data[idx])
    idx += 1
    
    board = []
    for _ in range(N):
        row = data[idx]
        idx += 1
        board.append(row)
    
    Q = int(data[idx])
    idx += 1
    c = list(map(int, data[idx:idx+Q]))
    
    # Precompute for each possible sub-board of size k x k
    # For each position (i, j), compute the number of inversions needed to make it a correct chessboard
    # There are two possible correct patterns: starting with 0 or 1
    # For each cell (i, j), compute the number of inversions needed for both patterns
    
    # Precompute for each cell (i, j) the number of inversions needed for both patterns
    # Pattern 0: (i + j) % 2 == 0 -> 0, else 1
    # Pattern 1: (i + j) % 2 == 0 -> 1, else 0
    
    # Create 2D arrays for the number of inversions needed for each pattern
    # For each cell (i, j), compute the number of inversions needed for pattern 0 and pattern 1
    # We'll store them in a 2D array for each pattern
    
    # Create a 2D array for pattern 0 and pattern 1
    # pattern0[i][j] = number of inversions needed to make (i, j) fit pattern 0
    # pattern1[i][j] = number of inversions needed to make (i, j) fit pattern 1
    
    pattern0 = [[0]*M for _ in range(N)]
    pattern1 = [[0]*M for _ in range(N)]
    
    for i in range(N):
        for j in range(M):
            if board[i][j] == '0':
                pattern0[i][j] = 0 if (i + j) % 2 == 0 else 1
                pattern1[i][j] = 1 if (i + j) % 2 == 0 else 0
            else:
                pattern0[i][j] = 1 if (i + j) % 2 == 0 else 0
                pattern1[i][j] = 0 if (i + j) % 2 == 0 else 1
    
    # Precompute for each possible sub-board size k, the minimum number of inversions needed for both patterns
    # We'll create 2D arrays for each possible k, but since k can be up to 200, we'll precompute for all possible k
    # For each possible k, we'll create a 2D array that stores the minimum number of inversions needed for a k x k sub-board starting at (i, j)
    
    # Precompute for each possible k, the minimum number of inversions needed for both patterns
    # We'll create two 2D arrays: min_inversions0 and min_inversions1
    # min_inversions0[i][j] = minimum number of inversions needed for a k x k sub-board starting at (i, j) with pattern 0
    # min_inversions1[i][j] = minimum number of inversions needed for a k x k sub-board starting at (i, j) with pattern 1
    
    # For each possible k, we'll compute these arrays
    # We'll precompute for all k from 1 to min(N, M)
    
    max_k = min(N, M)
    min_inversions0 = [[[0]*M for _ in range(N)] for _ in range(max_k+1)]
    min_inversions1 = [[[0]*M for _ in range(N)] for _ in range(max_k+1)]
    
    for k in range(1, max_k+1):
        for i in range(N - k + 1):
            for j in range(M - k + 1):
                # Compute the number of inversions needed for pattern 0
                inv0 = 0
                for x in range(k):
                    for y in range(k):
                        if (i + x + j + y) % 2 == 0:
                            if board[i + x][j + y] == '0':
                                inv0 += 0
                            else:
                                inv0 += 1
                        else:
                            if board[i + x][j + y] == '0':
                                inv0 += 1
                            else:
                                inv0 += 0
                # Compute the number of inversions needed for pattern 1
                inv1 = 0
                for x in range(k):
                    for y in range(k):
                        if (i + x + j + y) % 2 == 0:
                            if board[i + x][j + y] == '1':
                                inv1 += 0
                            else:
                                inv1 += 1
                        else:
                            if board[i + x][j + y] == '1':
                                inv1 += 0
                            else:
                                inv1 += 1
                # Store the minimum inversions for this k and position
                min_inversions0[k][i][j] = inv0
                min_inversions1[k][i][j] = inv1
    
    # For each query, find the maximum k such that either min_inversions0[k][i][j] <= c_i or min_inversions1[k][i][j] <= c_i for some (i, j)
    
    # Precompute for each k, the minimum number of inversions needed for both patterns across all possible sub-boards of size k
    # min_inversions0[k] = min(min_inversions0[k][i][j] for all i, j)
    # min_inversions1[k] = min(min_inversions1[k][i][j] for all i, j)
    
    min_inversions0_all = [0]*(max_k+1)
    min_inversions1_all = [0]*(max_k+1)
    
    for k in range(1, max_k+1):
        min0 = float('inf')
        min1 = float('inf')
        for i in range(N - k + 1):
            for j in range(M - k + 1):
                if min_inversions0[k][i][j] < min0:
                    min0 = min_inversions0[k][i][j]
                if min_inversions1[k][i][j] < min1:
                    min1 = min_inversions1[k][i][j]
        min_inversions0_all[k] = min0
        min_inversions1_all[k] = min1
    
    # For each query, find the maximum k such that either min_inversions0_all[k] <= c_i or min_inversions1_all[k] <= c_i
    
    for ci in c:
        max_k = 0
        for k in range(min(N, M), 0, -1):
            if min_inversions0_all[k] <= ci or min_inversions1_all[k] <= ci:
                max_k = k
                break
        print(max_k)
        
if __name__ == '__main__':
    solve()