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
    opening = []
    closing = []
    for b in B:
        if b <= k:
            opening.append(b)
        else:
            closing.append(b)
    
    # For each opening bracket, find the corresponding closing bracket
    # We'll use a stack to find matching pairs
    stack = []
    bracket_pairs = {}
    for i, b in enumerate(B):
        if b <= k:
            stack.append((b, i))
        else:
            if stack:
                top = stack[-1]
                bracket_pairs[(top[0], b)] = (top[1], i)
                stack.pop()
    
    # Now we need to find the maximum sum of values such that the bracket sequence is well-bracketed
    # We'll use dynamic programming
    # dp[i][j] = maximum sum for the first i brackets, with the last bracket being the j-th opening bracket
    # We'll use a 2D array where dp[i][j] represents the maximum sum for the first i brackets and the last opening bracket is j
    # We'll also track the matching closing bracket for each opening bracket
    # Since k can be up to 7, the size of the DP table is manageable
    
    # Initialize DP table
    dp = [[-float('inf')] * (k + 1) for _ in range(N + 1)]
    dp[0][0] = 0  # Base case: 0 brackets, 0 opening brackets
    
    for i in range(1, N + 1):
        for j in range(1, k + 1):
            # If current bracket is an opening bracket
            if B[i - 1] == j:
                # We can take this bracket as a new opening bracket
                # So we can take the value of this bracket and add it to the previous state
                dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + V[i - 1])
                # Also, we can take this bracket as a closing bracket for a previous opening bracket
                # So we need to check if there's a matching pair
                if j in bracket_pairs:
                    # Find the matching closing bracket
                    if B[i - 1] in bracket_pairs:
                        # Get the matching opening bracket and its index
                        opening_bracket, closing_index = bracket_pairs[B[i - 1]]
                        # Check if the closing bracket is at position i - 1
                        if closing_index == i - 1:
                            # We can take this closing bracket and add it to the previous state
                            dp[i][j] = max(dp[i][j], dp[i - 1][opening_bracket] + V[i - 1])
            else:
                # If current bracket is a closing bracket
                # We need to find if there's a matching opening bracket
                # Check if there's a matching pair for this closing bracket
                if B[i - 1] in bracket_pairs:
                    # Get the matching opening bracket and its index
                    opening_bracket, closing_index = bracket_pairs[B[i - 1]]
                    # Check if the closing bracket is at position i - 1
                    if closing_index == i - 1:
                        # We can take this closing bracket and add it to the previous state
                        dp[i][j] = max(dp[i][j], dp[i - 1][opening_bracket] + V[i - 1])
    
    # The answer is the maximum value in the last row of the DP table
    result = max(dp[N][j] for j in range(k + 1))
    print(result)

if __name__ == '__main__':
    solve()