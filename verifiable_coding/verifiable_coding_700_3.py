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
        # Dynamic programming approach
        # dp[i][0] = min cost to rob up to i-th bank with worker 0
        # dp[i][1] = min cost to rob up to i-th bank with worker 1
        # dp[i][2] = min cost to rob up to i-th bank with worker 2
        # dp[i][3] = min cost to rob up to i-th bank with worker 3
        # Initialize for first bank
        dp0 = min(banks[0][0], banks[0][1], banks[0][2], banks[0][3])
        dp1 = min(banks[0][0], banks[0][1], banks[0][2], banks[0][3])
        dp2 = min(banks[0][0], banks[0][1], banks[0][2], banks[0][3])
        dp3 = min(banks[0][0], banks[0][1], banks[0][2], banks[0][3])
        # Iterate through the rest of the banks
        for i in range(1, N):
            a, b, c, d = banks[i]
            new_dp0 = min(dp1, dp2, dp3) + a
            new_dp1 = min(dp0, dp2, dp3) + b
            new_dp2 = min(dp0, dp1, dp3) + c
            new_dp3 = min(dp0, dp1, dp2) + d
            dp0, dp1, dp2, dp3 = new_dp0, new_dp1, new_dp2, new_dp3
        results.append(min(dp0, dp1, dp2, dp3))
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()