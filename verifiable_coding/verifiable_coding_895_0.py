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

    # We need to find the minimum cost such that for every pair of adjacent knights, at least one gets dessert.
    # This is equivalent to finding a vertex cover in a cycle graph.
    # For a cycle graph, the minimum vertex cover can be found using dynamic programming.

    # Convert the cycle into a linear array by duplicating the first element at the end.
    costs = costs + costs[:1]

    # dp[i][0] = minimum cost to cover the first i knights, with the i-th not selected
    # dp[i][1] = minimum cost to cover the first i knights, with the i-th selected
    dp = [[0] * 2 for _ in range(n + 1)]

    dp[1][0] = 0  # first knight not selected, but since it's a cycle, this is not valid
    dp[1][1] = costs[0]

    for i in range(2, n + 1):
        dp[i][0] = dp[i - 1][1]  # i-th not selected, so i-1 must be selected
        dp[i][1] = min(dp[i - 1][0], dp[i - 1][1]) + costs[i - 1]  # i-th selected

    # For a cycle, we cannot select both first and last knight
    # So we consider two cases: first knight is not selected, last knight is selected
    # and first knight is selected, last knight is not selected
    result = min(dp[n][0], dp[n][1])
    print(result)

if __name__ == '__main__':
    solve()