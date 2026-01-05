import sys

def solve():
    import math
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    for i in range(1, T + 1):
        N = int(input[i])
        count = 0
        while N > 0:
            s = int(math.isqrt(N))
            count += 1
            N -= s * s
        print(count)

if __name__ == '__main__':
    solve()