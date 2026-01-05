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
    
    # dp[i][j] = maximum sum for the first i opening brackets and j closing brackets
    dp = [[-float('inf')]*(len(close_brackets)+1) for _ in range(len(open_brackets)+1)]
    dp[0][0] = 0
    
    for i in range(len(open_brackets)+1):
        for j in range(len(close_brackets)+1):
            if i == 0 and j == 0:
                continue
            if i > 0:
                dp[i][j] = max(dp[i][j], dp[i-1][j] + (V[open_brackets[i-1]-1] if open_brackets[i-1] in open_brackets else 0))
            if j > 0:
                dp[i][j] = max(dp[i][j], dp[i][j-1] + (V[close_brackets[j-1]-1] if close_brackets[j-1] in close_brackets else 0))
    
    max_sum = max(max(row) for row in dp)
    print(max_sum if max_sum != -float('inf') else 0)

if __name__ == '__main__':
    solve()