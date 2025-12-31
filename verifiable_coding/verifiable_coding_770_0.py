import sys
import math

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    for _ in range(T):
        n, k = int(data[idx]), int(data[idx+1])
        idx += 2
        a = list(map(int, data[idx:idx+n]))
        idx += n
        
        # Separate even and odd numbers
        evens = []
        odds = []
        for i in range(n):
            if a[i] % 2 == 0:
                evens.append(a[i])
            else:
                odds.append(a[i])
        
        # Function to find maximum sum of elements with at most K distance between any two
        def max_sum(arr, k):
            dp = [0] * (len(arr) + 1)
            for i in range(1, len(arr) + 1):
                dp[i] = max(dp[i-1], arr[i-1])
                if i > k + 1:
                    dp[i] = max(dp[i], dp[i - k - 1] + arr[i-1])
            return dp[-1]
        
        # Compute max sum for even and odd
        max_even = max_sum(evens, k)
        max_odd = max_sum(odds, k)
        
        # The answer is the sum of the max even and max odd
        results.append(str(max_even + max_odd))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()