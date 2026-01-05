import sys
import math

def compute_gcd(arr):
    current_gcd = arr[0]
    for num in arr[1:]:
        current_gcd = math.gcd(current_gcd, num)
        if current_gcd == 1:
            break
    return current_gcd

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
        # Precompute prefix gcds
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
                # Try all possible previous positions
                for k in range(i):
                    # If we split at k, then the last partition is from k+1 to i
                    # The gcd of the last partition is prefix_gcd[i-1] // prefix_gcd[k-1]
                    # But we need to compute the gcd of the subarray from k+1 to i
                    # So we need to compute the gcd of arr[k+1 ... i]
                    # Which is prefix_gcd[i-1] // prefix_gcd[k]
                    if k == 0:
                        last_gcd = prefix_gcd[i-1]
                    else:
                        last_gcd = math.gcd(prefix_gcd[i-1], prefix_gcd[k-1])
                    dp[i][j] = max(dp[i][j], dp[k][j-1] + last_gcd)
        results.append(dp[N][K])
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()