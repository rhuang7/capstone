import sys

def solve():
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    for i in range(1, T + 1):
        N = int(input[i])
        total = 0
        for k in range(1, N + 1, 2):
            total += (N - k + 1) * (N - k + 2) // 2
        print(total)

if __name__ == '__main__':
    solve()