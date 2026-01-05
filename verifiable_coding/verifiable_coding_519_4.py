import sys

def solve():
    import sys
    input = sys.stdin.buffer.read().split()
    idx = 0
    N = int(input[idx])
    idx += 1
    k = int(input[idx])
    idx += 1
    V = list(map(int, input[idx:idx+N]))
    idx += N
    B = list(map(int, input[idx:idx+N]))
    
    # Preprocess: separate opening and closing brackets
    open_brackets = []
    close_brackets = []
    for i in range(N):
        if B[i] <= k:
            open_brackets.append((B[i], i))
        else:
            close_brackets.append((B[i], i))
    
    # Sort opening brackets by value, closing brackets by value
    open_brackets.sort()
    close_brackets.sort()
    
    # dp[i][j] = maximum sum for the first i opening brackets and j closing brackets
    dp = [[-float('inf')] * (len(close_brackets) + 1) for _ in range(len(open_brackets) + 1)]
    dp[0][0] = 0
    
    for i in range(len(open_brackets) + 1):
        for j in range(len(close_brackets) + 1):
            if i > 0:
                dp[i][j] = max(dp[i][j], dp[i-1][j] + V[open_brackets[i-1][1]])
            if j > 0:
                dp[i][j] = max(dp[i][j], dp[i][j-1] + V[close_brackets[j-1][1]])
    
    # Find the maximum sum where the number of opening and closing brackets are equal
    max_sum = -float('inf')
    for i in range(1, len(open_brackets) + 1):
        for j in range(1, len(close_brackets) + 1):
            if i == j:
                max_sum = max(max_sum, dp[i][j])
    
    print(max_sum if max_sum != -float('inf') else 0)

if __name__ == '__main__':
    solve()