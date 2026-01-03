import sys
import math

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
        a = list(map(int, data[idx:idx + n]))
        idx += n
        
        # Precompute for each position the minimum number of elements to remove from the front
        # to make the remaining array good
        # We will use a greedy approach to check if a subarray is good
        
        # For each possible prefix length k (0 <= k <= n), check if the subarray a[k:] is good
        # We need to find the smallest k such that a[k:] is good
        
        # To check if a subarray is good, we can simulate the process of building a non-decreasing array
        # by taking elements from either end of the subarray
        
        # We can use a two-pointer approach to check if the subarray is good
        # We will try to build a non-decreasing array by taking elements from either end
        
        # For each possible k, check if a[k:] is good
        # We will use a binary search approach to find the minimal k
        
        # Precompute for each position the minimum k such that a[k:] is good
        # We can use a sliding window approach
        
        # We will use a greedy approach to find the minimal k
        # For each possible k, check if a[k:] is good
        
        # To check if a subarray is good, we can simulate the process of building a non-decreasing array
        # by taking elements from either end of the subarray
        
        # Let's define a helper function to check if a subarray is good
        def is_good(sub):
            left = 0
            right = len(sub) - 1
            c = []
            while left <= right:
                if not c or sub[left] <= c[-1]:
                    c.append(sub[left])
                    left += 1
                elif not c or sub[right] <= c[-1]:
                    c.append(sub[right])
                    right -= 1
                else:
                    return False
            return True
        
        # Now, for each possible k, check if a[k:] is good
        # We can use binary search to find the minimal k
        # We will try to find the minimal k such that a[k:] is good
        
        # Initialize the answer as n (meaning we need to remove all elements)
        ans = n
        
        # Try all possible k from 0 to n
        for k in range(n + 1):
            if is_good(a[k:]):
                ans = min(ans, k)
        
        results.append(str(ans))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()