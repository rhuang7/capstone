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
        # But for large n and m, we need a pattern
        # The parity of S(n, m) is 1 if and only if the binary representation of n and m satisfy certain conditions
        # The parity of S(n, m) is 1 if and only if the binary representation of m is a subset of the binary representation of n
        # This is equivalent to (n & m) == m
        if (n & m) == m:
            results.append('1')
        else:
            results.append('0')
    print('\n'.join(results))

if __name__ == '__main__':
    solve()