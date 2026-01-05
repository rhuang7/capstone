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
        # For each person count p, the number of candies per person is (x - R) / p
        # x is the total candies, which must be >= R + 1 (since each person gets at least 1 candy)
        # x = k * p + R, where k is a positive integer
        # We need to find the smallest x such that x - R is divisible by all p in P
        # x - R must be a common multiple of all p in P
        # The smallest such x is R + LCM of all p in P
        # Compute LCM of all p in P
        def lcm(a, b):
            return a * b // math.gcd(a, b)
        current_lcm = 1
        for p in P:
            current_lcm = lcm(current_lcm, p)
        result = current_lcm + R
        print(result)

if __name__ == '__main__':
    solve()