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
        # Dynamic programming
        # dp[i][0] = min cost to rob up to i-th bank with i-th bank not robbed
        # dp[i][1] = min cost to rob up to i-th bank with i-th bank robbed
        # Initialize for first bank
        dp0 = [0] * N
        dp1 = [0] * N
        a, b, c, d = banks[0]
        dp0[0] = 0
        dp1[0] = min(a, b, c, d)
        for i in range(1, N):
            a_i, b_i, c_i, d_i = banks[i]
            # If i-th bank is not robbed, then previous can be robbed or not
            dp0[i] = min(dp0[i-1], dp1[i-1])
            # If i-th bank is robbed, then previous cannot be robbed
            dp1[i] = dp0[i-1] + min(a_i, b_i, c_i, d_i)
        results.append(min(dp0[-1], dp1[-1]))
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()