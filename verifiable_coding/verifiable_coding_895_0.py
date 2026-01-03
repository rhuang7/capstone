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
    # dp[i][0] = min cost to cover first i knights, not selecting i-th
    # dp[i][1] = min cost to cover first i knights, selecting i-th
    dp = [[0] * 2 for _ in range(n)]

    dp[0][0] = 0
    dp[0][1] = costs[0]

    for i in range(1, n):
        dp[i][0] = dp[i-1][1]
        dp[i][1] = min(dp[i-1][0], dp[i-1][1]) + costs[i]

    # Since the table is circular, we have to consider two cases:
    # 1. Not selecting the first knight
    # 2. Selecting the first knight
    # For case 1, we can't select the last knight
    # For case 2, we can't select the second last knight
    # So we compute the minimum of both cases

    # Case 1: Not selecting the first knight
    # We can select the last knight
    case1 = dp[n-1][0] + costs[-1]

    # Case 2: Selecting the first knight
    # We can't select the second last knight
    case2 = dp[n-2][1]

    print(min(case1, case2))

if __name__ == '__main__':
    solve()