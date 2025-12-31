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
        a = list(map(int, data[idx:idx + n]))
        idx += n
        
        # Precompute the minimum prefix length to remove
        # We need to find the smallest k such that the subarray a[k:] is good
        # A subarray is good if we can arrange it into a non-decreasing sequence
        # by taking elements from either end
        
        # For a subarray to be good, it must be possible to arrange it into a non-decreasing sequence
        # by taking elements from either end. This is equivalent to the subarray being a "valid" sequence
        # that can be rearranged into non-decreasing order by taking from ends
        
        # We can use a greedy approach to check for each possible k
        # We'll use a two-pointer approach to check if the subarray a[k:] is good
        
        # Precompute for all possible k
        # We'll use a sliding window approach to find the minimal k
        # We'll use a deque to keep track of the elements in the subarray
        # and check if it's possible to arrange them into non-decreasing order
        
        # Let's try to find the minimal k
        min_k = n  # maximum possible value
        
        for k in range(n):
            # Check if a[k:] is good
            left = k
            right = n - 1
            dq = []
            valid = True
            while left <= right:
                if not dq or dq[-1] <= a[left]:
                    dq.append(a[left])
                    left += 1
                elif not dq or dq[-1] >= a[right]:
                    dq.append(a[right])
                    right -= 1
                else:
                    valid = False
                    break
            if valid:
                min_k = min(min_k, k)
        
        results.append(str(min_k))
    
    print('\n'.join(results))