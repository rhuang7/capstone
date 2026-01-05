import sys
import math

def compute_gcd(arr):
    return math.gcd(*arr)

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    for _ in range(T):
        N, K = int(data[idx]), int(data[idx+1])
        idx += 2
        arr = list(map(int, data[idx:idx+N]))
        idx += N
        # Compute prefix gcds
        prefix_gcd = [0] * N
        prefix_gcd[0] = arr[0]
        for i in range(1, N):
            prefix_gcd[i] = math.gcd(prefix_gcd[i-1], arr[i])
        # Dynamic programming
        dp = [[0] * (K+1) for _ in range(N+1)]
        # Base case: 0 elements, 0 partitions
        dp[0][0] = 0
        # Fill dp
        for i in range(1, N+1):
            for j in range(1, K+1):
                if j == 1:
                    dp[i][j] = prefix_gcd[i-1]
                else:
                    dp[i][j] = max(dp[i-1][j-1] + compute_gcd(arr[i-1:]), dp[i-1][j])
        results.append(dp[N][K])
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()