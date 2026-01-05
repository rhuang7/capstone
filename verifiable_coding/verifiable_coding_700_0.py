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
        # DP approach
        # dp[i][0] = min cost to rob up to i-th bank with i-th bank not robbed
        # dp[i][1] = min cost to rob up to i-th bank with i-th bank robbed
        # Initialize
        dp_prev_not = float('inf')
        dp_prev_yes = float('inf')
        # First bank
        a, b, c, d = banks[0]
        dp_prev_not = min(a, b, c, d)
        dp_prev_yes = min(a, b, c, d)
        # Iterate from second bank
        for i in range(1, N):
            a, b, c, d = banks[i]
            # Current not robbed
            current_not = min(dp_prev_yes + a, dp_prev_not + b, dp_prev_yes + c, dp_prev_not + d)
            # Current robbed
            current_yes = min(dp_prev_not + a, dp_prev_not + b, dp_prev_not + c, dp_prev_not + d)
            dp_prev_not, dp_prev_yes = current_not, current_yes
        results.append(min(dp_prev_not, dp_prev_yes))
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()