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
        
        # Precompute prefix sums of B (but we don't need to store B)
        # Instead, we use the formula B[i][j] = A[i] + A[j]
        # The sum of a square submatrix of B is sum_{i=x1}^x2 sum_{j=y1}^y2 (A[i] + A[j])
        # = sum_{i=x1}^x2 (A[i] * (y2 - y1 + 1)) + sum_{j=y1}^y2 (A[j] * (x2 - x1 + 1))
        # = (y2 - y1 + 1) * sum_{i=x1}^x2 A[i] + (x2 - x1 + 1) * sum_{j=y1}^y2 A[j]
        # = (y2 - y1 + 1) * (prefix[x2] - prefix[x1-1]) + (x2 - x1 + 1) * (prefix[y2] - prefix[y1-1])
        
        # Let k = x2 - x1 + 1 = y2 - y1 + 1 (since it's a square)
        # So we need to find all k such that there exist x1, y1 with:
        # k * (prefix[x1 + k - 1] - prefix[x1 - 1]) + k * (prefix[y1 + k - 1] - prefix[y1 - 1]) = X
        # => k * (sumA[x1 + k - 1] - sumA[x1 - 1] + sumA[y1 + k - 1] - sumA[y1 - 1]) = X
        # => sumA[x1 + k - 1] - sumA[x1 - 1] + sumA[y1 + k - 1] - sumA[y1 - 1] = X / k
        
        # For each k from 1 to N:
        count = 0
        for k in range(1, N+1):
            target = X // k
            if k * target != X:
                continue
            # We need to find pairs (i, j) such that:
            # (prefix[i + k - 1] - prefix[i - 1]) + (prefix[j + k - 1] - prefix[j - 1]) = target
            # where 1 <= i <= N - k + 1, 1 <= j <= N - k + 1
            # Let's precompute all possible values of (prefix[i + k - 1] - prefix[i - 1]) for i in valid range
            # and count how many times each value occurs
            freq = {}
            for i in range(1, N - k + 2):
                val = prefix[i + k - 1] - prefix[i - 1]
                if val in freq:
                    freq[val] += 1
                else:
                    freq[val] += 1
            # Now for each value in freq, check if (target - val) is also in freq
            for val in freq:
                if (target - val) in freq:
                    count += freq[val] * freq[target - val]
        results.append(count)
    
    for res in results:
        print(res)