import sys

def solve():
    import math
    n, m, a = map(int, sys.stdin.buffer.read().split())
    rows = math.ceil(n / a)
    cols = math.ceil(m / a)
    print(rows * cols)

if __name__ == '__main__':
    solve()