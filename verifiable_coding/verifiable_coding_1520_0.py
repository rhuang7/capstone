import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    n = int(data[0])
    A = list(map(int, data[1:n+1]))
    
    # dp[i][x] = maximum length of subsequence ending at i with xor of last two elements as x
    # We use a dictionary to store the maximum length for each xor value
    dp = [{} for _ in range(n)]
    
    for i in range(n):
        # Start a new subsequence with just A[i]
        dp[i][0] = 1
        for j in range(i):
            xor = A[i] ^ A[j]
            # Check if we can extend the subsequence ending at j
            for prev_xor in dp[j]:
                if xor >= prev_xor:
                    if xor in dp[i]:
                        dp[i][xor] = max(dp[i][xor], dp[j][prev_xor] + 1)
                    else:
                        dp[i][xor] = dp[j][prev_xor] + 1
        # Also consider the subsequence consisting of just A[i]
        if 0 in dp[i]:
            dp[i][0] = max(dp[i][0], 1)
        else:
            dp[i][0] = 1
    
    # Find the maximum length among all subsequences
    max_len = 1
    for i in range(n):
        for length in dp[i].values():
            if length > max_len:
                max_len = length
    print(max_len)

if __name__ == '__main__':
    solve()