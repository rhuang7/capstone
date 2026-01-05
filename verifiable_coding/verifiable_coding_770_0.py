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
            # So we can use a sliding window approach to select the maximum elements
            # We will use a greedy approach: take the maximum in each window
            max_sum = 0
            window = []
            for i in range(len(arr)):
                # Add current element to window
                window.append(arr[i])
                # If window size exceeds k+1, remove the first element
                if len(window) > k + 1:
                    window.pop(0)
                # Take the maximum in the window
                max_sum += max(window)
            return max_sum
        
        # Compute maximum sum for even and odd numbers
        max_even = max_sum(evens, k)
        max_odd = max_sum(odds, k)
        
        # The answer is the sum of the maximum even and maximum odd
        results.append(str(max_even + max_odd))
    
    print('\n'.join(results))