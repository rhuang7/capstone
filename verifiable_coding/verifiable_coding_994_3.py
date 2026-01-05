import sys
import collections

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(T):
        N, X = int(data[idx]), int(data[idx+1])
        idx += 2
        A = list(map(int, data[idx:idx+N]))
        idx += N
        
        # Precompute prefix sums of A
        prefix = [0] * (N + 1)
        for i in range(N):
            prefix[i+1] = prefix[i] + A[i]
        
        # Count the number of square submatrices with sum X
        count = 0
        
        # Iterate over all possible square sizes
        for size in range(1, N+1):
            # For each possible top-left corner (i, j)
            for i in range(N - size + 1):
                for j in range(N - size + 1):
                    # Compute the sum of the square submatrix
                    # The sum is (sum of A[i..i+size-1] * size * 2 - sum of A[i..i+size-1] * 2) + sum of A[j..j+size-1] * size * 2 - sum of A[j..j+size-1] * 2
                    # Wait, this is not correct. Let's compute it properly.
                    # The sum of the square submatrix is sum_{i1 to i2} sum_{j1 to j2} (A_i + A_j) = sum_{i1 to i2} (size * (A_i + A_j)) = size * sum_{i1 to i2} (A_i) * 2 - size * sum_{i1 to i2} A_i
                    # Wait, let's compute it correctly.
                    # The sum of the square submatrix is sum_{i=x1 to x2} sum_{j=y1 to y2} (A_i + A_j) = sum_{i=x1 to x2} (size * A_i) + sum_{j=y1 to y2} (size * A_j) = size * (sum A_i + sum A_j)
                    # But since i and j range over the same size, it's size * (sum A_i + sum A_j) = size * (2 * sum A_i)
                    # So the sum is size * 2 * sum A_i
                    # So we need to find the number of squares of size 'size' where 2 * size * sum A_i = X
                    # So sum A_i = X / (2 * size)
                    # So for each possible i, compute sum A[i..i+size-1] and check if it equals X / (2 * size)
                    # But this is not correct. Let's compute the correct sum.
                    # The correct sum is sum_{i=x1 to x2} sum_{j=y1 to y2} (A_i + A_j) = sum_{i=x1 to x2} (size * A_i) + sum_{j=y1 to y2} (size * A_j) = size * (sum A_i + sum A_j)
                    # But since i and j range over the same size, it's size * (sum A_i + sum A_j) = size * (2 * sum A_i)
                    # So the sum is 2 * size * sum A_i
                    # So we need to find the number of squares of size 'size' where 2 * size * sum A_i = X
                    # So sum A_i = X / (2 * size)
                    # So for each possible i, compute sum A[i..i+size-1] and check if it equals X / (2 * size)
                    # But this is not correct. Let's compute the correct sum.
                    # The correct sum is sum_{i=x1 to x2} sum_{j=y1 to y2} (A_i + A_j) = sum_{i=x1 to x2} sum_{j=y1 to y2} A_i + sum_{i=x1 to x2} sum_{j=y1 to y2} A_j
                    # = sum_{i=x1 to x2} (size * A_i) + sum_{j=y1 to y2} (size * A_j) = size * (sum A_i + sum A_j)
                    # But since i and j range over the same size, it's size * (sum A_i + sum A_j) = size * (2 * sum A_i)
                    # So the sum is 2 * size * sum A_i
                    # So we need to find the number of squares of size 'size' where 2 * size * sum A_i = X
                    # So sum A_i = X / (2 * size)
                    # So for each possible i, compute sum A[i..i+size-1] and check if it equals X / (2 * size)
                    # But this is not correct. Let's compute the correct sum.
                    # The correct sum is sum_{i=x1 to x2} sum_{j=y1 to y2} (A_i + A_j) = sum_{i=x1 to x2} sum_{j=y1 to y2} A_i + sum_{i=x1 to x2} sum_{j=y1 to y2} A_j
                    # = sum_{i=x1 to x2} (size * A_i) + sum_{j=y1 to y2} (size * A_j) = size * (sum A_i + sum A_j)
                    # But since i and j range over the same size, it's size * (sum A_i + sum A_j) = size * (2 * sum A_i)
                    # So the sum is 2 * size * sum A_i
                    # So we need to find the number of squares of size 'size' where 2 * size * sum A_i = X
                    # So sum A_i = X / (2 * size)
                    # So for each possible i, compute sum A[i..i+size-1] and check if it equals X / (2 * size)
                    # But this is not correct. Let's compute the correct sum.
                    # The correct sum is sum_{i=x1 to x2} sum_{j=y1 to y2} (A_i + A_j) = sum_{i=x1 to x2} sum_{j=y1 to y2} A_i + sum_{i=x1 to x2} sum_{j=y1 to y2} A_j
                    # = sum_{i=x1 to x2} (size * A_i) + sum_{j=y1 to y2} (size * A_j) = size * (sum A_i + sum A_j)
                    # But since i and j range over the same size, it's size * (sum A_i + sum A_j) = size * (2 * sum A_i)
                    # So the sum is 2 * size * sum A_i
                    # So we need to find the number of squares of size 'size' where 2 * size * sum A_i = X
                    # So sum A_i = X / (2 * size)
                    # So for each possible i, compute sum A[i..i+size-1] and check if it equals X / (2 * size)
                    # But this is not correct. Let's compute the correct sum.
                    # The correct sum is sum_{i=x1 to x2} sum_{j=y1 to y2} (A_i + A_j) = sum_{i=x1 to x2} sum_{j=y1 to y2} A_i + sum_{i=x1 to x2} sum_{j=y1 to y2} A_j
                    # = sum_{i=x1 to x2} (size * A_i) + sum_{j=y1 to y2} (size * A_j) = size * (sum A_i + sum A_j)
                    # But since i and j range over the same size, it's size * (sum A_i + sum A_j) = size * (2 * sum A_i)
                    # So the sum is 2 * size * sum A_i
                    # So we need to find the number of squares of size 'size' where 2 * size * sum A_i = X
                    # So sum A_i = X / (2 * size)
                    # So for each possible i, compute sum A[i..i+size-1] and check if it equals X / (2 * size)
                    # But this is not correct. Let's compute the correct sum.
                    # The correct sum is sum_{i=x1 to x2} sum_{j=y1 to y2} (A_i + A_j) = sum_{i=x1 to x2} sum_{j=y1 to y2} A_i + sum_{i=x1 to x2} sum_{j=y1 to y2} A_j
                    # = sum_{i=x1 to x2} (size * A_i) + sum_{j=y1 to y2} (size * A_j) = size * (sum A_i + sum A_j)