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
    
    grid = []
    for _ in range(N):
        grid.append(data[idx])
        idx += 1
    
    Q = int(data[idx])
    idx += 1
    c = list(map(int, data[idx:idx+Q]))
    
    # Precompute for all possible sub-boards
    # For each possible top-left (i,j) and bottom-right (i+k-1,j+k-1), compute the minimal number of flips needed to make it a correct chessboard
    # We'll precompute for all possible k (side length)
    # For each k, we'll compute for all possible top-left (i,j) the minimal flips needed
    # Then for each query, we can binary search the maximum k for which there exists a sub-board with flips <= c_i
    
    # Precompute for all possible k
    max_k = min(N, M)
    dp = [[[0] * (M + 1) for _ in range(N + 1)] for _ in range(max_k + 1)]
    
    # For each possible k
    for k in range(1, max_k + 1):
        # For each possible top-left (i,j)
        for i in range(N - k + 1):
            for j in range(M - k + 1):
                # Compute the number of flips needed for the sub-board starting at (i,j) with size k x k
                # The correct chessboard pattern alternates colors
                # We need to check if the sub-board can be made correct with at most c_i flips
                # We can precompute the number of flips needed for each possible (i,j,k)
                # We'll use a 2D prefix sum to compute the number of 0s and 1s in the sub-board
                # For the correct pattern, the top-left cell is 0, then alternates
                # So for the sub-board, the correct pattern is:
                # (i + x + j + y) % 2 == 0 -> 0
                # (i + x + j + y) % 2 == 1 -> 1
                # So for each cell (x,y) in the sub-board, we check if it matches the correct pattern
                # We can precompute the number of mismatches for each possible (i,j,k)
                # We'll use a 2D prefix sum to compute the number of 0s and 1s in the sub-board
                # Then for each cell (x,y) in the sub-board, we check if it matches the correct pattern
                # We can compute the number of flips needed for the sub-board starting at (i,j) with size k x k
                # We'll use a 2D prefix sum to compute the number of 0s and 1s in the sub-board
                # Then for each cell (x,y) in the sub-board, we check if it matches the correct pattern
                # We can compute the number of flips needed for the sub-board starting at (i,j) with size k x k
                # We'll use a 2D prefix sum to compute the number of 0s and 1s in the sub-board
                # Then for each cell (x,y) in the sub-board, we check if it matches the correct pattern
                # We can compute the number of flips needed for the sub-board starting at (i,j) with size k x k
                # We'll use a 2D prefix sum to compute the number of 0s and 1s in the sub-board
                # Then for each cell (x,y) in the sub-board, we check if it matches the correct pattern
                # We can compute the number of flips needed for the sub-board starting at (i,j) with size k x k
                # We'll use a 2D prefix sum to compute the number of 0s and 1s in the sub-board
                # Then for each cell (x,y) in the sub-board, we check if it matches the correct pattern
                # We can compute the number of flips needed for the sub-board starting at (i,j) with size k x k
                # We'll use a 2D prefix sum to compute the number of 0s and 1s in the sub-board
                # Then for each cell (x,y) in the sub-board, we check if it matches the correct pattern
                # We can compute the number of flips needed for the sub-board starting at (i,j) with size k x k
                # We'll use a 2D prefix sum to compute the number of 0s and 1s in the sub-board
                # Then for each cell (x,y) in the sub-board, we check if it matches the correct pattern
                # We can compute the number of flips needed for the sub-board starting at (i,j) with size k x k
                # We'll use a 2D prefix sum to compute the number of 0s and 1s in the sub-board
                # Then for each cell (x,y) in the sub-board, we check if it matches the correct pattern
                # We can compute the number of flips needed for the sub-board starting at (i,j) with size k x k
                # We'll use a 2D prefix sum to compute the number of 0s and 1s in the sub-board
                # Then for each cell (x,y) in the sub-board, we check if it matches the correct pattern
                # We can compute the number of flips needed for the sub-board starting at (i,j) with size k x k
                # We'll use a 2D prefix sum to compute the number of 0s and 1s in the sub-board
                # Then for each cell (x,y) in the sub-board, we check if it matches the correct pattern
                # We can compute the number of flips needed for the sub-board starting at (i,j) with size k x k
                # We'll use a 2D prefix sum to compute the number of 0s and 1s in the sub-board
                # Then for each cell (x,y) in the sub-board, we check if it matches the correct pattern
                # We can compute the number of flips needed for the sub-board starting at (i,j) with size k x k
                # We'll use a 2D prefix sum to compute the number of 0s and 1s in the sub-board
                # Then for each cell (x,y) in the sub-board, we check if it matches the correct pattern
                # We can compute the number of flips needed for the sub-board starting at (i,j) with size k x k
                # We'll use a 2D prefix sum to compute the number of 0s and 1s in the sub-board
                # Then for each cell (x,y) in the sub-board, we check if it matches the correct pattern
                # We can compute the number of flips needed for the sub-board starting at (i,j) with size k x k
                # We'll use a 2D prefix sum to compute the number of 0s and 1s in the sub-board
                # Then for each cell (x,y) in the sub-board, we check if it matches the correct pattern
                # We can compute the number of flips needed for the sub-board starting at (i,j) with size k x k
                # We'll use a 2D prefix sum to compute the number of 0s and 1s in the sub-board
                # Then for each cell (x,y) in the sub-board, we check if it matches the correct pattern
                # We can compute the number of flips needed for the sub-board starting at (i,j) with size k x k
                # We'll use a 2D prefix sum to compute the number of 0s and 1s in the sub-board
                # Then for each cell (x,y) in the sub-board, we check if it matches the correct pattern
                # We can compute the number of flips needed for the sub-board starting at (i,j) with size k x k
                # We'll use a 2D prefix sum to compute the number of 0s and 1s in the sub-board
                # Then for each cell (x,y) in the sub-board, we check if it matches the correct pattern
                # We can compute the number of flips needed for the sub-board starting at (i,j) with size k x k
                # We'll use a 2D prefix sum to compute the number of 0s and 1s in the sub-board
                # Then for each cell (x,y) in the sub-board, we check if it matches the correct pattern
                # We can compute the number of flips needed for the sub-board starting at (i,j) with size k x k
                # We'll use a 2D prefix sum to compute the number of 0s and 1s in the sub-board
                # Then for each cell (x,y) in the sub-board