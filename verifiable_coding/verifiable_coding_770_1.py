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
        
        # For even numbers, we can take at most one in every k+1 consecutive elements
        # So we can take the maximum sum of a subsequence where no two elements are within k distance
        # This is similar to the maximum sum of a subsequence with no two elements within k distance
        # We can use dynamic programming for this
        
        # Function to compute maximum sum of a subsequence with no two elements within k distance
        def max_subsequence_sum(arr, k):
            n = len(arr)
            dp = [0] * (n + 1)
            for i in range(1, n + 1):
                dp[i] = max(dp[i-1], dp[i-1 - k] + arr[i-1])
            return dp[n]
        
        max_even = max_subsequence_sum(evens, k)
        max_odd = max_subsequence_sum(odds, k)
        results.append(str(max_even + max_odd))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()