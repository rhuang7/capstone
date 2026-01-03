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
        # DP approach
        # dp[i][0] = min cost to rob up to i-th bank with i-th bank not robbed
        # dp[i][1] = min cost to rob up to i-th bank with i-th bank robbed
        # Initialize for first bank
        dp0 = [0] * (N + 1)  # not robbed
        dp1 = [0] * (N + 1)  # robbed
        dp0[1] = 0
        dp1[1] = min(banks[0][0], banks[0][1], banks[0][2], banks[0][3])
        for i in range(2, N + 1):
            # current bank is i-th (0-based)
            a, b, c, d = banks[i - 1]
            # if current bank is not robbed, previous can be robbed or not
            dp0[i] = min(dp0[i - 1], dp1[i - 1])
            # if current bank is robbed, previous cannot be robbed
            dp1[i] = dp0[i - 1] + min(a, b, c, d)
        results.append(min(dp0[N], dp1[N]))
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()