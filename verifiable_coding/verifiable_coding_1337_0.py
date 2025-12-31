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
        # For each person count p, the number of candies must be of the form k*p + R
        # We need the minimum such number that works for all p in P
        # So we need to find the smallest number x such that x ≡ R (mod p) for all p in P
        # This is equivalent to finding the smallest x >= R such that x ≡ R (mod LCM of all p in P)
        from math import gcd
        from functools import reduce
        def lcm(a, b):
            return a * b // gcd(a, b)
        L = reduce(lcm, P)
        # The smallest x is R + k*L where k is the smallest integer such that x >= R + 1 (since each person must get at least 1 candy)
        # So x = R + L * k, where k is the smallest integer such that R + L * k >= R + 1
        # Which is k = 1 if R + L >= R + 1, which it always is
        x = R + L
        print(x)

if __name__ == '__main__':
    solve()