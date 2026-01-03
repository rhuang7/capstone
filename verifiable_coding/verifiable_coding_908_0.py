import sys

def solve():
    import math
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    cases = list(map(int, input[1:T+1]))
    for N in cases:
        h = math.isqrt(2 * N)
        while (h * (h + 1)) // 2 > N:
            h -= 1
        print(h)

if __name__ == '__main__':
    solve()