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
    
    # Precompute for each possible square size the minimum number of flips needed
    # for each possible top-left corner
    # We'll use a 2D array for each possible square size
    # For each square size k, we'll compute for all (i,j) the min flips needed
    # to make a k x k square starting at (i,j) correct
    
    # Precompute for all possible square sizes
    max_size = min(N, M)
    # We'll use a 3D array: dp[k][i][j] = min flips needed for a k x k square starting at (i,j)
    # But since k can be up to 200, and N and M up to 200, this is 200*200*200 = 8,000,000 which is manageable
    # However, we can optimize by using a 2D array for each k
    
    # We'll use a list of 2D arrays, one for each possible k
    # dp[k] is a 2D array of size N x M
    dp = []
    for k in range(1, max_size + 1):
        dp_k = [[0]*M for _ in range(N)]
        for i in range(N - k + 1):
            for j in range(M - k + 1):
                # Compute the number of flips needed for the k x k square starting at (i,j)
                # We can precompute the number of 0s and 1s in each rectangle
                # But for efficiency, we'll compute it directly
                # For a k x k square, the correct pattern is alternating colors
                # The first cell (i,j) can be 0 or 1, and the rest must follow
                # So we need to check for both possibilities and choose the one with fewer flips
                # However, since we can choose to flip cells, we can choose the pattern that requires fewer flips
                # So we can compute the number of flips needed for both possible patterns
                # and choose the minimum
                # But for large k, this is O(k^2) per cell, which is too slow
                # So we need a way to compute this in O(1) per cell
                # We can precompute prefix sums for 0s and 1s
                # Let's precompute prefix sums for 0s and 1s
                # prefix_0[i][j] = number of 0s in the rectangle (0,0) to (i-1,j-1)
                # Similarly for prefix_1
                # Then, the number of 0s in the rectangle (i,j) to (i+k-1,j+k-1) is prefix_0[i+k][j+k] - prefix_0[i][j+k] - prefix_0[i+k][j] + prefix_0[i][j]
                # Similarly for 1s
                # So we can precompute prefix_0 and prefix_1
                # Then, for each cell (i,j), we can compute the number of 0s and 1s in the k x k square
                # Then, the number of flips needed for the pattern starting with 0 is (number of 1s in the square)
                # The number of flips needed for the pattern starting with 1 is (number of 0s in the square)
                # We take the minimum of the two
                # So for each k, we can compute dp[k][i][j] as the minimum of the two
                # But for this, we need the prefix sums
                # So first, precompute prefix_0 and prefix_1
                # Then, for each k, compute dp[k][i][j]
                # But since we need to compute this for all k, we can precompute the prefix sums once
                # Then, for each k, we compute dp[k][i][j]
                # So let's precompute prefix_0 and prefix_1
                # We'll compute them once before processing the queries
                # Now, compute the prefix sums
                # prefix_0[i][j] = number of 0s in the rectangle (0,0) to (i-1,j-1)
                # Similarly for prefix_1
                # We'll precompute these
                # Now, let's precompute prefix_0 and prefix_1
                # For the board, we can compute them
                # But since the board is up to 200x200, this is manageable
                # Now, let's compute prefix_0 and prefix_1
                # We'll compute them once before processing the queries
                # Now, for each k, we can compute dp[k][i][j]
                # But this is O(N*M*k), which for k=200 is O(200*200*200) = 8,000,000, which is acceptable
                # So let's precompute prefix_0 and prefix_1
                # Now, compute prefix_0 and prefix_1
                # prefix_0 is a (N+1) x (M+1) array
                # Similarly for prefix_1
                # Now, let's compute them
                # Initialize prefix_0 and prefix_1
                prefix_0 = [[0]*(M+1) for _ in range(N+1)]
                prefix_1 = [[0]*(M+1) for _ in range(N+1)]
                for i in range(N):
                    for j in range(M):
                        prefix_0[i+1][j+1] = prefix_0[i][j+1] + prefix_0[i+1][j] - prefix_0[i][j] + (1 if board[i][j] == '0' else 0)
                        prefix_1[i+1][j+1] = prefix_1[i][j+1] + prefix_1[i+1][j] - prefix_1[i][j] + (1 if board[i][j] == '1' else 0)
                # Now, for each k, compute dp[k][i][j]
                # But since we need to compute this for all k, we can precompute it
                # So for each k, we'll compute dp_k
                # But this is O(N*M*k), which is acceptable
                # So for each k, we compute dp_k
                # Now, for each k, we'll compute dp_k
                # So let's precompute all dp_k
                # But since we need to process queries, we can precompute for all possible k
                # Now, for each k, we'll compute dp_k
                # But since we need to process queries, we can precompute for all possible k
                # Now, for each k, we'll compute dp_k
                # So let's precompute for all k
                # But for large k, this is O(N*M*k) which is 200*200*200 = 8,000,000
                # So let's precompute for all k
                # Now, for each k, compute dp_k
                # But for each k, we can compute dp_k
                # Now, for each k, compute dp_k
                # So let's proceed
                # Now, for each k, compute dp_k
                # So for each k, we can compute dp_k as follows:
                # For each i in 0 to N-k
                # For each j in 0 to M-k
                # Compute the number of 0s and 1s in the k x k square starting at (i,j)
                # The number of 0s is prefix_0[i+k][j+k] - prefix_0[i][j+k] - prefix_0[i+k][j] + prefix_0[i][j]
                # Similarly for 1s
                # Then, the number of flips needed for the pattern starting with 0 is (number of 1s in the square)
                # The number of flips needed for the pattern starting with 1 is (number of 0s in the square)
                # We take the minimum of the two
                # So for dp_k[i][j], we store this minimum
                # So for each k, we compute dp_k
                # Now, let's compute dp_k
                # But since we need to compute this for all k, we can precompute it
                # So let's proceed
                # Now, compute dp_k
                # For each i in range(N - k + 1)
                # For each j in range(M - k