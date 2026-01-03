import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    for i in range(1, T+1):
        n = int(data[i])
        print(2 * n * n - 2 * n + 2)

if __name__ == '__main__':
    solve()