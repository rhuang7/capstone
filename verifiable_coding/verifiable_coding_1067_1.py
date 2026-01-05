import sys
MOD = 10**9 + 7

def solve():
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    for i in range(1, T + 1):
        N = int(data[i])
        if N == 1:
            print(4)
            continue
        if N == 2:
            print(6)
            continue
        a, b = 0, 0
        for _ in range(N - 1):
            a, b = b, (a * 3 + b * 2) % MOD
        print(b)

if __name__ == '__main__':
    solve()