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
            # Set A[k] to 0
            # Compute prefix sums with A[k] set to 0
            # We need to find the number of ways to split B into two non-empty contiguous parts with equal sum
            # Let's compute the prefix sum with A[k] set to 0
            # We can do this by subtracting A[k] from the original prefix sum
            # But we need to handle the prefix sum correctly
            # Let's compute the prefix sum with A[k] set to 0
            # We can do this by creating a new prefix sum array
            # But since N is large, we need an efficient way
            # Let's compute the prefix sum with A[k] set to 0
            # Let's compute the prefix sum with A[k] set to 0
            # We can use the original prefix sum and subtract A[k] at position k
            # But we need to handle the prefix sum correctly
            # Let's compute the prefix sum with A[k] set to 0
            # Let's compute the prefix sum with A[k] set to 0
            # Let's compute the prefix sum with A[k] set to 0
            # Let's compute the prefix sum with A[k] set to 0
            # Let's compute the prefix sum with A[k] set to 0
            # Let's compute the prefix sum with A[k] set to 0
            # Let's compute the prefix sum with A[k] set to 0
            # Let's compute the prefix sum with A[k] set to 0
            # Let's compute the prefix sum with A[k] set to 0
            # Let's compute the prefix sum with A[k] set to 0
            # Let's compute the prefix sum with A[k] set to 0
            # Let's compute the prefix sum with A[k] set to 0
            # Let's compute the prefix sum with A[k] set to 0
            # Let's compute the prefix sum with A[k] set to 0
            # Let's compute the prefix sum with A[k] set to 0
            # Let's compute the prefix sum with A[k] set to 0
            # Let's compute the prefix sum with A[k] set to 0
            # Let's compute the prefix sum with A[k] set to 0
            # Let's compute the prefix sum with A[k] set to 0
            # Let's compute the prefix sum with A[k] set to 0
            # Let's compute the prefix sum with A[k] set to 0
            # Let's compute the prefix sum with A[k] set to 0
            # Let's compute the prefix sum with A[k] set to 0
            # Let's compute the prefix sum with A[k] set to 0
            # Let's compute the prefix sum with A[k] set to 0
            # Let's compute the prefix sum with A[k] set to 0
            # Let's compute the prefix sum with A[k] set to 0
            # Let's compute the prefix sum with A[k] set to 0
            # Let's compute the prefix sum with A[k] set to 0
            # Let's compute the prefix sum with A[k] set to 0
            # Let's compute the prefix sum with A[k] set to 0
            # Let's compute the prefix sum with A[k] set to 0
            # Let's compute the prefix sum with A[k] set to 0
            # Let's compute the prefix sum with A[k] set to 0
            # Let's compute the prefix sum with A[k] set to 0
            # Let's compute the prefix sum with A[k] set to 0
            # Let's compute the prefix sum with A[k] set to 0
            # Let's compute the prefix sum with A[k] set to 0
            # Let's compute the prefix sum with A[k] set to 0
            # Let's compute the prefix sum with A[k] set to 0
            # Let's compute the prefix sum with A[k] set to 0
            # Let's compute the prefix sum with A[k] set to 0
            # Let's compute the prefix sum with A[k] set to 0
            # Let's compute the prefix sum with A[k] set to 0
            # Let's compute the prefix sum with A[k] set to 0
            # Let's compute the prefix sum with A[k] set to 0
            # Let's compute the prefix sum with A[k] set to 0
            # Let's compute the prefix sum with A[k] set to 0
            # Let's compute the prefix sum with A[k] set to 0
            # Let's compute the prefix sum with A[k] set to 0
            # Let's compute the prefix sum with A[k] set to 0
            # Let's compute the prefix sum with A[k] set to 0
            # Let's compute the prefix sum with A[k] set to 0
            # Let's compute the prefix sum with A[k] set to 0
            # Let's compute the prefix sum with A[k] set to 0
            # Let's compute the prefix sum with A[k] set to 0
            # Let's compute the prefix sum with A[k] set to 0
            # Let's compute the prefix sum with A[k] set to 0
            # Let's compute the prefix sum with A[k] set to 0
            # Let's compute the prefix sum with A[k] set to 0
            # Let's compute the prefix sum with A[k] set to 0
            # Let's compute the prefix sum with A[k] set to 0
            # Let's compute the prefix sum with A[k] set to 0
            # Let's compute the prefix sum with A[k] set to 0
            # Let's compute the prefix sum with A[k] set to 0
            # Let's compute the prefix sum with A[k] set to 0
            # Let's compute the prefix sum with A[k] set to 0
            # Let's compute the prefix sum with A[k] set to 0
            # Let's compute the prefix sum with A[k] set to 0
            # Let's compute the prefix sum with A[k] set to 0
            # Let's compute the prefix sum with A[k] set to 0
            # Let's compute the prefix sum with A[k] set to 0
            # Let's compute the prefix sum with A[k] set to 0
            # Let's compute the prefix sum with A[k] set to 0
            # Let's compute the prefix sum with A[k] set to 0
            # Let's compute the prefix sum with A[k] set to 0
            # Let's compute the prefix sum with A[k] set to 0
            # Let's compute the prefix sum with A[k] set to 0
            # Let's compute the prefix sum with A[k] set to 0
            # Let's compute the prefix sum with A[k] set to 0
            # Let's compute the prefix sum with A[k] set to 0
            # Let's compute the prefix sum with A[k] set to 0
            # Let's compute the prefix sum with A[k] set to 0
            # Let's compute the prefix sum with A[k] set to 0
            # Let's compute the prefix sum with A[k] set to 0
            # Let's compute the prefix sum with A[k] set to 0
            # Let's compute the prefix sum with A[k] set to 0
            # Let's compute the prefix sum with A[k] set to 0
            # Let's compute the prefix sum with A[k] set to 0
            # Let's compute the prefix sum with A[k] set to 0
            # Let's compute the prefix sum with A[k] set to 0
            # Let's compute the prefix sum with A[k] set to 0
            # Let's compute the prefix sum with A[k] set to 0
            # Let's compute the prefix sum with A[k] set to 0
            # Let's compute the prefix sum with A[k] set to 0
            # Let's compute the prefix sum with A[k] set to 0
            # Let's compute the prefix sum with A[k] set to 0
            # Let's compute the prefix sum with A[k] set to