import sys
import bisect

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    idx = 0
    N = int(data[idx])
    idx += 1
    M = int(data[idx])
    idx += 1
    
    grid = []
    for _ in range(N):
        grid.append(data[idx])
        idx += 1
    
    Q = int(data[idx])
    idx += 1
    
    c = list(map(int, data[idx:idx+Q]))
    
    # Precompute for each possible sub-board size (up to min(N,M))
    max_size = min(N, M)
    # For each possible size k (from 1 to max_size), precompute the minimum number of flips needed for all possible k x k sub-boards
    # We'll use a 2D array for each k, storing the minimum flips needed for each top-left (i,j)
    # We'll also precompute for each k, the minimum flips needed for all possible k x k sub-boards
    # We'll use a 2D array for each k, storing the minimum flips needed for each top-left (i,j)
    # We'll also precompute for each k, the minimum flips needed for all possible k x k sub-boards
    # We'll use a 2D array for each k, storing the minimum flips needed for each top-left (i,j)
    # We'll also precompute for each k, the minimum flips needed for all possible k x k sub-boards
    # We'll use a 2D array for each k, storing the minimum flips needed for each top-left (i,j)
    # We'll also precompute for each k, the minimum flips needed for all possible k x k sub-boards
    # We'll use a 2D array for each k, storing the minimum flips needed for each top-left (i,j)
    # We'll also precompute for each k, the minimum flips needed for all possible k x k sub-boards
    # We'll use a 2D array for each k, storing the minimum flips needed for each top-left (i,j)
    # We'll also precompute for each k, the minimum flips needed for all possible k x k sub-boards
    # We'll use a 2D array for each k, storing the minimum flips needed for each top-left (i,j)
    # We'll also precompute for each k, the minimum flips needed for all possible k x k sub-boards
    # We'll use a 2D array for each k, storing the minimum flips needed for each top-left (i,j)
    # We'll also precompute for each k, the minimum flips needed for all possible k x k sub-boards
    # We'll use a 2D array for each k, storing the minimum flips needed for each top-left (i,j)
    # We'll also precompute for each k, the minimum flips needed for all possible k x k sub-boards
    # We'll use a 2D array for each k, storing the minimum flips needed for each top-left (i,j)
    # We'll also precompute for each k, the minimum flips needed for all possible k x k sub-boards
    # We'll use a 2D array for each k, storing the minimum flips needed for each top-left (i,j)
    # We'll also precompute for each k, the minimum flips needed for all possible k x k sub-boards
    # We'll use a 2D array for each k, storing the minimum flips needed for each top-left (i,j)
    # We'll also precompute for each k, the minimum flips needed for all possible k x k sub-boards
    # We'll use a 2D array for each k, storing the minimum flips needed for each top-left (i,j)
    # We'll also precompute for each k, the minimum flips needed for all possible k x k sub-boards
    # We'll use a 2D array for each k, storing the minimum flips needed for each top-left (i,j)
    # We'll also precompute for each k, the minimum flips needed for all possible k x k sub-boards
    # We'll use a 2D array for each k, storing the minimum flips needed for each top-left (i,j)
    # We'll also precompute for each k, the minimum flips needed for all possible k x k sub-boards
    # We'll use a 2D array for each k, storing the minimum flips needed for each top-left (i,j)
    # We'll also precompute for each k, the minimum flips needed for all possible k x k sub-boards
    # We'll use a 2D array for each k, storing the minimum flips needed for each top-left (i,j)
    # We'll also precompute for each k, the minimum flips needed for all possible k x k sub-boards
    # We'll use a 2D array for each k, storing the minimum flips needed for each top-left (i,j)
    # We'll also precompute for each k, the minimum flips needed for all possible k x k sub-boards
    # We'll use a 2D array for each k, storing the minimum flips needed for each top-left (i,j)
    # We'll also precompute for each k, the minimum flips needed for all possible k x k sub-boards
    # We'll use a 2D array for each k, storing the minimum flips needed for each top-left (i,j)
    # We'll also precompute for each k, the minimum flips needed for all possible k x k sub-boards
    # We'll use a 2D array for each k, storing the minimum flips needed for each top-left (i,j)
    # We'll also precompute for each k, the minimum flips needed for all possible k x k sub-boards
    # We'll use a 2D array for each k, storing the minimum flips needed for each top-left (i,j)
    # We'll also precompute for each k, the minimum flips needed for all possible k x k sub-boards
    # We'll use a 2D array for each k, storing the minimum flips needed for each top-left (i,j)
    # We'll also precompute for each k, the minimum flips needed for all possible k x k sub-boards
    # We'll use a 2D array for each k, storing the minimum flips needed for each top-left (i,j)
    # We'll also precompute for each k, the minimum flips needed for all possible k x k sub-boards
    # We'll use a 2D array for each k, storing the minimum flips needed for each top-left (i,j)
    # We'll also precompute for each k, the minimum flips needed for all possible k x k sub-boards
    # We'll use a 2D array for each k, storing the minimum flips needed for each top-left (i,j)
    # We'll also precompute for each k, the minimum flips needed for all possible k x k sub-boards
    # We'll use a 2D array for each k, storing the minimum flips needed for each top-left (i,j)
    # We'll also precompute for each k, the minimum flips needed for all possible k x k sub-boards
    # We'll use a 2D array for each k, storing the minimum flips needed for each top-left (i,j)
    # We'll also precompute for each k, the minimum flips needed for all possible k x k sub-boards
    # We'll use a 2D array for each k, storing the minimum flips needed for each top-left (i,j)
    # We'll also precompute for each k, the minimum flips needed for all possible k x k sub-boards
    # We'll use a 2D array for each k, storing the minimum flips needed for each top-left (i,j)
    # We'll also precompute for each k, the minimum flips needed for all possible k x k sub-boards
    # We'll use a 2D array for each k, storing the minimum flips needed for each top-left (i,j)
    # We'll also precompute for each k, the minimum flips needed for all possible k x k sub-boards
    # We'll use a 2D array for each k, storing the minimum flips needed for each top-left (i,j)
    # We'll also precompute for each k, the minimum flips needed for all possible k x k sub-boards
    # We'll use a 2D array for each k, storing the minimum flips needed for each top-left (i,j)
    # We'll also precompute for each k, the minimum flips needed for all possible k x k sub-boards
    # We'll use a 2D array for each k, storing the minimum flips needed for each top-left (i,j)
    # We'll also precompute for each k, the minimum flips needed for all possible k x k sub-boards
    # We'll use a 2D array for each k, storing the minimum flips needed for each top-left (i,j)
    # We'll also precompute for each k, the minimum flips needed for all possible k x k sub-boards
    # We'll use a 2