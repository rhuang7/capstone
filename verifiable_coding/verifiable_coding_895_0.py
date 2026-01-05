import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    N = int(data[0])
    costs = list(map(int, data[1:]))

    if N == 1:
        print(costs[0])
        return

    # Dynamic programming approach for circular arrangement
    # dp[i][0] = min cost for first i knights, not selecting i-th
    # dp[i][1] = min cost for first i knights, selecting i-th
    dp = [[0] * 2 for _ in range(N)]

    dp[0][0] = 0
    dp[0][1] = costs[0]

    for i in range(1, N):
        dp[i][0] = dp[i-1][1]
        dp[i][1] = min(dp[i-1][0], dp[i-1][1]) + costs[i]

    # For circular arrangement, we have two cases:
    # 1. Do not select the first knight, then select the rest (excluding last)
    # 2. Do not select the last knight, then select the rest (excluding first)
    # We take the minimum of these two cases
    option1 = dp[N-2][1]
    option2 = dp[N-1][0]

    print(min(option1, option2))

if __name__ == '__main__':
    solve()