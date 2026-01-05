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
        # Dynamic programming approach
        # dp[i][0] = min cost to rob up to i-th bank with worker 0
        # dp[i][1] = min cost to rob up to i-th bank with worker 1
        # dp[i][2] = min cost to rob up to i-th bank with worker 2
        # dp[i][3] = min cost to rob up to i-th bank with worker 3
        # Initialize for first bank
        dp = [[0]*4 for _ in range(N)]
        for i in range(4):
            dp[0][i] = banks[0][i]
        # Fill dp table
        for i in range(1, N):
            for j in range(4):
                # If current worker is j, then previous worker can't be j-1 or j+1 (mod 4)
                min_prev = float('inf')
                for k in range(4):
                    if k != j:
                        min_prev = min(min_prev, dp[i-1][k])
                dp[i][j] = min_prev + banks[i][j]
        # The answer is the minimum of the last row
        results.append(min(dp[N-1]))
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()