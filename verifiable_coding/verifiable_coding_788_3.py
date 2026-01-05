import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    for i in range(1, T + 1):
        N = int(data[i])
        first = N
        while first >= 10:
            first //= 10
        last = N % 10
        print(first + last)

if __name__ == '__main__':
    solve()