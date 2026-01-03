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
    # We'll use a 2D array for dynamic programming
    dp = [[-float('inf')] * (len(close_brackets) + 1) for _ in range(len(open_brackets) + 1)]
    dp[0][0] = 0
    
    for i in range(len(open_brackets) + 1):
        for j in range(len(close_brackets) + 1):
            if i > 0:
                dp[i][j] = max(dp[i][j], dp[i-1][j])
            if j > 0:
                dp[i][j] = max(dp[i][j], dp[i][j-1])
            if i > 0 and j > 0:
                # Check if the current opening bracket can pair with the current closing bracket
                if bracket_map[open_brackets[i-1]] == close_brackets[j-1]:
                    dp[i][j] = max(dp[i][j], dp[i-1][j-1] + V[B.index(open_brackets[i-1])])
    
    # The answer is the maximum value in the last row and last column
    result = max(dp[len(open_brackets)][len(close_brackets)])
    print(result if result != -float('inf') else 0)

if __name__ == '__main__':
    solve()