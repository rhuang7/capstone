import sys
import math

def compute_gcd(arr):
    gcd_val = arr[0]
    for num in arr[1:]:
        gcd_val = math.gcd(gcd_val, num)
        if gcd_val == 1:
            break
    return gcd_val

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
        # If K is 1, the sum is the GCD of the entire array
        if K == 1:
            results.append(compute_gcd(arr))
            continue
        # If K is greater than the number of elements, it's impossible
        if K > N:
            results.append(0)
            continue
        # Precompute prefix GCDs
        prefix_gcd = [0] * N
        prefix_gcd[0] = arr[0]
        for i in range(1, N):
            prefix_gcd[i] = math.gcd(prefix_gcd[i-1], arr[i])
        # dp[i][j] = maximum sum for first i elements divided into j parts
        dp = [[-1] * (K+1) for _ in range(N+1)]
        dp[0][0] = 0
        for i in range(1, N+1):
            for j in range(1, K+1):
                if j > i:
                    continue
                # Try all possible positions to split
                for m in range(j-1, i):
                    if dp[m][j-1] != -1:
                        current_gcd = compute_gcd(arr[m:i])
                        dp[i][j] = max(dp[i][j], dp[m][j-1] + current_gcd)
        results.append(dp[N][K])
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()