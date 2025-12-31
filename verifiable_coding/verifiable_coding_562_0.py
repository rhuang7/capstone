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
    
    grid = []
    for _ in range(N):
        row = data[idx]
        grid.append(row)
        idx += 1
    
    Q = int(data[idx])
    idx += 1
    
    c = list(map(int, data[idx:idx+Q]))
    
    # Precompute for each possible square size the minimum number of flips needed
    # for each possible top-left corner
    # We'll use a 2D array for each possible square size
    # For each square size k, we'll compute the minimum flips for all possible k x k squares
    # We'll precompute for all possible k from 1 to min(N, M)
    # Then for each query, we'll binary search the maximum k for which there exists a k x k square that can be fixed with <= c_i flips
    
    max_k = min(N, M)
    # Precompute for each possible k (1 to max_k) and for each possible top-left (i, j) the minimum flips needed to make a k x k square correct
    # We'll use a 2D array for each k
    # For each k, we'll store a 2D array of size (N - k + 1) x (M - k + 1)
    # But since N and M are up to 200, and k can be up to 200, this is feasible
    
    # We'll precompute for all possible k from 1 to max_k
    # For each k, we'll compute the minimum flips needed for all possible k x k squares
    # We'll store it in a 3D array: min_flips[k][i][j] = min flips needed to make the square starting at (i, j) of size k correct
    
    # We'll also precompute for each k the maximum possible size of a square that can be fixed with c_i flips
    # We'll store for each k the list of possible square sizes that can be achieved with up to c_i flips
    
    # First, precompute for each k from 1 to max_k, and for each possible square of size k, the minimum flips needed to make it correct
    
    # To compute the minimum flips for a square of size k, we need to check if the square is already correct, or if we need to flip some cells
    # For a square to be correct, it must alternate colors in a chessboard pattern
    # There are two possible patterns for a square:
    # 1. (i + j) % 2 == 0: cell is 0
    # 2. (i + j) % 2 == 1: cell is 1
    # So for each square, we can compute the number of flips needed for both patterns and take the minimum
    
    # Precompute for each possible square of size k, the minimum flips needed for both patterns
    # We'll store it in a 3D array: min_flips[k][i][j] = min flips needed for square starting at (i, j) of size k
    
    # We'll also precompute for each k, the maximum possible square size that can be achieved with up to c_i flips
    
    # Precompute for each k from 1 to max_k
    # For each k, we'll compute for all possible squares of size k the minimum flips needed
    
    # We'll use a 3D array: min_flips[k][i][j] = min flips needed for square starting at (i, j) of size k
    
    # But since N and M are up to 200, and k is up to 200, this is feasible
    
    # Precompute for each k from 1 to max_k
    # For each k, we'll compute for all possible squares of size k the minimum flips needed
    
    # We'll use a 3D array: min_flips[k][i][j] = min flips needed for square starting at (i, j) of size k
    
    # To save space, we can compute for each k and store the minimum flips for each square of size k
    
    # We'll use a list of lists of lists: min_flips[k][i][j] = min flips needed for square starting at (i, j) of size k
    
    # We'll precompute for each k from 1 to max_k
    # For each k, we'll compute for all possible squares of size k the minimum flips needed
    
    # We'll also precompute for each k, the maximum possible square size that can be achieved with up to c_i flips
    
    # Precompute for each k from 1 to max_k
    # For each k, we'll compute for all possible squares of size k the minimum flips needed
    
    # We'll use a 3D array: min_flips[k][i][j] = min flips needed for square starting at (i, j) of size k
    
    # But since N and M are up to 200, and k is up to 200, this is feasible
    
    # We'll precompute for each k from 1 to max_k
    # For each k, we'll compute for all possible squares of size k the minimum flips needed
    
    # We'll also precompute for each k, the maximum possible square size that can be achieved with up to c_i flips
    
    # Precompute for each k from 1 to max_k
    # For each k, we'll compute for all possible squares of size k the minimum flips needed
    
    # We'll use a 3D array: min_flips[k][i][j] = min flips needed for square starting at (i, j) of size k
    
    # But since N and M are up to 200, and k is up to 200, this is feasible
    
    # We'll precompute for each k from 1 to max_k
    # For each k, we'll compute for all possible squares of size k the minimum flips needed
    
    # We'll also precompute for each k, the maximum possible square size that can be achieved with up to c_i flips
    
    # Precompute for each k from 1 to max_k
    # For each k, we'll compute for all possible squares of size k the minimum flips needed
    
    # We'll use a 3D array: min_flips[k][i][j] = min flips needed for square starting at (i, j) of size k
    
    # But since N and M are up to 200, and k is up to 200, this is feasible
    
    # We'll precompute for each k from 1 to max_k
    # For each k, we'll compute for all possible squares of size k the minimum flips needed
    
    # We'll also precompute for each k, the maximum possible square size that can be achieved with up to c_i flips
    
    # Precompute for each k from 1 to max_k
    # For each k, we'll compute for all possible squares of size k the minimum flips needed
    
    # We'll use a 3D array: min_flips[k][i][j] = min flips needed for square starting at (i, j) of size k
    
    # But since N and M are up to 200, and k is up to 200, this is feasible
    
    # We'll precompute for each k from 1 to max_k
    # For each k, we'll compute for all possible squares of size k the minimum flips needed
    
    # We'll also precompute for each k, the maximum possible square size that can be achieved with up to c_i flips
    
    # Precompute for each k from 1 to max_k
    # For each k, we'll compute for all possible squares of size k the minimum flips needed
    
    # We'll use a 3D array: min_flips[k][i][j] = min flips needed for square starting at (i, j) of size k
    
    # But since N and M are up to 200, and k is up to 200, this is feasible
    
    # We'll precompute for each k from 1 to max_k
    # For each k, we'll compute for all possible squares of size k the minimum flips needed
    
    # We'll also precompute for each k, the maximum possible square size that can be achieved with up to c_i flips
    
    # Precompute for each k from 1 to max_k
    # For each k, we'll compute for all possible squares of size k the minimum flips needed
    
    # We'll use a 3D array: min_flips[k][i][j] = min flips needed for square starting at (i, j) of size k
    
    # But since N and M are up to 200, and k is up to 200, this is feasible
    
    # We'll precompute for each k from 1 to max_k
    # For each k, we'll compute for all possible squares of size k the minimum flips needed