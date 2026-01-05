import sys
MOD = 10**9 + 7

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    for _ in range(T):
        N = int(data[idx])
        idx += 1
        maxnumbers = list(map(int, data[idx:idx+N]))
        idx += N
        maxnumbers.sort()
        if maxnumbers[0] > 1:
            results.append(0)
            continue
        dp = [0] * (N + 1)
        dp[0] = 1
        for i in range(N):
            for j in range(N - i):
                dp[j + 1] = (dp[j + 1] + dp[j] * (maxnumbers[i] - j)) % MOD
        results.append(dp[N])
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()