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
    # We'll use a dictionary to map opening brackets to their closing counterparts
    bracket_map = {i: i + k for i in range(1, k + 1)}
    
    # dp[i][j] = maximum sum for the first i opening brackets and j closing brackets
    # We'll use a 2D array to store the DP values
    # Since k can be up to 7, the maximum number of opening brackets is 7
    # So the DP array can be of size (k+1) x (k+1)
    dp = [[-float('inf')] * (k + 1) for _ in range(k + 1)]
    dp[0][0] = 0
    
    for i in range(1, k + 1):
        for j in range(1, k + 1):
            # Try to match the i-th opening bracket with the j-th closing bracket
            # Only if the closing bracket is the corresponding one for the opening bracket
            if bracket_map[i] == j:
                # We can take the i-th opening bracket and the j-th closing bracket
                # So we take the value of the i-th opening bracket and the j-th closing bracket
                # And add it to the dp[i-1][j-1]
                dp[i][j] = dp[i-1][j-1] + V[open_brackets[i-1]-1] + V[close_brackets[j-1]-1]
            # Also consider not taking the i-th opening bracket
            dp[i][j] = max(dp[i][j], dp[i-1][j])
            # Also consider not taking the j-th closing bracket
            dp[i][j] = max(dp[i][j], dp[i][j-1])
    
    # The maximum sum is the maximum value in dp[k][k]
    print(max(dp[k][k], 0))

if __name__ == '__main__':
    solve()