import sys
MOD = 10**9 + 7

def solve():
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    for _ in range(T):
        N = int(data[idx])
        idx += 1
        B = list(map(int, data[idx:idx+N]))
        idx += N
        if B[0] == 0:
            results.append(1)
            continue
        if B[0] != B[1]:
            results.append(0)
            continue
        dp = [0] * (N + 1)
        dp[0] = 1
        for i in range(1, N + 1):
            if i == 1:
                if B[0] == 0:
                    dp[i] = 1
                else:
                    dp[i] = 1
            else:
                if B[i-1] != B[i-2]:
                    dp[i] = 0
                else:
                    dp[i] = (dp[i-1] * 2) % MOD
        results.append(dp[N])
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()