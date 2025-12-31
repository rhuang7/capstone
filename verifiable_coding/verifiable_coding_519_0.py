import sys

def solve():
    import sys
    input = sys.stdin.buffer.read().split()
    idx = 0
    N = int(input[idx]); idx += 1
    k = int(input[idx]); idx += 1
    V = list(map(int, input[idx:idx+N])); idx += N
    B = list(map(int, input[idx:idx+N]))
    
    # Preprocess B to separate opening and closing brackets
    open_brackets = []
    close_brackets = []
    for b in B:
        if b <= k:
            open_brackets.append(b)
        else:
            close_brackets.append(b)
    
    # For each opening bracket, find the corresponding closing bracket
    # We'll use a dictionary to map opening brackets to their corresponding closing brackets
    bracket_map = {i: i + k for i in range(1, k + 1)}
    
    # We'll use dynamic programming to solve this problem
    # dp[i][j] represents the maximum sum for the first i opening brackets and j closing brackets
    # We'll use a 2D array for DP
    # Since k can be up to 7, the maximum number of opening brackets is k, and the same for closing
    # So the DP table size is (k+1) x (k+1)
    dp = [[-float('inf')] * (k + 1) for _ in range(k + 1)]
    dp[0][0] = 0  # Base case: no brackets used
    
    for i in range(1, k + 1):
        for j in range(1, k + 1):
            # Try to match the i-th opening bracket with the j-th closing bracket
            if bracket_map[i] == j:
                # If this is a valid pair, we can take the value of this bracket
                # And add it to the maximum sum from the previous state
                dp[i][j] = max(dp[i][j], dp[i-1][j-1] + V[B.index(bracket_map[i])])
            # Try to not use the i-th opening bracket
            dp[i][j] = max(dp[i][j], dp[i-1][j])
            # Try to not use the j-th closing bracket
            dp[i][j] = max(dp[i][j], dp[i][j-1])
    
    # The answer is the maximum value in the dp table
    # We need to consider all possible combinations of opening and closing brackets
    # But we need to ensure that the brackets are used in a valid way
    # So we need to consider all possible combinations of opening and closing brackets
    # where the number of opening brackets is equal to the number of closing brackets
    # and the brackets are matched in a valid way
    max_sum = -float('inf')
    for i in range(1, k + 1):
        for j in range(1, k + 1):
            if i == j:
                max_sum = max(max_sum, dp[i][j])
    
    print(max_sum)

if __name__ == '__main__':
    solve()