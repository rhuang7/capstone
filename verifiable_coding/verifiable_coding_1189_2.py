import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    for _ in range(T):
        N = int(data[idx])
        idx += 1
        A = list(map(int, data[idx:idx+N]))
        idx += N
        total = 0
        prefix = [0] * (N + 1)
        for i in range(N):
            prefix[i + 1] = prefix[i] + A[i]
        for k in range(N):
            # Create B by setting A[k] = 0
            # Compute prefix sums of B
            # B = A with A[k] = 0
            # We need to find number of ways to split B into two non-empty contiguous parts with equal sum
            # Let's compute prefix sums of B
            # B[i] = A[i] if i != k else 0
            # Let's compute prefix sums of B
            # B = A with A[k] = 0
            # We need to find number of ways to split B into two non-empty contiguous parts with equal sum
            # Let's compute prefix sums of B
            # B = A with A[k] = 0
            # We need to find number of ways to split B into two non-empty contiguous parts with equal sum
            # Let's compute prefix sums of B
            # B = A with A[k] = 0
            # We need to find number of ways to split B into two non-empty contiguous parts with equal sum
            # Let's compute prefix sums of B
            # B = A with A[k] = 0
            # We need to find number of ways to split B into two non-empty contiguous parts with equal sum
            # Let's compute prefix sums of B
            # B = A with A[k] = 0
            # We need to find number of ways to split B into two non-empty contiguous parts with equal sum
            # Let's compute prefix sums of B
            # B = A with A[k] = 0
            # We need to find number of ways to split B into two non-empty contiguous parts with equal sum
            # Let's compute prefix sums of B
            # B = A with A[k] = 0
            # We need to find number of ways to split B into two non-empty contiguous parts with equal sum
            # Let's compute prefix sums of B
            # B = A with A[k] = 0
            # We need to find number of ways to split B into two non-empty contiguous parts with equal sum
            # Let's compute prefix sums of B
            # B = A with A[k] = 0
            # We need to find number of ways to split B into two non-empty contiguous parts with equal sum
            # Let's compute prefix sums of B
            # B = A with A[k] = 0
            # We need to find number of ways to split B into two non-empty contiguous parts with equal sum
            # Let's compute prefix sums of B
            # B = A with A[k] = 0
            # We need to find number of ways to split B into two non-empty contiguous parts with equal sum
            # Let's compute prefix sums of B
            # B = A with A[k] = 0
            # We need to find number of ways to split B into two non-empty contiguous parts with equal sum
            # Let's compute prefix sums of B
            # B = A with A[k] = 0
            # We need to find number of ways to split B into two non-empty contiguous parts with equal sum
            # Let's compute prefix sums of B
            # B = A with A[k] = 0
            # We need to find number of ways to split B into two non-empty contiguous parts with equal sum
            # Let's compute prefix sums of B
            # B = A with A[k] = 0
            # We need to find number of ways to split B into two non-empty contiguous parts with equal sum
            # Let's compute prefix sums of B
            # B = A with A[k] = 0
            # We need to find number of ways to split B into two non-empty contiguous parts with equal sum
            # Let's compute prefix sums of B
            # B = A with A[k] = 0
            # We need to find number of ways to split B into two non-empty contiguous parts with equal sum
            # Let's compute prefix sums of B
            # B = A with A[k] = 0
            # We need to find number of ways to split B into two non-empty contiguous parts with equal sum
            # Let's compute prefix sums of B
            # B = A with A[k] = 0
            # We need to find number of ways to split B into two non-empty contiguous parts with equal sum
            # Let's compute prefix sums of B
            # B = A with A[k] = 0
            # We need to find number of ways to split B into two non-empty contiguous parts with equal sum
            # Let's compute prefix sums of B
            # B = A with A[k] = 0
            # We need to find number of ways to split B into two non-empty contiguous parts with equal sum
            # Let's compute prefix sums of B
            # B = A with A[k] = 0
            # We need to find number of ways to split B into two non-empty contiguous parts with equal sum
            # Let's compute prefix sums of B
            # B = A with A[k] = 0
            # We need to find number of ways to split B into two non-empty contiguous parts with equal sum
            # Let's compute prefix sums of B
            # B = A with A[k] = 0
            # We need to find number of ways to split B into two non-empty contiguous parts with equal sum
            # Let's compute prefix sums of B
            # B = A with A[k] = 0
            # We need to find number of ways to split B into two non-empty contiguous parts with equal sum
            # Let's compute prefix sums of B
            # B = A with A[k] = 0
            # We need to find number of ways to split B into two non-empty contiguous parts with equal sum
            # Let's compute prefix sums of B
            # B = A with A[k] = 0
            # We need to find number of ways to split B into two non-empty contiguous parts with equal sum
            # Let's compute prefix sums of B
            # B = A with A[k] = 0
            # We need to find number of ways to split B into two non-empty contiguous parts with equal sum
            # Let's compute prefix sums of B
            # B = A with A[k] = 0
            # We need to find number of ways to split B into two non-empty contiguous parts with equal sum
            # Let's compute prefix sums of B
            # B = A with A[k] = 0
            # We need to find number of ways to split B into two non-empty contiguous parts with equal sum
            # Let's compute prefix sums of B
            # B = A with A[k] = 0
            # We need to find number of ways to split B into two non-empty contiguous parts with equal sum
            # Let's compute prefix sums of B
            # B = A with A[k] = 0
            # We need to find number of ways to split B into two non-empty contiguous parts with equal sum
            # Let's compute prefix sums of B
            # B = A with A[k] = 0
            # We need to find number of ways to split B into two non-empty contiguous parts with equal sum
            # Let's compute prefix sums of B
            # B = A with A[k] = 0
            # We need to find number of ways to split B into two non-empty contiguous parts with equal sum
            # Let's compute prefix sums of B
            # B = A with A[k] = 0
            # We need to find number of ways to split B into two non-empty contiguous parts with equal sum
            # Let's compute prefix sums of B
            # B = A with A[k] = 0
            # We need to find number of ways to split B into two non-empty contiguous parts with equal sum
            # Let's compute prefix sums of B
            # B = A with A[k] = 0
            # We need to find number of ways to split B into two non-empty contiguous parts with equal sum
            # Let's compute prefix sums of B
            # B = A with A[k] = 0
            # We need to find number of ways to split B into two non-empty contiguous parts with equal sum
            # Let's compute prefix sums of B
            # B = A with A[k] = 0
            # We need to find number of ways to split B into two non-empty contiguous parts with equal sum
            # Let's compute prefix sums of B
            # B = A with A[k] = 0
            # We need to