import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    n = int(data[0])
    costs = list(map(int, data[1:]))

    if n == 1:
        print(costs[0])
        return

    # dp[i][0] = min cost for first i knights, not selecting i-th
    # dp[i][1] = min cost for first i knights, selecting i-th
    dp = [[0] * 2 for _ in range(n)]
    dp[0][0] = 0
    dp[0][1] = costs[0]

    for i in range(1, n):
        dp[i][0] = dp[i-1][1]
        dp[i][1] = min(dp[i-1][0], dp[i-1][1]) + costs[i]

    # Since it's a circle, we have to consider two cases:
    # 1. Do not select the first knight
    # 2. Do not select the last knight
    # We take the minimum of these two cases
    res1 = dp[n-1][0]
    res2 = dp[n-2][1] + costs[n-1]
    print(min(res1, res2))

if __name__ == '__main__':
    solve()