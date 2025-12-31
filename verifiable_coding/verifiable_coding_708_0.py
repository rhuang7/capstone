import sys
MOD = 10**9 + 7

def solve():
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    idx = 1
    for _ in range(T):
        N = int(data[idx])
        A = int(data[idx+1])
        idx += 2
        if N == 0:
            print(0)
            continue
        res = 0
        p = 1
        for i in range(1, N+1):
            cnt = 2 * i - 1
            if cnt == 1:
                res = (res + p * A) % MOD
            else:
                res = (res + p * A * (A - 1) * (A - 2) // 2) % MOD
            p = (p * (A - 1) * (A - 2) // 2) % MOD
        print(res % MOD)

if __name__ == '__main__':
    solve()