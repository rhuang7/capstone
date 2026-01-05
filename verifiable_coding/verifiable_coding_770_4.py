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
        
        # Function to find maximum sum of elements with no two within distance k
        def max_sum(arr, k):
            # We can take at most one element from each window of size k+1
            # So we can use a greedy approach: take the maximum in each window
            # But since we can take elements from different windows, we need to use dynamic programming
            # Let's use dynamic programming
            dp = [0] * (len(arr) + 1)
            for i in range(1, len(arr) + 1):
                # Option 1: take the current element
                # We can't take any element in the previous k positions
                max_prev = 0
                for j in range(1, min(i, k) + 1):
                    max_prev = max(max_prev, dp[i - j])
                dp[i] = max(dp[i - 1], arr[i - 1] + max_prev)
                # Option 2: don't take the current element
                dp[i] = max(dp[i], dp[i - 1])
            return dp[-1]
        
        max_even = max_sum(evens, k)
        max_odd = max_sum(odds, k)
        results.append(max_even + max_odd)
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()