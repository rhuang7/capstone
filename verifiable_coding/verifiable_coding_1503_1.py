import sys

def solve():
    import math
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    idx = 1
    for _ in range(T):
        N = int(input[idx])
        M = int(input[idx+1])
        idx += 2
        g = math.gcd(N, M)
        a = N // g
        b = M // g
        print(a * b)

if __name__ == '__main__':
    solve()