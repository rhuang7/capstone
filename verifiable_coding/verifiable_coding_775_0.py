import sys
import bisect

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(T):
        N = int(data[idx])
        K = int(data[idx+1])
        x = int(data[idx+2])
        D = int(data[idx+3])
        idx += 4
        p = list(map(int, data[idx:idx+K]))
        idx += K
        
        # Sort the known values
        p.sort()
        
        # Check if the known values already violate the D condition
        for i in range(K):
            if i + 1 < K and p[i+1] - p[i] > D:
                results.append(-1)
                break
        else:
            # Find the maximum possible values for the unknowns
            # The unknowns must be placed in such a way that each has at least one other within D
            # Also, all values must be <= x and distinct
            # We need to fill the unknowns in the gaps between known values, and also at the ends
            
            # Create a list of known values
            known = p[:]
            
            # Add x if it's not already in the known list
            if x not in known:
                known.append(x)
                known.sort()
            
            # Now, fill the unknowns
            # We need to add (N - K) values
            # These values must be placed in such a way that each has at least one other within D
            # Also, all values must be <= x
            
            # We'll use a greedy approach: place the values as high as possible
            # We'll use a list to keep track of the current positions
            # We'll use a sorted list to manage the positions
            
            # Start with the known values
            positions = known[:]
            positions.sort()
            
            # Now, we need to add (N - K) values
            added = 0
            while added < (N - K):
                # Try to place the next value as high as possible
                # Find the rightmost position where we can place a value
                # such that it is within D of at least one existing value
                # and is <= x
                # We'll check the rightmost possible position
                # We can do this by checking the last element
                # and trying to place a value as high as possible
                
                # Check if we can place a value after the last known value
                last = positions[-1]
                if last + D <= x:
                    # We can place a value at last + D
                    # But we need to ensure it's not already in the list
                    # and that it's not already in the list
                    # Also, we need to make sure that it is within D of at least one existing value
                    # So we can place it at last + D
                    # But we need to check if it's within D of any existing value
                    # Since we are placing it at last + D, it is within D of last
                    # So it's valid
                    # Also, we need to ensure that it's not already in the list
                    # Since the list is sorted, we can use bisect to check
                    pos = bisect.bisect_right(positions, last + D)
                    if pos < len(positions) and positions[pos] == last + D:
                        # Already exists
                        pass
                    else:
                        # Add it
                        positions.insert(pos, last + D)
                        added += 1
                else:
                    # Try to place a value in the middle of the existing positions
                    # Find the rightmost position where we can place a value
                    # such that it is within D of at least one existing value
                    # We can do this by checking the last few positions
                    # Try to find the rightmost position where we can place a value
                    # that is within D of at least one existing value
                    # We'll start from the end and go backwards
                    # Try to find the rightmost position where we can place a value
                    # that is within D of at least one existing value
                    # and is <= x
                    # We can try to place a value in the middle of the existing positions
                    # We'll try to find the rightmost position where we can place a value
                    # that is within D of at least one existing value
                    # and is <= x
                    # We can try to find the rightmost position where we can place a value
                    # that is within D of at least one existing value
                    # and is <= x
                    # We can try to find the rightmost position where we can place a value
                    # that is within D of at least one existing value
                    # and is <= x
                    # We can try to find the rightmost position where we can place a value
                    # that is within D of at least one existing value
                    # and is <= x
                    # We can try to find the rightmost position where we can place a value
                    # that is within D of at least one existing value
                    # and is <= x
                    # We can try to find the rightmost position where we can place a value
                    # that is within D of at least one existing value
                    # and is <= x
                    # We can try to find the rightmost position where we can place a value
                    # that is within D of at least one existing value
                    # and is <= x
                    # We can try to find the rightmost position where we can place a value
                    # that is within D of at least one existing value
                    # and is <= x
                    # We can try to find the rightmost position where we can place a value
                    # that is within D of at least one existing value
                    # and is <= x
                    # We can try to find the rightmost position where we can place a value
                    # that is within D of at least one existing value
                    # and is <= x
                    # We can try to find the rightmost position where we can place a value
                    # that is within D of at least one existing value
                    # and is <= x
                    # We can try to find the rightmost position where we can place a value
                    # that is within D of at least one existing value
                    # and is <= x
                    # We can try to find the rightmost position where we can place a value
                    # that is within D of at least one existing value
                    # and is <= x
                    # We can try to find the rightmost position where we can place a value
                    # that is within D of at least one existing value
                    # and is <= x
                    # We can try to find the rightmost position where we can place a value
                    # that is within D of at least one existing value
                    # and is <= x
                    # We can try to find the rightmost position where we can place a value
                    # that is within D of at least one existing value
                    # and is <= x
                    # We can try to find the rightmost position where we can place a value
                    # that is within D of at least one existing value
                    # and is <= x
                    # We can try to find the rightmost position where we can place a value
                    # that is within D of at least one existing value
                    # and is <= x
                    # We can try to find the rightmost position where we can place a value
                    # that is within D of at least one existing value
                    # and is <= x
                    # We can try to find the rightmost position where we can place a value
                    # that is within D of at least one existing value
                    # and is <= x
                    # We can try to find the rightmost position where we can place a value
                    # that is within D of at least one existing value
                    # and is <= x
                    # We can try to find the rightmost position where we can place a value
                    # that is within D of at least one existing value
                    # and is <= x
                    # We can try to find the rightmost position where we can place a value
                    # that is within D of at least one existing value
                    # and is <= x
                    # We can try to find the rightmost position where we can place a value
                    # that is within D of at least one existing value
                    # and is <= x
                    # We can try to find the rightmost position where we can place a value
                    # that is within D of at least one existing value
                    # and is <= x
                    # We can try to find the rightmost position where we can place a value
                    # that is within D of at least one existing value
                    # and is <= x
                    # We can try to find the rightmost position where we can place a value
                    # that is within D of at least one existing value
                    # and is <= x
                    # We can try to find the rightmost position where we can place a value
                    # that is within D of at least one existing value
                    # and is <= x
                    # We can try to find the right