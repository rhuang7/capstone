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
        # For each P[i], the number of candies must be of the form k*P[i] + R
        # We need the minimum number of candies that satisfies this for all P[i]
        # So we need the least common multiple (LCM) of all P[i], then compute the smallest k such that k*LCM + R is minimized
        # But since we want the minimum total candies, we need the smallest k such that k*LCM + R is minimized, which is k=1
        # So the answer is LCM of all P[i] + R
        # But we need to ensure that R is less than min(P[i])
        # So compute LCM of all P[i]
        from math import gcd
        def lcm(a, b):
            return a * b // gcd(a, b)
        l = P[0]
        for num in P[1:]:
            l = lcm(l, num)
        print(l + R)

if __name__ == '__main__':
    solve()