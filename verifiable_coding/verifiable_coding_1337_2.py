import sys

def solve():
    import math
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    for _ in range(T):
        N = int(data[idx])
        idx += 1
        P = list(map(int, data[idx:idx+N]))
        idx += N
        R = int(data[idx])
        idx += 1
        min_p = min(P)
        if R >= min_p:
            print(0)
            continue
        # We need to find the smallest x such that x % p == R for all p in P
        # This is equivalent to finding the smallest x >= R such that x - R is divisible by LCM of all p in P
        from math import gcd
        from functools import reduce
        def lcm(a, b):
            return a * b // gcd(a, b)
        L = reduce(lcm, P)
        # The smallest x is R + L
        print(R + L)

if __name__ == '__main__':
    solve()