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
        # Using the recurrence relation mod 2
        # S(n, m) mod 2 = (m * S(n-1, m) + S(n-1, m-1)) mod 2
        # But since we are working mod 2, this simplifies to:
        # S(n, m) mod 2 = (m * S(n-1, m) + S(n-1, m-1)) mod 2
        # We can use dynamic programming with mod 2
        # However, for large n and m, we need a smarter approach
        # The parity of S(n, m) is equal to the binomial coefficient C(n-1, m-1) mod 2
        # This is known as Lucas's theorem
        # So we need to compute C(n-1, m-1) mod 2
        # Using Lucas's theorem, we can compute this efficiently
        # Lucas's theorem: C(n, m) mod 2 is 1 if and only if the binary representation of m is a subset of the binary representation of n
        # So we need to check if the binary representation of m-1 is a subset of the binary representation of n-1
        # This can be done by checking if (n-1) & (m-1) == m-1
        if (n-1) & (m-1) == m-1:
            results.append('1')
        else:
            results.append('0')
    print('\n'.join(results))

if __name__ == '__main__':
    solve()