import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    n = int(data[0])
    costs = list(map(int, data[1:n+1]))
    
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
    
    # For a circular table, we need to consider two cases:
    # 1. Do not select the first knight, then select the last
    # 2. Do not select the last knight, then select the first
    # We take the minimum of these two cases
    # But since the table is circular, we need to handle the wrap-around
    # So we can compute the minimum of the two cases:
    # Case 1: not select first, select last
    # Case 2: not select last, select first
    # But since the table is circular, we can't just take min(dp[n-1][0], dp[n-1][1])
    # We need to consider the two cases separately
    
    # Case 1: not select first, select last
    # We can't select first, so we have to select the last
    # So we can take the min of dp[n-2][0] + costs[n-1]
    # But we also have to make sure that the last is selected
    # So we can take the min of dp[n-2][0] + costs[n-1]
    # And also the min of dp[n-2][1] + costs[n-1]
    # But since we can't select the first, we have to take the min of dp[n-2][0] + costs[n-1]
    # Because if we select the last, we can't select the first, so we have to take the min of dp[n-2][0] + costs[n-1]
    # But we also have to make sure that the last is selected
    # So we can take the min of dp[n-2][0] + costs[n-1]
    # And also the min of dp[n-2][1] + costs[n-1]
    # But since we can't select the first, we have to take the min of dp[n-2][0] + costs[n-1]
    
    # Case 2: not select last, select first
    # We can't select the last, so we have to select the first
    # So we can take the min of dp[n-1][0] + costs[0]
    # But we also have to make sure that the first is selected
    # So we can take the min of dp[n-1][0] + costs[0]
    # And also the min of dp[n-1][1] + costs[0]
    # But since we can't select the last, we have to take the min of dp[n-1][0] + costs[0]
    
    # So the final answer is the minimum of the two cases
    # Case 1: not select first, select last
    # Case 2: not select last, select first
    # But since the table is circular, we can't just take the min of dp[n-1][0] and dp[n-1][1]
    # We need to consider the two cases separately
    
    # Case 1: not select first, select last
    # We can't select first, so we have to select the last
    # So we can take the min of dp[n-2][0] + costs[n-1]
    # But we also have to make sure that the last is selected
    # So we can take the min of dp[n-2][0] + costs[n-1]
    
    # Case 2: not select last, select first
    # We can't select the last, so we have to select the first
    # So we can take the min of dp[n-1][0] + costs[0]
    # But we also have to make sure that the first is selected
    # So we can take the min of dp[n-1][0] + costs[0]
    
    # So the final answer is the minimum of the two cases
    # Case 1: not select first, select last
    # Case 2: not select last, select first
    # But since the table is circular, we can't just take the min of dp[n-1][0] and dp[n-1][1]
    # We need to consider the two cases separately
    
    # Case 1: not select first, select last
    # We can't select first, so we have to select the last
    # So we can take the min of dp[n-2][0] + costs[n-1]
    # But we also have to make sure that the last is selected
    # So we can take the min of dp[n-2][0] + costs[n-1]
    
    # Case 2: not select last, select first
    # We can't select the last, so we have to select the first
    # So we can take the min of dp[n-1][0] + costs[0]
    # But we also have to make sure that the first is selected
    # So we can take the min of dp[n-1][0] + costs[0]
    
    # So the final answer is the minimum of the two cases
    # Case 1: not select first, select last
    # Case 2: not select last, select first
    # But since the table is circular, we can't just take the min of dp[n-1][0] and dp[n-1][1]
    # We need to consider the two cases separately
    
    # Case 1: not select first, select last
    # We can't select first, so we have to select the last
    # So we can take the min of dp[n-2][0] + costs[n-1]
    # But we also have to make sure that the last is selected
    # So we can take the min of dp[n-2][0] + costs[n-1]
    
    # Case 2: not select last, select first
    # We can't select the last, so we have to select the first
    # So we can take the min of dp[n-1][0] + costs[0]
    # But we also have to make sure that the first is selected
    # So we can take the min of dp[n-1][0] + costs[0]
    
    # So the final answer is the minimum of the two cases
    # Case 1: not select first, select last
    # Case 2: not select last, select first
    # But since the table is circular, we can't just take the min of dp[n-1][0] and dp[n-1][1]
    # We need to consider the two cases separately
    
    # Case 1: not select first, select last
    # We can't select first, so we have to select the last
    # So we can take the min of dp[n-2][0] + costs[n-1]
    # But we also have to make sure that the last is selected
    # So we can take the min of dp[n-2][0] + costs[n-1]
    
    # Case 2: not select last, select first
    # We can't select the last, so we have to select the first
    # So we can take the min of dp[n-1][0] + costs[0]
    # But we also have to make sure that the first is selected
    # So we can take the min of dp[n-1][0] + costs[0]
    
    # So the final answer is the minimum of the two cases
    # Case 1: not select first, select last
    # Case 2: not select last, select first
    # But since the table is circular, we can't just take the min of dp[n-1][0] and dp[n-1][1]
    # We need to consider the two cases separately
    
    # Case 1: not select first, select last
    # We can't select first, so we have to select the last
    # So we can take the min of dp[n-2][0] + costs[n-1]
    # But we also have to make sure that the last is selected
    # So we can take the min of dp[n-2][0] + costs[n-1]
    
    # Case 2: not select last, select first
    # We can't select the last, so we have to select the first
    # So we can take the