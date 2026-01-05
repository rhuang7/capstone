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
            # We can take at most one element from each window of size k+1
            # So we can use a sliding window approach to select maximum elements
            # We can greedily take the maximum in each window
            res = 0
            i = 0
            while i < len(arr):
                # Find the maximum in the window [i, min(i + k, len(arr)-1)]
                max_val = -1
                j = i
                while j < min(i + k + 1, len(arr)):
                    if arr[j] > max_val:
                        max_val = arr[j]
                    j += 1
                res += max_val
                i = j
            return res
        
        max_even = max_sum(evens, k)
        max_odd = max_sum(odds, k)
        results.append(str(max_even + max_odd))
    
    print('\n'.join(results))