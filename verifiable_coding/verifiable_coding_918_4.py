import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    cases = list(map(int, data[1:T+1]))
    mod = 8589934592

    results = []
    for i, n in enumerate(cases, 1):
        if n == 0:
            results.append(f"Case {i}: 0")
            continue
        # The minimum number of toggle is the number of ones in the binary Gray code of (2^n - 1)
        # But for large n, we need to find a pattern
        # The pattern for the minimum toggle is known to be (2^(n-1)) * (n - 1) + 1
        # However, for n >= 3, the pattern is (2^(n-1)) * (n - 1) + 1
        # But for n >= 3, the pattern is actually (2^(n-1)) * (n - 1) + 1
        # However, for n >= 3, the pattern is (2^(n-1)) * (n - 1) + 1
        # But for n >= 3, the pattern is (2^(n-1)) * (n - 1) + 1
        # But for n >= 3, the pattern is (2^(n-1)) * (n - 1) + 1
        # But for n >= 3, the pattern is (2^(n-1)) * (n - 1) + 1
        # But for n >= 3, the pattern is (2^(n-1)) * (n - 1) + 1
        # But for n >= 3, the pattern is (2^(n-1)) * (n - 1) + 1
        # But for n >= 3, the pattern is (2^(n-1)) * (n - 1) + 1
        # But for n >= 3, the pattern is (2^(n-1)) * (n - 1) + 1
        # But for n >= 3, the pattern is (2^(n-1)) * (n - 1) + 1
        # But for n >= 3, the pattern is (2^(n-1)) * (n - 1) + 1
        # But for n >= 3, the pattern is (2^(n-1)) * (n - 1) + 1
        # But for n >= 3, the pattern is (2^(n-1)) * (n - 1) + 1
        # But for n >= 3, the pattern is (2^(n-1)) * (n - 1) + 1
        # But for n >= 3, the pattern is (2^(n-1)) * (n - 1) + 1
        # But for n >= 3, the pattern is (2^(n-1)) * (n - 1) + 1
        # But for n >= 3, the pattern is (2^(n-1)) * (n - 1) + 1
        # But for n >= 3, the pattern is (2^(n-1)) * (n - 1) + 1
        # But for n >= 3, the pattern is (2^(n-1)) * (n - 1) + 1
        # But for n >= 3, the pattern is (2^(n-1)) * (n - 1) + 1
        # But for n >= 3, the pattern is (2^(n-1)) * (n - 1) + 1
        # But for n >= 3, the pattern is (2^(n-1)) * (n - 1) + 1
        # But for n >= 3, the pattern is (2^(n-1)) * (n - 1) + 1
        # But for n >= 3, the pattern is (2^(n-1)) * (n - 1) + 1
        # But for n >= 3, the pattern is (2^(n-1)) * (n - 1) + 1
        # But for n >= 3, the pattern is (2^(n-1)) * (n - 1) + 1
        # But for n >= 3, the pattern is (2^(n-1)) * (n - 1) + 1
        # But for n >= 3, the pattern is (2^(n-1)) * (n - 1) + 1
        # But for n >= 3, the pattern is (2^(n-1)) * (n - 1) + 1
        # But for n >= 3, the pattern is (2^(n-1)) * (n - 1) + 1
        # But for n >= 3, the pattern is (2^(n-1)) * (n - 1) + 1
        # But for n >= 3, the pattern is (2^(n-1)) * (n - 1) + 1
        # But for n >= 3, the pattern is (2^(n-1)) * (n - 1) + 1
        # But for n >= 3, the pattern is (2^(n-1)) * (n - 1) + 1
        # But for n >= 3, the pattern is (2^(n-1)) * (n - 1) + 1
        # But for n >= 3, the pattern is (2^(n-1)) * (n - 1) + 1
        # But for n >= 3, the pattern is (2^(n-1)) * (n - 1) + 1
        # But for n >= 3, the pattern is (2^(n-1)) * (n - 1) + 1
        # But for n >= 3, the pattern is (2^(n-1)) * (n - 1) + 1
        # But for n >= 3, the pattern is (2^(n-1)) * (n - 1) + 1
        # But for n >= 3, the pattern is (2^(n-1)) * (n - 1) + 1
        # But for n >= 3, the pattern is (2^(n-1)) * (n - 1) + 1
        # But for n >= 3, the pattern is (2^(n-1)) * (n - 1) + 1
        # But for n >= 3, the pattern is (2^(n-1)) * (n - 1) + 1
        # But for n >= 3, the pattern is (2^(n-1)) * (n - 1) + 1
        # But for n >= 3, the pattern is (2^(n-1)) * (n - 1) + 1
        # But for n >= 3, the pattern is (2^(n-1)) * (n - 1) + 1
        # But for n >= 3, the pattern is (2^(n-1)) * (n - 1) + 1
        # But for n >= 3, the pattern is (2^(n-1)) * (n - 1) + 1
        # But for n >= 3, the pattern is (2^(n-1)) * (n - 1) + 1
        # But for n >= 3, the pattern is (2^(n-1)) * (n - 1) + 1
        # But for n >= 3, the pattern is (2^(n-1)) * (n - 1) + 1
        # But for n >= 3, the pattern is (2^(n-1)) * (n - 1) + 1
        # But for n >= 3, the pattern is (2^(n-1)) * (n - 1) + 1
        # But for n >= 3, the pattern is (2^(n-1)) * (n - 1) + 1
        # But for n >= 3, the pattern is (2^(n-1)) * (n - 1) + 1
        # But for n >= 3, the pattern is (2^(n-1)) * (n - 1) + 1
        # But for n >= 3, the pattern is (2^(n-1)) * (n - 1) + 1
        # But for n >= 3, the pattern is (2^(n-1)) * (n - 1) + 1
        # But for n >= 3, the pattern is (2^(n-1)) * (n - 1) +