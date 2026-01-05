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
        # But for large n and m, we need an efficient way
        # The parity of S(n, m) is equivalent to the binomial coefficient C(n-1, m-1) mod 2
        # Using Lucas theorem
        def lucas(a, b):
            if b == 0:
                return 1
            return (lucas(a // 2, b // 2) * lucas(a % 2, b % 2)) % 2
        res = lucas(n-1, m-1)
        results.append(str(res))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()