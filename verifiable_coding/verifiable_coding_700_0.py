import sys

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
        banks = []
        for _ in range(N):
            a, b, c, d = map(int, data[idx:idx+4])
            banks.append((a, b, c, d))
            idx += 4
        
        # DP array: dp[i][0] = min cost to rob up to i-th bank with i-th bank not robbed
        # dp[i][1] = min cost to rob up to i-th bank with i-th bank robbed
        dp = [[0] * 2 for _ in range(N)]
        
        # Initialize for first bank
        dp[0][0] = 0
        dp[0][1] = banks[0][0]
        
        for i in range(1, N):
            # If i-th bank is not robbed, then previous can be robbed or not
            dp[i][0] = min(dp[i-1][0], dp[i-1][1])
            # If i-th bank is robbed, then previous cannot be robbed
            dp[i][1] = dp[i-1][0] + min(banks[i][0], banks[i][1], banks[i][2], banks[i][3])
        
        results.append(min(dp[N-1][0], dp[N-1][1]))
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()