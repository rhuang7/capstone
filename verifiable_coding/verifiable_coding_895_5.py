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

    # Convert to a circular array
    costs = costs + costs

    # Dynamic programming approach
    # dp[i][0] = min cost to cover first i knights, not covering i-th
    # dp[i][1] = min cost to cover first i knights, covering i-th
    dp = [[0] * 2 for _ in range(n)]

    dp[0][0] = 0
    dp[0][1] = costs[0]

    for i in range(1, n):
        dp[i][0] = dp[i-1][1]
        dp[i][1] = min(dp[i-1][0], dp[i-1][1]) + costs[i]

    result = min(dp[n-1][0], dp[n-1][1])
    print(result)

if __name__ == '__main__':
    solve()