import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    n, a = map(int, input().split())
    for _ in range(a):
        if n % 10 == 0:
            n = n // 10
        else:
            n = n - 1
    print(n)

if __name__ == '__main__':
    solve()