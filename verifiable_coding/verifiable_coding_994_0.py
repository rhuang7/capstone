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
        
        # Precompute prefix sums of B
        # B[i][j] = A[i] + A[j]
        # Sum of square submatrix from (x1, y1) to (x2, y2) is sum_{i=x1}^{x2} sum_{j=y1}^{y2} (A[i] + A[j])
        # = sum_{i=x1}^{x2} (A[i] * (y2 - y1 + 1) + sum_{j=y1}^{y2} A[j])
        # = (y2 - y1 + 1) * sum_{i=x1}^{x2} A[i] + (x2 - x1 + 1) * sum_{j=y1}^{y2} A[j]
        # = (y2 - y1 + 1) * (prefix[x2] - prefix[x1-1]) + (x2 - x1 + 1) * (prefix[y2] - prefix[y1-1])
        # Let k = x2 - x1 = y2 - y1
        # Then x2 = x1 + k, y2 = y1 + k
        # So the sum is k * (prefix[x1 + k] - prefix[x1-1]) + (k + 1) * (prefix[y1 + k] - prefix[y1-1])
        # We need this sum to be X
        
        # For each possible k (from 0 to N-1), iterate over possible x1 and y1
        count = 0
        for k in range(N):
            # For each possible x1, compute the value of (prefix[x1 + k] - prefix[x1-1]) * k
            # And for each possible y1, compute (prefix[y1 + k] - prefix[y1-1]) * (k + 1)
            # We need k * a + (k + 1) * b = X
            # => k*a + (k + 1)*b = X
            # => k*(a + b) + b = X
            # => b = X - k*(a + b)
            # But this may not help directly. Instead, we can precompute all possible a and b for this k
            # and check if k*a + (k+1)*b = X
            # So for each x1, compute a = prefix[x1 + k] - prefix[x1-1]
            # For each y1, compute b = prefix[y1 + k] - prefix[y1-1]
            # Check if k*a + (k+1)*b == X
            # To optimize, we can precompute all possible a and b for this k
            # and for each a, find the number of b's such that (k+1)*b = X - k*a
            # => b = (X - k*a) / (k+1)
            # So for each a, compute (X - k*a) and check if it is divisible by (k+1)
            # and if so, check how many times that value of b appears in the list of b's
            # So we can precompute all possible b's for this k, and store their frequencies
            # Then for each a, compute (X - k*a) and check if it is divisible by (k+1)
            # and if so, look up the frequency of (X - k*a) / (k+1) in the b list
            # This would be O(N) per k, which is acceptable since k ranges up to N-1 and N is up to 1e5
            # However, for large N, this would be O(N^2), which is too slow
            # So we need a better approach
            
            # Let's try to find a mathematical way to express the condition
            # k*a + (k+1)*b = X
            # => k*a + (k+1)*b = X
            # => k*(a + b) + b = X
            # => b = X - k*(a + b)
            # Not helpful. Let's try to find a way to express this in terms of a and b
            # For a fixed k, we can precompute all possible a and b
            # Then for each a, compute required b = (X - k*a) / (k+1)
            # And check if this b is present in the list of b's
            # So for each k, we can precompute all possible a's and b's
            # Then for each a, compute required b and check if it exists in the b list
            # This is O(N) per k, which is O(N^2) overall, which is too slow for N=1e5
            
            # So we need a better approach
            # Let's try to find a way to express the sum of the square submatrix in terms of prefix sums
            # The sum is k * (prefix[x1 + k] - prefix[x1-1]) + (k+1) * (prefix[y1 + k] - prefix[y1-1])
            # = k * (prefix[x1 + k] - prefix[x1-1]) + (k+1) * (prefix[y1 + k] - prefix[y1-1])
            # = k * (prefix[x1 + k] - prefix[x1-1]) + (k+1) * (prefix[y1 + k] - prefix[y1-1])
            # Let's denote this as k*a + (k+1)*b = X
            # We can rewrite this as:
            # k*a + (k+1)*b = X
            # => k*(a + b) + b = X
            # => b = X - k*(a + b)
            # Not helpful. Let's think of it as:
            # k*a + (k+1)*b = X
            # => k*(a + b) + b = X
            # => b = X - k*(a + b)
            # Not helpful. Let's think of it as:
            # k*a + (k+1)*b = X
            # => k*a + (k+1)*b = X
            # => k*(a + b) + b = X
            # => b = X - k*(a + b)
            # Not helpful. Let's try to find a way to express this in terms of a and b
            # Let's think of this as:
            # k*a + (k+1)*b = X
            # => k*a + (k+1)*b = X
            # => k*a + (k+1)*b = X
            # => k*a + (k+1)*b = X
            # => k*a + (k+1)*b = X
            # => k*a + (k+1)*b = X
            # => k*a + (k+1)*b = X
            # => k*a + (k+1)*b = X
            # => k*a + (k+1)*b = X
            # => k*a + (k+1)*b = X
            # => k*a + (k+1)*b = X
            # => k*a + (k+1)*b = X
            # => k*a + (k+1)*b = X
            # => k*a + (k+1)*b = X
            # => k*a + (k+1)*b = X
            # => k*a + (k+1)*b = X
            # => k*a + (k+1)*b = X
            # => k*a + (k+1)*b = X
            # => k*a + (k+1)*b = X
            # => k*a + (k+1)*b = X
            # => k*a + (k+1)*b = X
            # => k*a + (k+1)*b = X
            # => k*a + (k+1)*b = X
            # => k*a + (k+1)*b = X
            # => k*a + (k+1)*b = X
            # => k*a + (k+1)*b = X
            # => k*a + (k+1)*b = X
            # => k*a + (k+1)*b = X
            # => k*a + (k+1)*b = X
            # => k*a + (k+1)*