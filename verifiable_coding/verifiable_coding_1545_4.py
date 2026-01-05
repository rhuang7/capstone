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
        # We can compute this using dynamic programming with modulo 2
        # However, for n up to 1e9, we need a formula
        # The parity of S(n, m) is 1 if and only if the binary representation of m is a subset of the binary representation of n
        # This is known as the Lucas theorem for Stirling numbers
        # So, we check if every bit set in m is also set in n
        # If yes, then S(n, m) mod 2 is 1, else 0
        # So, we check if (n & m) == m
        if (n & m) == m:
            results.append('1')
        else:
            results.append('0')
    print('\n'.join(results))

if __name__ == '__main__':
    solve()