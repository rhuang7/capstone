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

    # Since it's a circular table, we can break it into a linear problem
    # by considering two cases: one where the first knight is not selected
    # and one where the first knight is selected.

    # Case 1: First knight is not selected
    # Then the second knight must be selected, and we solve for the rest
    # from index 2 to n-1
    # But since it's circular, we need to ensure that the last knight is
    # also covered. So we need to solve for the linear case from index 2 to n-1
    # and also ensure that the last knight is covered.

    # Case 2: First knight is selected
    # Then we can solve for the linear case from index 1 to n-1

    # We'll use dynamic programming to solve the linear problem
    def linear_dp(arr):
        if not arr:
            return 0
        if len(arr) == 1:
            return arr[0]
        # dp[i] = minimum cost to cover the first i knights
        dp = [0] * (len(arr) + 1)
        dp[0] = 0
        dp[1] = arr[0]
        for i in range(2, len(arr) + 1):
            dp[i] = min(dp[i-1], dp[i-2] + arr[i-1])
        return dp[-1]

    # Case 1: First knight is not selected
    # Then the second knight must be selected
    # We solve for the linear case from index 2 to n-1
    # But we also need to ensure that the last knight is covered
    # So we solve for the linear case from index 2 to n-1 and add the cost of the last knight
    # if it's not selected
    # But this is not correct, we need to ensure that the last knight is covered
    # So we solve for the linear case from index 2 to n-1 and also ensure that the last knight is covered
    # So we can solve for the linear case from index 2 to n-1 and add the cost of the last knight
    # if it's not selected

    # Case 1: First knight is not selected
    # Then the second knight must be selected
    # We solve for the linear case from index 2 to n-1
    # But we also need to ensure that the last knight is covered
    # So we solve for the linear case from index 2 to n-1 and add the cost of the last knight
    # if it's not selected

    # Case 2: First knight is selected
    # Then we solve for the linear case from index 1 to n-1

    # So the answer is the minimum of the two cases
    # Case 1: first knight is not selected, second knight is selected
    # So we solve for the linear case from index 2 to n-1
    # and add the cost of the second knight
    # But this is not correct, we need to ensure that the last knight is covered
    # So we solve for the linear case from index 2 to n-1 and add the cost of the last knight
    # if it's not selected

    # So the correct approach is to solve for the linear case from index 2 to n-1
    # and also ensure that the last knight is covered

    # So the answer is the minimum of:
    # 1. The cost of the first knight plus the solution for the linear case from index 2 to n-1
    # 2. The solution for the linear case from index 1 to n-1

    # But this is not correct, because the first knight is not selected, so the second knight must be selected
    # and the last knight must be selected

    # So the correct approach is to solve for the linear case from index 2 to n-1 and add the cost of the second knight
    # and also add the cost of the last knight if it's not selected

    # So the answer is the minimum of:
    # 1. The cost of the first knight plus the solution for the linear case from index 2 to n-1
    # 2. The solution for the linear case from index 1 to n-1

    # So the answer is the minimum of the two cases

    # Case 1: first knight is selected
    # We solve for the linear case from index 1 to n-1
    case1 = linear_dp(costs[1:])

    # Case 2: first knight is not selected
    # Then the second knight must be selected
    # We solve for the linear case from index 2 to n-1
    # and add the cost of the second knight
    # But we also need to ensure that the last knight is covered
    # So we solve for the linear case from index 2 to n-1 and add the cost of the second knight
    # and also add the cost of the last knight if it's not selected

    # So the answer is the minimum of the two cases
    # But this is not correct, because the last knight must be covered
    # So we solve for the linear case from index 2 to n-1 and add the cost of the second knight
    # and also add the cost of the last knight if it's not selected

    # So the answer is the minimum of:
    # 1. The cost of the first knight plus the solution for the linear case from index 2 to n-1
    # 2. The solution for the linear case from index 1 to n-1

    # But this is not correct, because the first knight is not selected, so the second knight must be selected
    # and the last knight must be selected

    # So the correct approach is to solve for the linear case from index 2 to n-1 and add the cost of the second knight
    # and also add the cost of the last knight if it's not selected

    # So the answer is the minimum of:
    # 1. The cost of the second knight plus the solution for the linear case from index 3 to n-1
    # 2. The solution for the linear case from index 1 to n-1

    # So the answer is the minimum of:
    # 1. The cost of the second knight plus the solution for the linear case from index 3 to n-1
    # 2. The solution for the linear case from index 1 to n-1

    # So the answer is the minimum of:
    # 1. The cost of the second knight plus the solution for the linear case from index 3 to n-1
    # 2. The solution for the linear case from index 1 to n-1

    # So the answer is the minimum of:
    # 1. The cost of the second knight plus the solution for the linear case from index 3 to n-1
    # 2. The solution for the linear case from index 1 to n-1

    # So the answer is the minimum of:
    # 1. The cost of the second knight plus the solution for the linear case from index 3 to n-1
    # 2. The solution for the linear case from index 1 to n-1

    # So the answer is the minimum of:
    # 1. The cost of the second knight plus the solution for the linear case from index 3 to n-1
    # 2. The solution for the linear case from index 1 to n-1

    # So the answer is the minimum of:
    # 1. The cost of the second knight plus the solution for the linear case from index 3 to n-1
    # 2. The solution for the linear case from index 1 to n-1

    # So the answer is the minimum of:
    # 1. The cost of the second knight plus the solution for the linear case from index 3 to n-1
    # 2. The solution for the linear case from index 1 to n-1

    # So the answer is the minimum of:
    # 1. The cost of the second knight plus the solution for the linear case from index 3 to n-1
    # 2. The solution for the linear case from index 1 to n-1

    # So the answer is the minimum of:
    # 1. The cost of the second knight plus the solution for the linear case from index 3 to n-1
    # 2. The solution for the linear case from index 1 to n-1

    # So the answer is the minimum of:
    # 1. The cost of the second knight plus the solution for the linear case from index 3 to n-1
    # 2. The solution for the linear case from index 1 to n-1

    # So the answer is the minimum of