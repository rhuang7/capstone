import sys
import bisect

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        a = list(map(int, data[idx:idx+n]))
        idx += n
        
        # Precompute the minimum prefix to remove
        # We need to find the smallest k such that the subarray a[k:] is good
        # A subarray is good if we can arrange it in non-decreasing order by taking from ends
        
        # For a subarray to be good, it must be possible to arrange it in non-decreasing order by taking from ends
        # This is equivalent to the subarray being a valid "double-ended" non-decreasing sequence
        
        # We can use a greedy approach to check for each possible k
        # We'll try to find the smallest k such that a[k:] is good
        
        # Try all possible k from 0 to n
        # For each k, check if a[k:] is good
        # To check if a[k:] is good, we can use a two-pointer approach
        # Start with left = k, right = n-1
        # We can take from left or right, and keep track of the current maximum
        # If at any point the current element is less than the current maximum, it's not good
        
        # We'll precompute for all k from 0 to n
        # We'll store the smallest k for which a[k:] is good
        
        # Initialize the answer as n (meaning we need to remove all elements)
        ans = n
        
        for k in range(n+1):
            left = k
            right = n-1
            current_max = -1
            valid = True
            while left <= right:
                if a[left] <= current_max:
                    left += 1
                elif a[right] <= current_max:
                    right -= 1
                else:
                    # Choose the smaller of the two
                    if a[left] <= a[right]:
                        current_max = a[left]
                        left += 1
                    else:
                        current_max = a[right]
                        right -= 1
            if left > right:
                ans = min(ans, k)
        
        results.append(str(ans))
    
    print('\n'.join(results))