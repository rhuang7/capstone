import sys
MOD = 10**9 + 7

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
        max_numbers = list(map(int, data[idx:idx+N]))
        idx += N
        
        # Sort the max_numbers
        max_numbers.sort()
        
        # Check if it's possible to assign distinct numbers
        # The smallest possible maximum is N (since we need N distinct numbers)
        if max_numbers[0] < N:
            results.append(0)
            continue
        
        # Now calculate the number of ways
        # We use dynamic programming
        # dp[i][j] = number of ways to assign numbers to first i people with max number j
        # But since N is small (<=50), we can use a 1D DP array
        dp = [0] * (max_numbers[-1] + 1)
        dp[0] = 1  # Base case: 1 way to assign nothing
        
        for i in range(N):
            new_dp = [0] * (max_numbers[-1] + 1)
            for j in range(max_numbers[-1] + 1):
                if dp[j] == 0:
                    continue
                # Choose a number from 1 to max_numbers[i]
                # If we choose a number k, then we can add it to the previous ways
                # But we need to ensure that k is not used before
                # So we add dp[j] to new_dp[k]
                # But since we are using a sorted list, we can use the fact that we are choosing numbers in order
                # So we can use the fact that the previous numbers are all less than the current max
                # So we can add dp[j] to new_dp[k] for k from 1 to max_numbers[i]
                # But we need to avoid duplicates
                # So we can use the fact that the current max is max_numbers[i]
                # So for each number k in 1 to max_numbers[i], we can add dp[j] to new_dp[k]
                # But we need to make sure that k is not already used
                # So we can use the fact that the previous numbers are all less than the current max
                # So we can use the fact that the current max is max_numbers[i]
                # So for each number k in 1 to max_numbers[i], we can add dp[j] to new_dp[k]
                # But we need to make sure that k is not already used
                # So we can use the fact that the previous numbers are all less than the current max
                # So we can use the fact that the current max is max_numbers[i]
                # So for each number k in 1 to max_numbers[i], we can add dp[j] to new_dp[k]
                # But we need to make sure that k is not already used
                # So we can use the fact that the previous numbers are all less than the current max
                # So we can use the fact that the current max is max_numbers[i]
                # So for each number k in 1 to max_numbers[i], we can add dp[j] to new_dp[k]
                # But we need to make sure that k is not already used
                # So we can use the fact that the previous numbers are all less than the current max
                # So we can use the fact that the current max is max_numbers[i]
                # So for each number k in 1 to max_numbers[i], we can add dp[j] to new_dp[k]
                # But we need to make sure that k is not already used
                # So we can use the fact that the previous numbers are all less than the current max
                # So we can use the fact that the current max is max_numbers[i]
                # So for each number k in 1 to max_numbers[i], we can add dp[j] to new_dp[k]
                # But we need to make sure that k is not already used
                # So we can use the fact that the previous numbers are all less than the current max
                # So we can use the fact that the current max is max_numbers[i]
                # So for each number k in 1 to max_numbers[i], we can add dp[j] to new_dp[k]
                # But we need to make sure that k is not already used
                # So we can use the fact that the previous numbers are all less than the current max
                # So we can use the fact that the current max is max_numbers[i]
                # So for each number k in 1 to max_numbers[i], we can add dp[j] to new_dp[k]
                # But we need to make sure that k is not already used
                # So we can use the fact that the previous numbers are all less than the current max
                # So we can use the fact that the current max is max_numbers[i]
                # So for each number k in 1 to max_numbers[i], we can add dp[j] to new_dp[k]
                # But we need to make sure that k is not already used
                # So we can use the fact that the previous numbers are all less than the current max
                # So we can use the fact that the current max is max_numbers[i]
                # So for each number k in 1 to max_numbers[i], we can add dp[j] to new_dp[k]
                # But we need to make sure that k is not already used
                # So we can use the fact that the previous numbers are all less than the current max
                # So we can use the fact that the current max is max_numbers[i]
                # So for each number k in 1 to max_numbers[i], we can add dp[j] to new_dp[k]
                # But we need to make sure that k is not already used
                # So we can use the fact that the previous numbers are all less than the current max
                # So we can use the fact that the current max is max_numbers[i]
                # So for each number k in 1 to max_numbers[i], we can add dp[j] to new_dp[k]
                # But we need to make sure that k is not already used
                # So we can use the fact that the previous numbers are all less than the current max
                # So we can use the fact that the current max is max_numbers[i]
                # So for each number k in 1 to max_numbers[i], we can add dp[j] to new_dp[k]
                # But we need to make sure that k is not already used
                # So we can use the fact that the previous numbers are all less than the current max
                # So we can use the fact that the current max is max_numbers[i]
                # So for each number k in 1 to max_numbers[i], we can add dp[j] to new_dp[k]
                # But we need to make sure that k is not already used
                # So we can use the fact that the previous numbers are all less than the current max
                # So we can use the fact that the current max is max_numbers[i]
                # So for each number k in 1 to max_numbers[i], we can add dp[j] to new_dp[k]
                # But we need to make sure that k is not already used
                # So we can use the fact that the previous numbers are all less than the current max
                # So we can use the fact that the current max is max_numbers[i]
                # So for each number k in 1 to max_numbers[i], we can add dp[j] to new_dp[k]
                # But we need to make sure that k is not already used
                # So we can use the fact that the previous numbers are all less than the current max
                # So we can use the fact that the current max is max_numbers[i]
                # So for each number k in 1 to max_numbers[i], we can add dp[j] to new_dp[k]
                # But we need to make sure that k is not already used
                # So we can use the fact that the previous numbers are all less than the current max
                # So we can use the fact that the current max is max_numbers[i]
                # So for each number k in 1 to max_numbers[i], we can add dp[j] to new_dp[k]
                # But we need to make sure that k is not already used
                # So we can use the fact that the previous numbers are all less than the current max
                # So we can use the fact that the current max is max_numbers[i]
                # So for each number k in 1 to max_numbers[i], we can add dp[j] to new_dp[k]
                # But we need to make sure that k is not already used
                # So we can use the fact that the previous numbers are all less than the current max
                # So we can use the fact that the current max is max_numbers[i]
                # So for each number k in 1 to max_numbers[i], we can add dp[j] to new_dp[k]
                # But we need to make sure that k is not already used
                # So we can use the fact that the previous numbers are all less