import sys

def solve():
    import sys
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    for i in range(1, T + 1):
        N = int(input[i])
        last = N % 10
        first = N
        while first >= 10:
            first //= 10
        print(first + last)

if __name__ == '__main__':
    solve()