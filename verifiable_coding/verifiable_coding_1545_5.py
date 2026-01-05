import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    t = int(data[0])
    idx = 1
    results = []
    for _ in range(t):
        n = int(data[idx])
        m = int(data[idx+1])
        idx += 2
        # Compute S(n, m) mod 2
        # Using the recurrence relation modulo 2
        # S(n, m) mod 2 = (m * S(n-1, m) + S(n-1, m-1)) mod 2
        # Base cases:
        # S(n, 0) = 0 for n > 0
        # S(0, 0) = 1
        # S(n, 1) = 1 for n >= 1
        # S(n, n) = 1 for n >= 1
        # S(n, m) = 0 if m > n
        # We can use dynamic programming with memoization
        # But since n can be up to 1e9, we need a better approach
        # Using Lucas theorem for Stirling numbers modulo 2
        # S(n, m) mod 2 is 1 if and only if the binary representation of m is a subset of the binary representation of n
        # So, we check if (n & m) == m
        if (n & m) == m:
            results.append(1)
        else:
            results.append(0)
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()