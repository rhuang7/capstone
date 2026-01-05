import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(T):
        type_ = int(data[idx])
        idx += 1
        s = data[idx]
        idx += 1
        n = len(s)
        
        # Check if it's possible to make the arrangement likable
        # A valid arrangement must have no two consecutive same characters
        # So, the number of B's and G's must differ by at most 1
        cnt_b = s.count('B')
        cnt_g = n - cnt_b
        if abs(cnt_b - cnt_g) > 1:
            results.append("-1")
            continue
        
        # Generate the target arrangement
        # We can have either BGBGBG... or GBGBGB...
        # We need to choose the one that requires minimum swaps
        # Let's try both possibilities and choose the one with minimum cost
        
        # Function to compute minimum cost for a given target arrangement
        def min_cost(target):
            # Create a list of positions where we need to swap
            # For each character in s, if it's not matching target, we need to swap
            # We'll use a greedy approach to match the characters
            # We'll track the positions where we need to swap
            # We'll also track the cost based on the type
            
            # Create a list of positions for 'B' and 'G' in the target
            target_b = []
            target_g = []
            for i, c in enumerate(target):
                if c == 'B':
                    target_b.append(i)
                else:
                    target_g.append(i)
            
            # Create a list of positions for 'B' and 'G' in the original string
            original_b = []
            original_g = []
            for i, c in enumerate(s):
                if c == 'B':
                    original_b.append(i)
                else:
                    original_g.append(i)
            
            # Match the original B's to target B's and original G's to target G's
            # We'll use two pointers to match them
            # For each B in original, we'll find the corresponding B in target
            # And for each G in original, we'll find the corresponding G in target
            
            # Initialize pointers
            i = 0  # pointer for original_b
            j = 0  # pointer for target_b
            cost = 0
            
            # Match original B's to target B's
            while i < len(original_b) and j < len(target_b):
                if original_b[i] == target_b[j]:
                    i += 1
                    j += 1
                else:
                    # We need to swap this B with a G in the target
                    # So we'll swap it with the next G in the target
                    # We'll find the next G in the target
                    # We'll find the next G in the original
                    # We'll swap them
                    # But since we're using a greedy approach, we'll just calculate the cost
                    # and move the pointers
                    # This is for type 0, 1, 2
                    # We'll calculate the cost based on the type
                    # For type 0: cost is 1
                    # For type 1: cost is |original_b[i] - target_g[j]|
                    # For type 2: cost is (original_b[i] - target_g[j])^2
                    # We'll find the next G in the target
                    # We'll find the next G in the original
                    # We'll swap them
                    # But since we are not actually swapping, we just need to calculate the cost
                    # So we'll find the next G in the target and the next G in the original
                    # and calculate the cost
                    # This is for the case where we have to swap a B with a G
                    # So we'll find the next G in the target and the next G in the original
                    # and calculate the cost
                    # We'll also increment the pointers
                    
                    # Find the next G in the target
                    next_g_target = None
                    for k in range(j, len(target_g)):
                        if target_g[k] > target_b[j]:
                            next_g_target = target_g[k]
                            break
                    # Find the next G in the original
                    next_g_original = None
                    for k in range(i, len(original_g)):
                        if original_g[k] > original_b[i]:
                            next_g_original = original_g[k]
                            break
                    
                    # If we can't find a G in the target or original, it's not possible
                    if next_g_target is None or next_g_original is None:
                        return float('inf')
                    
                    # Calculate the cost based on the type
                    if type_ == 0:
                        cost += 1
                    elif type_ == 1:
                        cost += abs(next_g_original - next_g_target)
                    elif type_ == 2:
                        cost += (next_g_original - next_g_target) ** 2
                    
                    # Move the pointers
                    i += 1
                    j += 1
                    
            # Similarly for G's
            i = 0  # pointer for original_g
            j = 0  # pointer for target_g
            while i < len(original_g) and j < len(target_g):
                if original_g[i] == target_g[j]:
                    i += 1
                    j += 1
                else:
                    # We need to swap this G with a B in the target
                    # So we'll find the next B in the target and the next B in the original
                    # and calculate the cost
                    # This is for the case where we have to swap a G with a B
                    # So we'll find the next B in the target and the next B in the original
                    # and calculate the cost
                    # We'll also increment the pointers
                    
                    # Find the next B in the target
                    next_b_target = None
                    for k in range(j, len(target_b)):
                        if target_b[k] > target_g[j]:
                            next_b_target = target_b[k]
                            break
                    # Find the next B in the original
                    next_b_original = None
                    for k in range(i, len(original_b)):
                        if original_b[k] > original_g[i]:
                            next_b_original = original_b[k]
                            break
                    
                    # If we can't find a B in the target or original, it's not possible
                    if next_b_target is None or next_b_original is None:
                        return float('inf')
                    
                    # Calculate the cost based on the type
                    if type_ == 0:
                        cost += 1
                    elif type_ == 1:
                        cost += abs(next_b_original - next_b_target)
                    elif type_ == 2:
                        cost += (next_b_original - next_b_target) ** 2
                    
                    # Move the pointers
                    i += 1
                    j += 1
            
            return cost
        
        # Try both possible target arrangements
        # Target 1: BGBGBG...
        target1 = []
        for i in range(n):
            if i % 2 == 0:
                target1.append('B')
            else:
                target1.append('G')
        cost1 = min_cost(target1)
        
        # Target 2: GBGBGB...
        target2 = []
        for i in range(n):
            if i % 2 == 0:
                target2.append('G')
            else:
                target2.append('B')
        cost2 = min_cost(target2)
        
        # Choose the minimum cost
        results.append(str(min(cost1, cost2)))
    
    print('\n'.join(results))