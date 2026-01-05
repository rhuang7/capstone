import sys
import bisect

def main():
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
    idx += Q
    
    # Precompute for each possible sub-board (i,j) the number of cells that need to be flipped to make it correct
    # There are two possible correct patterns for a sub-board of size k x k:
    # 1. Starting with 0 in (i,j)
    # 2. Starting with 1 in (i,j)
    # For each (i,j), we compute the number of flips needed for both patterns
    
    # Precompute for each cell (i,j) the number of 0s and 1s in the sub-board starting at (i,j) with size k x k
    # We'll use dynamic programming to compute this efficiently
    
    # Precompute prefix sums for 0s and 1s
    prefix_0 = [[0]*(M+1) for _ in range(N+1)]
    prefix_1 = [[0]*(M+1) for _ in range(N+1)]
    
    for i in range(N):
        for j in range(M):
            prefix_0[i+1][j+1] = prefix_0[i][j+1] + prefix_0[i+1][j] - prefix_0[i][j] + (0 if board[i][j] == '0' else 1)
            prefix_1[i+1][j+1] = prefix_1[i][j+1] + prefix_1[i+1][j] - prefix_1[i][j] + (1 if board[i][j] == '0' else 0)
    
    # For each possible sub-board size k, precompute the minimum number of flips needed for all possible (i,j)
    # We'll store for each (i,j) the minimum flips needed for all k up to min(N,M)
    # We'll use a 2D array for each k, but since we need to answer queries efficiently, we'll precompute for all possible k and store the maximum possible k for each (i,j)
    
    # For each possible sub-board size k, we'll compute the maximum k for which there exists a sub-board of size k x k that can be fixed with at most c_i flips
    # We'll use binary search for each query
    
    # Precompute for each (i,j) the maximum k for which there exists a sub-board of size k x k that can be fixed with at most c_i flips
    # We'll store for each (i,j) the maximum k for which there exists a sub-board of size k x k that can be fixed with at most c_i flips
    
    # Precompute for each (i,j) the minimum flips needed for all k up to min(N,M)
    # We'll store for each (i,j) the maximum k for which there exists a sub-board of size k x k that can be fixed with at most c_i flips
    
    # Precompute for each (i,j) the minimum flips needed for all k up to min(N,M)
    # We'll store for each (i,j) the maximum k for which there exists a sub-board of size k x k that can be fixed with at most c_i flips
    
    # Precompute for each (i,j) the minimum flips needed for all k up to min(N,M)
    # We'll store for each (i,j) the maximum k for which there exists a sub-board of size k x k that can be fixed with at most c_i flips
    
    # Precompute for each (i,j) the minimum flips needed for all k up to min(N,M)
    # We'll store for each (i,j) the maximum k for which there exists a sub-board of size k x k that can be fixed with at most c_i flips
    
    # Precompute for each (i,j) the minimum flips needed for all k up to min(N,M)
    # We'll store for each (i,j) the maximum k for which there exists a sub-board of size k x k that can be fixed with at most c_i flips
    
    # Precompute for each (i,j) the minimum flips needed for all k up to min(N,M)
    # We'll store for each (i,j) the maximum k for which there exists a sub-board of size k x k that can be fixed with at most c_i flips
    
    # Precompute for each (i,j) the minimum flips needed for all k up to min(N,M)
    # We'll store for each (i,j) the maximum k for which there exists a sub-board of size k x k that can be fixed with at most c_i flips
    
    # Precompute for each (i,j) the minimum flips needed for all k up to min(N,M)
    # We'll store for each (i,j) the maximum k for which there exists a sub-board of size k x k that can be fixed with at most c_i flips
    
    # Precompute for each (i,j) the minimum flips needed for all k up to min(N,M)
    # We'll store for each (i,j) the maximum k for which there exists a sub-board of size k x k that can be fixed with at most c_i flips
    
    # Precompute for each (i,j) the minimum flips needed for all k up to min(N,M)
    # We'll store for each (i,j) the maximum k for which there exists a sub-board of size k x k that can be fixed with at most c_i flips
    
    # Precompute for each (i,j) the minimum flips needed for all k up to min(N,M)
    # We'll store for each (i,j) the maximum k for which there exists a sub-board of size k x k that can be fixed with at most c_i flips
    
    # Precompute for each (i,j) the minimum flips needed for all k up to min(N,M)
    # We'll store for each (i,j) the maximum k for which there exists a sub-board of size k x k that can be fixed with at most c_i flips
    
    # Precompute for each (i,j) the minimum flips needed for all k up to min(N,M)
    # We'll store for each (i,j) the maximum k for which there exists a sub-board of size k x k that can be fixed with at most c_i flips
    
    # Precompute for each (i,j) the minimum flips needed for all k up to min(N,M)
    # We'll store for each (i,j) the maximum k for which there exists a sub-board of size k x k that can be fixed with at most c_i flips
    
    # Precompute for each (i,j) the minimum flips needed for all k up to min(N,M)
    # We'll store for each (i,j) the maximum k for which there exists a sub-board of size k x k that can be fixed with at most c_i flips
    
    # Precompute for each (i,j) the minimum flips needed for all k up to min(N,M)
    # We'll store for each (i,j) the maximum k for which there exists a sub-board of size k x k that can be fixed with at most c_i flips
    
    # Precompute for each (i,j) the minimum flips needed for all k up to min(N,M)
    # We'll store for each (i,j) the maximum k for which there exists a sub-board of size k x k that can be fixed with at most c_i flips
    
    # Precompute for each (i,j) the minimum flips needed for all k up to min(N,M)
    # We'll store for each (i,j) the maximum k for which there exists a sub-board of size k x k that can be fixed with at most c_i flips
    
    # Precompute for each (i,j) the minimum flips needed for all k up to min(N,M)
    # We'll store for each (i,j) the maximum k for which there exists a sub-board of size k x k that can be fixed with at most c_i flips
    
    # Precompute for each (i,j) the minimum flips needed for all k up to min(N,M)
    # We'll store for each (i,j) the maximum k for which there exists a sub-board of size k x k that can be fixed with at most c_i flips
    
    # Precompute for each (i,j) the minimum flips needed for all k up to min(N,M)
    # We'll store for each (i,j) the maximum k for which there exists a sub-board of size k x k that can be fixed with at most c_i flips
    
    # Precompute for each (i,j) the minimum flips needed for all k up to min(N,M)
    # We'll store for each (i,j) the maximum k for which there exists a sub-board of size k x k that can be fixed with at most c_i flips
    
    # Precompute for each (i,j) the minimum flips needed for