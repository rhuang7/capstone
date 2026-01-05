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
        
        # Function to find maximum sum of elements with no two within distance K
        def max_sum(arr, k):
            dp = [0] * len(arr)
            dp[0] = arr[0]
            for i in range(1, len(arr)):
                # Check if we can take current element
                # Find the farthest element before i that is not within K distance
                left = 0
                right = i - 1
                pos = -1
                while left <= right:
                    mid = (left + right) // 2
                    if i - mid > k:
                        pos = mid
                        right = mid - 1
                    else:
                        left = mid + 1
                if pos != -1:
                    dp[i] = max(dp[i], arr[i] + dp[pos])
                else:
                    dp[i] = max(dp[i], arr[i])
                # Not take current element
                dp[i] = max(dp[i], dp[i-1])
            return dp[-1]
        
        max_even = 0
        if evens:
            max_even = max_sum(evens, k)
        max_odd = 0
        if odds:
            max_odd = max_sum(odds, k)
        results.append(str(max_even + max_odd))
    
    sys.stdout.write('\n'.join(results) + '\n')

if __name__ == '__main__':
    solve()