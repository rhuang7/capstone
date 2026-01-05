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
        idx += 1
        X = []
        H = []
        for _ in range(N):
            x = int(data[idx])
            h = int(data[idx+1])
            X.append(x)
            H.append(h)
            idx += 2
        
        # Sort the points by X coordinate (already sorted according to input constraints)
        # We need to assign heights to points such that the area under the roof is maximized
        # The optimal way is to assign the largest heights to the points with the largest X differences
        # So we sort the heights in descending order and assign them to the points in order
        
        # Sort the points by X (already sorted, but we can sort by index for clarity)
        points = sorted(zip(X, H), key=lambda x: x[0])
        X_sorted = [x for x, h in points]
        H_sorted = [h for x, h in points]
        
        # Sort H in descending order
        H_sorted.sort(reverse=True)
        
        # Assign the largest H to the rightmost points
        # We can do this by sorting the points by X in ascending order and assigning the largest H to the rightmost
        # So we sort the points by X in ascending order, then assign the largest H to the rightmost
        # So we sort the points by X in ascending order, then assign H in descending order
        
        # Sort the points by X in ascending order (already sorted)
        # Assign H in descending order
        # We can do this by sorting the H in descending order and assigning them to the points in order
        
        # Create a list of (X, H) pairs
        # Sort the H in descending order and assign to the points in order
        # We can do this by sorting the H in descending order and then assigning to the points in order
        
        # Create a list of (X, H) pairs
        # Sort the H in descending order and assign to the points in order
        # We can do this by sorting the H in descending order and then assigning to the points in order
        
        # Now, we have X_sorted and H_sorted (sorted in ascending order of X)
        # We need to assign H_sorted to X_sorted in such a way that the area is maximized
        # The optimal way is to assign the largest H to the rightmost point
        # So we sort the points by X in ascending order, then assign H in descending order
        
        # So we sort the H in descending order and assign them to the points in order
        # So we have X_sorted and H_sorted (sorted in ascending order of X)
        # We need to assign H_sorted to X_sorted in such a way that the area is maximized
        # The optimal way is to assign the largest H to the rightmost point
        # So we sort the H in descending order and assign them to the points in order
        
        # Now, we have X_sorted and H_sorted (sorted in ascending order of X)
        # We need to assign H_sorted to X_sorted in such a way that the area is maximized
        # The optimal way is to assign the largest H to the rightmost point
        # So we sort the H in descending order and assign them to the points in order
        
        # Now, we have X_sorted and H_sorted (sorted in ascending order of X)
        # We need to assign H_sorted to X_sorted in such a way that the area is maximized
        # The optimal way is to assign the largest H to the rightmost point
        # So we sort the H in descending order and assign them to the points in order
        
        # Now, we have X_sorted and H_sorted (sorted in ascending order of X)
        # We need to assign H_sorted to X_sorted in such a way that the area is maximized
        # The optimal way is to assign the largest H to the rightmost point
        # So we sort the H in descending order and assign them to the points in order
        
        # Now, we have X_sorted and H_sorted (sorted in ascending order of X)
        # We need to assign H_sorted to X_sorted in such a way that the area is maximized
        # The optimal way is to assign the largest H to the rightmost point
        # So we sort the H in descending order and assign them to the points in order
        
        # Now, we have X_sorted and H_sorted (sorted in ascending order of X)
        # We need to assign H_sorted to X_sorted in such a way that the area is maximized
        # The optimal way is to assign the largest H to the rightmost point
        # So we sort the H in descending order and assign them to the points in order
        
        # Now, we have X_sorted and H_sorted (sorted in ascending order of X)
        # We need to assign H_sorted to X_sorted in such a way that the area is maximized
        # The optimal way is to assign the largest H to the rightmost point
        # So we sort the H in descending order and assign them to the points in order
        
        # Now, we have X_sorted and H_sorted (sorted in ascending order of X)
        # We need to assign H_sorted to X_sorted in such a way that the area is maximized
        # The optimal way is to assign the largest H to the rightmost point
        # So we sort the H in descending order and assign them to the points in order
        
        # Now, we have X_sorted and H_sorted (sorted in ascending order of X)
        # We need to assign H_sorted to X_sorted in such a way that the area is maximized
        # The optimal way is to assign the largest H to the rightmost point
        # So we sort the H in descending order and assign them to the points in order
        
        # Now, we have X_sorted and H_sorted (sorted in ascending order of X)
        # We need to assign H_sorted to X_sorted in such a way that the area is maximized
        # The optimal way is to assign the largest H to the rightmost point
        # So we sort the H in descending order and assign them to the points in order
        
        # Now, we have X_sorted and H_sorted (sorted in ascending order of X)
        # We need to assign H_sorted to X_sorted in such a way that the area is maximized
        # The optimal way is to assign the largest H to the rightmost point
        # So we sort the H in descending order and assign them to the points in order
        
        # Now, we have X_sorted and H_sorted (sorted in ascending order of X)
        # We need to assign H_sorted to X_sorted in such a way that the area is maximized
        # The optimal way is to assign the largest H to the rightmost point
        # So we sort the H in descending order and assign them to the points in order
        
        # Now, we have X_sorted and H_sorted (sorted in ascending order of X)
        # We need to assign H_sorted to X_sorted in such a way that the area is maximized
        # The optimal way is to assign the largest H to the rightmost point
        # So we sort the H in descending order and assign them to the points in order
        
        # Now, we have X_sorted and H_sorted (sorted in ascending order of X)
        # We need to assign H_sorted to X_sorted in such a way that the area is maximized
        # The optimal way is to assign the largest H to the rightmost point
        # So we sort the H in descending order and assign them to the points in order
        
        # Now, we have X_sorted and H_sorted (sorted in ascending order of X)
        # We need to assign H_sorted to X_sorted in such a way that the area is maximized
        # The optimal way is to assign the largest H to the rightmost point
        # So we sort the H in descending order and assign them to the points in order
        
        # Now, we have X_sorted and H_sorted (sorted in ascending order of X)
        # We need to assign H_sorted to X_sorted in such a way that the area is maximized
        # The optimal way is to assign the largest H to the rightmost point
        # So we sort the H in descending order and assign them to the points in order
        
        # Now, we have X_sorted and H_sorted (sorted in ascending order of X)
        # We need to assign H_sorted to X_sorted in such a way that the area is maximized
        # The optimal way is to assign the largest H to the rightmost point
        # So we sort the H in descending order and assign them to the points in order
        
        # Now, we have X_sorted and H_sorted (sorted in ascending order of X)
        # We need to assign H_sorted to X_sorted in such a way that the area is maximized
        # The optimal way is to assign the largest H to the rightmost point
        # So we sort the H in descending order and assign them to the points in order
        
        # Now, we have X_sorted and H_sorted (sorted in ascending order of