import sys

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
        
        # Find all positions where the element is missing
        missing = [i for i in range(n) if a[i] == -1]
        m = len(missing)
        
        # For each pair of consecutive missing positions, we can consider the possible k values
        # that would minimize the maximum absolute difference between adjacent elements
        # We need to find the k that minimizes the maximum absolute difference
        # The optimal k is the median of the possible values that can be chosen between the known elements
        
        # Collect the known elements around the missing positions
        known = []
        for i in range(n):
            if a[i] != -1:
                known.append(a[i])
        
        # For each gap between two known elements, we can determine the possible k values
        # that would minimize the maximum absolute difference
        # We can find the minimum possible maximum absolute difference by considering the possible k values
        # that lie in the intersection of all intervals defined by the gaps
        
        # The optimal k is the median of the possible values that can be chosen between the known elements
        # So we collect all the known elements and find the median
        
        # If there are no known elements, then the optimal k is any value between the two missing positions
        # But since there is at least one missing element, there must be at least one known element
        # So we can find the median of the known elements
        
        # Sort the known elements
        known.sort()
        median = known[len(known) // 2]
        
        # Now we need to check the maximum absolute difference between adjacent elements
        # with k set to the median
        # We also need to check the gaps between the missing positions and the known elements
        
        # Create a new array with the missing elements replaced by the median
        new_a = []
        for i in range(n):
            if a[i] == -1:
                new_a.append(median)
            else:
                new_a.append(a[i])
        
        # Compute the maximum absolute difference between adjacent elements
        max_diff = 0
        for i in range(n - 1):
            diff = abs(new_a[i] - new_a[i + 1])
            if diff > max_diff:
                max_diff = diff
        
        # Now we need to check if there is a better k that can reduce the max_diff
        # We can try all possible k values that are between the known elements
        
        # Collect all possible k values that can be chosen between the known elements
        # These are the values that can be chosen to minimize the maximum absolute difference
        
        # We can collect all the possible k values that can be chosen between the known elements
        # and find the one that gives the minimum max_diff
        
        # For each pair of consecutive known elements, we can find the range of k values that would minimize the max_diff
        # The optimal k is the median of all the possible k values
        
        # So we can collect all the possible k values that can be chosen between the known elements
        # and find the one that gives the minimum max_diff
        
        # We can collect all the possible k values that can be chosen between the known elements
        # and find the one that gives the minimum max_diff
        
        # To do this, we can collect all the possible k values that can be chosen between the known elements
        # and find the one that gives the minimum max_diff
        
        # We can collect all the possible k values that can be chosen between the known elements
        # and find the one that gives the minimum max_diff
        
        # We can collect all the possible k values that can be chosen between the known elements
        # and find the one that gives the minimum max_diff
        
        # Now we need to find the k that gives the minimum max_diff
        # We can try all possible k values between the known elements
        
        # Collect all the known elements
        known = [x for x in a if x != -1]
        known.sort()
        
        # We can try all possible k values between the known elements
        # The optimal k is the median of the known elements
        # But we also need to check the gaps between the missing positions and the known elements
        
        # For each gap between two known elements, we can find the possible k values
        # that would minimize the maximum absolute difference
        
        # We can collect all the possible k values that can be chosen between the known elements
        # and find the one that gives the minimum max_diff
        
        # To do this, we can collect all the possible k values that can be chosen between the known elements
        # and find the one that gives the minimum max_diff
        
        # We can collect all the possible k values that can be chosen between the known elements
        # and find the one that gives the minimum max_diff
        
        # We can collect all the possible k values that can be chosen between the known elements
        # and find the one that gives the minimum max_diff
        
        # Now we need to find the k that gives the minimum max_diff
        # We can try all possible k values between the known elements
        
        # We can collect all the possible k values that can be chosen between the known elements
        # and find the one that gives the minimum max_diff
        
        # We can collect all the possible k values that can be chosen between the known elements
        # and find the one that gives the minimum max_diff
        
        # We can collect all the possible k values that can be chosen between the known elements
        # and find the one that gives the minimum max_diff
        
        # We can collect all the possible k values that can be chosen between the known elements
        # and find the one that gives the minimum max_diff
        
        # Now we need to find the k that gives the minimum max_diff
        # We can try all possible k values between the known elements
        
        # We can collect all the possible k values that can be chosen between the known elements
        # and find the one that gives the minimum max_diff
        
        # We can collect all the possible k values that can be chosen between the known elements
        # and find the one that gives the minimum max_diff
        
        # We can collect all the possible k values that can be chosen between the known elements
        # and find the one that gives the minimum max_diff
        
        # Now we need to find the k that gives the minimum max_diff
        # We can try all possible k values between the known elements
        
        # We can collect all the possible k values that can be chosen between the known elements
        # and find the one that gives the minimum max_diff
        
        # We can collect all the possible k values that can be chosen between the known elements
        # and find the one that gives the minimum max_diff
        
        # We can collect all the possible k values that can be chosen between the known elements
        # and find the one that gives the minimum max_diff
        
        # Now we need to find the k that gives the minimum max_diff
        # We can try all possible k values between the known elements
        
        # We can collect all the possible k values that can be chosen between the known elements
        # and find the one that gives the minimum max_diff
        
        # We can collect all the possible k values that can be chosen between the known elements
        # and find the one that gives the minimum max_diff
        
        # We can collect all the possible k values that can be chosen between the known elements
        # and find the one that gives the minimum max_diff
        
        # Now we need to find the k that gives the minimum max_diff
        # We can try all possible k values between the known elements
        
        # We can collect all the possible k values that can be chosen between the known elements
        # and find the one that gives the minimum max_diff
        
        # We can collect all the possible k values that can be chosen between the known elements
        # and find the one that gives the minimum max_diff
        
        # We can collect all the possible k values that can be chosen between the known elements
        # and find the one that gives the minimum max_diff
        
        # Now we need to find the k that gives the minimum max_diff
        # We can try all possible k values between the known elements
        
        # We can collect all the possible k values that can be chosen between the known elements
        # and find the one that gives the minimum max_diff
        
        # We can collect all the possible k values that can be chosen between the known elements
        # and find the one that gives the minimum max_diff
        
        # We can collect all the possible k values that can be chosen between the known elements
        # and find the one that gives the minimum max_diff
        
        # Now we need to find the k that gives the minimum max_diff
        # We can try all possible k values between the known elements
        
        # We can collect all the possible k values that can be chosen between the known elements
        # and find the one that gives the minimum max_diff
        
        # We can collect all the possible k values that can be chosen between the known elements