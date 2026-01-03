import sys
import bisect

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
        
        # Precompute prefix sums of B (but B is not stored, we compute on the fly)
        # We need to find the number of square submatrices of B with sum X
        
        # For a square submatrix of size k x k, the sum can be computed using prefix sums
        # The sum of B from (x1, y1) to (x2, y2) is sum_{i=x1}^{x2} sum_{j=y1}^{y2} (A_i + A_j)
        # = sum_{i=x1}^{x2} (A_i * (y2 - y1 + 1)) + sum_{j=y1}^{y2} (A_j * (x2 - x1 + 1))
        # = (y2 - y1 + 1) * sum_{i=x1}^{x2} A_i + (x2 - x1 + 1) * sum_{j=y1}^{y2} A_j
        
        # Let k = x2 - x1 + 1 = y2 - y1 + 1
        # Then sum = k * (sum_A[x2] - sum_A[x1-1]) + k * (sum_A[y2] - sum_A[y1-1])
        # = k * (sum_A[x2] - sum_A[x1-1] + sum_A[y2] - sum_A[y1-1])
        
        # Let's precompute all possible values of (sum_A[i] - sum_A[j]) for 0 <= j < i <= N
        # Then for each k, we can find pairs (i, j) such that k * (sum_A[i] - sum_A[j] + sum_A[j] - sum_A[i]) = X
        # Wait, that's not right. Let me re-derive:
        
        # sum = k * (sum_A[x2] - sum_A[x1-1] + sum_A[y2] - sum_A[y1-1])
        # = k * (sum_A[x2] + sum_A[y2] - sum_A[x1-1] - sum_A[y1-1])
        
        # Let's define for each i, the value sum_A[i] as prefix[i]
        # Then for a square of size k, we need to find pairs (i, j) such that:
        # k * (prefix[i] + prefix[j] - prefix[i-k] - prefix[j-k]) = X
        
        # But this is complicated. Let's think of it differently.
        
        # For a square of size k x k, the sum is:
        # sum_{i=1}^k sum_{j=1}^k (A_i + A_j) = k * sum_{i=1}^k A_i + k * sum_{j=1}^k A_j = 2k * sum_{i=1}^k A_i
        
        # Wait, no. Because for each i and j, we have A_i + A_j. So the total is:
        # sum_{i=1}^k sum_{j=1}^k (A_i + A_j) = k * sum_{i=1}^k A_i + k * sum_{j=1}^k A_j = 2k * sum_{i=1}^k A_i
        
        # So the sum of the square submatrix of size k x k is 2k * sum_{i=1}^k A_i
        
        # So we need to find the number of k such that 2k * sum_{i=1}^k A_i = X
        
        # So for each k from 1 to N, we can compute the sum of the first k elements of A, multiply by 2k, and check if it equals X
        
        # So the solution is to compute for each k, the sum of the first k elements of A, multiply by 2k, and count how many times it equals X
        
        count = 0
        for k in range(1, N+1):
            s = prefix[k]
            if 2 * k * s == X:
                count += 1
        results.append(count)
    
    for res in results:
        print(res)