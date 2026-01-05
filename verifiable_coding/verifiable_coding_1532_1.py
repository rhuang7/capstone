import sys
MOD = 10**9 + 7

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
        max_numbers = list(map(int, data[idx:idx+N]))
        idx += N
        max_numbers.sort()
        # Check if it's possible to choose N distinct numbers
        # The minimum possible maximum is N (1, 2, ..., N)
        # The maximum possible minimum is max_numbers[0]
        if max_numbers[0] < N:
            results.append(0)
            continue
        # Calculate the number of ways
        # We use dynamic programming
        dp = [0] * (N + 1)
        dp[0] = 1
        for i in range(N):
            for j in range(N, 0, -1):
                if max_numbers[i] >= j:
                    dp[j] = (dp[j] + dp[j-1]) % MOD
        results.append(dp[N])
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()