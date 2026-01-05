import sys

def solve():
    n, m, a = map(int, sys.stdin.buffer.read().split())
    x = (n + a - 1) // a
    y = (m + a - 1) // a
    print(x * y)

if __name__ == '__main__':
    solve()