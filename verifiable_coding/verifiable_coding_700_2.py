import sys

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
        banks = []
        for _ in range(N):
            a, b, c, d = map(int, data[idx:idx+4])
            banks.append((a, b, c, d))
            idx += 4
        # Dynamic programming
        # dp[i][0] = min cost to rob i-th bank with worker A
        # dp[i][1] = min cost to rob i-th bank with worker B
        # dp[i][2] = min cost to rob i-th bank with worker C
        # dp[i][3] = min cost to rob i-th bank with worker D
        # dp[i][j] = min(dp[i-1][k] for k in 0-3 if k != j) + cost[j]
        # Initialize for first bank
        dp0 = min(banks[0][1], banks[0][2], banks[0][3]) + banks[0][0]
        dp1 = min(banks[0][0], banks[0][2], banks[0][3]) + banks[0][1]
        dp2 = min(banks[0][0], banks[0][1], banks[0][3]) + banks[0][2]
        dp3 = min(banks[0][0], banks[0][1], banks[0][2]) + banks[0][3]
        for i in range(1, N):
            a, b, c, d = banks[i]
            new0 = min(dp1, dp2, dp3) + a
            new1 = min(dp0, dp2, dp3) + b
            new2 = min(dp0, dp1, dp3) + c
            new3 = min(dp0, dp1, dp2) + d
            dp0, dp1, dp2, dp3 = new0, new1, new2, new3
        results.append(min(dp0, dp1, dp2, dp3))
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()