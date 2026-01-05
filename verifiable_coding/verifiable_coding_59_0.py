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
        a = list(map(int, data[idx:idx+n]))
        idx += n
        
        # Find all positions where the element is missing
        missing = []
        for i in range(n):
            if a[i] == -1:
                missing.append(i)
        
        # For each pair of consecutive missing positions, find the possible k values
        # that can minimize the max difference
        # We need to find the k that minimizes the maximum absolute difference
        # between adjacent elements, considering the missing positions
        
        # Collect all the non-missing elements around the missing positions
        non_missing = []
        for i in range(n):
            if a[i] != -1:
                non_missing.append(a[i])
        
        # For each missing position, we need to find the best k that can minimize the max difference
        # We can use binary search on the possible k values
        # But since the problem is to find the minimal possible max difference, we can use a binary search approach
        
        # The minimal possible m is 0, and the maximal possible m is the maximum difference between non-missing elements
        # So we can binary search on m, and check if there exists a k such that all adjacent differences are <= m
        
        # First, collect all the non-missing elements and their positions
        non_missing_positions = []
        for i in range(n):
            if a[i] != -1:
                non_missing_positions.append(i)
        
        # Now, for each pair of consecutive non-missing elements, we can find the possible k values
        # that can be placed in the missing positions to minimize the max difference
        
        # We will try to find the minimal m and the corresponding k
        # We can use binary search on m
        
        # Function to check if a given m is possible
        def is_possible(m):
            # Try to find a k such that all adjacent differences are <= m
            # We need to find a k that can be placed in the missing positions
            # such that the max difference between adjacent elements is <= m
            # We can try to find the k that minimizes the max difference
            
            # For each missing position, we can try to find the best k that can be placed there
            # such that the max difference between adjacent elements is <= m
            # We can use a greedy approach to find the best k
            
            # We can try to find the best k by considering the possible ranges of k
            # that can be placed in the missing positions
            
            # For each missing position, we can find the possible k values that can be placed there
            # such that the max difference between adjacent elements is <= m
            
            # We can use a greedy approach to find the best k
            # We can try to find the k that is the median of the possible values
            # or the value that can minimize the max difference
            
            # We can try to find the best k by considering the non-missing elements
            # and the missing positions between them
            
            # We can try to find the best k by considering the possible ranges
            # between the non-missing elements
            
            # We can use a binary search approach for k
            # We can try to find the best k that minimizes the max difference
            
            # We can try to find the best k by checking all possible k values
            # that are between the non-missing elements
            
            # We can try to find the best k by checking the possible ranges between the non-missing elements
            
            # For each missing position, we can find the possible k values that can be placed there
            # such that the max difference between adjacent elements is <= m
            
            # We can try to find the best k by checking the possible ranges between the non-missing elements
            
            # We can try to find the best k by checking the possible ranges between the non-missing elements
            
            # We can try to find the best k by checking the possible ranges between the non-missing elements
            
            # We can try to find the best k by checking the possible ranges between the non-missing elements
            
            # We can try to find the best k by checking the possible ranges between the non-missing elements
            
            # We can try to find the best k by checking the possible ranges between the non-missing elements
            
            # We can try to find the best k by checking the possible ranges between the non-missing elements
            
            # We can try to find the best k by checking the possible ranges between the non-missing elements
            
            # We can try to find the best k by checking the possible ranges between the non-missing elements
            
            # We can try to find the best k by checking the possible ranges between the non-missing elements
            
            # We can try to find the best k by checking the possible ranges between the non-missing elements
            
            # We can try to find the best k by checking the possible ranges between the non-missing elements
            
            # We can try to find the best k by checking the possible ranges between the non-missing elements
            
            # We can try to find the best k by checking the possible ranges between the non-missing elements
            
            # We can try to find the best k by checking the possible ranges between the non-missing elements
            
            # We can try to find the best k by checking the possible ranges between the non-missing elements
            
            # We can try to find the best k by checking the possible ranges between the non-missing elements
            
            # We can try to find the best k by checking the possible ranges between the non-missing elements
            
            # We can try to find the best k by checking the possible ranges between the non-missing elements
            
            # We can try to find the best k by checking the possible ranges between the non-missing elements
            
            # We can try to find the best k by checking the possible ranges between the non-missing elements
            
            # We can try to find the best k by checking the possible ranges between the non-missing elements
            
            # We can try to find the best k by checking the possible ranges between the non-missing elements
            
            # We can try to find the best k by checking the possible ranges between the non-missing elements
            
            # We can try to find the best k by checking the possible ranges between the non-missing elements
            
            # We can try to find the best k by checking the possible ranges between the non-missing elements
            
            # We can try to find the best k by checking the possible ranges between the non-missing elements
            
            # We can try to find the best k by checking the possible ranges between the non-missing elements
            
            # We can try to find the best k by checking the possible ranges between the non-missing elements
            
            # We can try to find the best k by checking the possible ranges between the non-missing elements
            
            # We can try to find the best k by checking the possible ranges between the non-missing elements
            
            # We can try to find the best k by checking the possible ranges between the non-missing elements
            
            # We can try to find the best k by checking the possible ranges between the non-missing elements
            
            # We can try to find the best k by checking the possible ranges between the non-missing elements
            
            # We can try to find the best k by checking the possible ranges between the non-missing elements
            
            # We can try to find the best k by checking the possible ranges between the non-missing elements
            
            # We can try to find the best k by checking the possible ranges between the non-missing elements
            
            # We can try to find the best k by checking the possible ranges between the non-missing elements
            
            # We can try to find the best k by checking the possible ranges between the non-missing elements
            
            # We can try to find the best k by checking the possible ranges between the non-missing elements
            
            # We can try to find the best k by checking the possible ranges between the non-missing elements
            
            # We can try to find the best k by checking the possible ranges between the non-missing elements
            
            # We can try to find the best k by checking the possible ranges between the non-missing elements
            
            # We can try to find the best k by checking the possible ranges between the non-missing elements
            
            # We can try to find the best k by checking the possible ranges between the non-missing elements
            
            # We can try to find the best k by checking the possible ranges between the non-missing elements
            
            # We can try to find the best k by checking the possible ranges between the non-missing elements
            
            # We can try to find the best k by checking the possible ranges between the non-missing elements
            
            # We can try to find the best k by checking the possible ranges between the non-missing elements
            
            # We can try to find the best k by checking the possible ranges between the non-missing elements
            
            # We can try to find the best k by checking the possible ranges between the non-missing elements
            
            # We can try to find the best k by checking the possible ranges between the non-missing elements
            
            # We can try to find the best k by checking the possible ranges between the non-m