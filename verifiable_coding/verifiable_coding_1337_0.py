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
        # For each person count p, the minimum number of candies needed is (p * k + R) where k is the maximum possible
        # So we need to find the minimum value of (p * k + R) such that (total - R) is divisible by p for all p in P
        # Which is equivalent to finding the least common multiple of all (p) and then calculating the minimum total
        # The minimum total is (lcm * k + R) where k is the smallest integer such that (lcm * k + R) >= (min_p * 1 + R)
        # So we need to find the lcm of all p in P
        from math import gcd
        def lcm(a, b):
            return a * b // gcd(a, b)
        current_lcm = 1
        for p in P:
            current_lcm = lcm(current_lcm, p)
        # Now find the minimum k such that (current_lcm * k + R) >= (min_p * 1 + R)
        # Which is k >= 1, so the minimum is current_lcm * 1 + R
        print(current_lcm + R)

if __name__ == '__main__':
    solve()