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
    # dp[i][0] = min cost if knight i is not selected
    # dp[i][1] = min cost if knight i is selected
    # For circular arrangement, we need to handle two cases:
    # 1. Exclude the first knight (so the last knight is not excluded)
    # 2. Exclude the last knight (so the first knight is not excluded)

    # Case 1: Exclude the first knight
    dp1 = [0] * N
    dp1[0] = 0  # first knight is not selected
    dp1[1] = costs[1]  # second knight is selected
    for i in range(2, N):
        dp1[i] = min(dp1[i-1] + costs[i], dp1[i-2] + costs[i])

    # Case 2: Exclude the last knight
    dp2 = [0] * N
    dp2[0] = 0  # first knight is not selected
    dp2[1] = costs[1]  # second knight is selected
    for i in range(2, N-1):
        dp2[i] = min(dp2[i-1] + costs[i], dp2[i-2] + costs[i])

    # The last knight is not selected in case 2
    # So we take the minimum of the two cases
    result = min(dp1[-1], dp2[-1])
    print(result)

if __name__ == '__main__':
    solve()