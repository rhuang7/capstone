import sys

def solve():
    input = sys.stdin.buffer.read().strip()
    N = int(input)
    if N % 4 == 0:
        print(N + 1)
    else:
        print(N - 1)

if __name__ == '__main__':
    solve()