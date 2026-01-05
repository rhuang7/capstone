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
        # The minimum number of candies is R + (min_p - R) * k, where k is the smallest integer such that R + k * min_p is divisible by min_p
        # We need to find the smallest k such that (R + k * min_p) % min_p == 0
        # But since R < min_p, we can directly compute it as R + min_p
        # Because R + min_p is the smallest number >= R that is divisible by min_p
        # So the minimum number of candies is R + min_p
        print(R + min_p)

if __name__ == '__main__':
    solve()