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
        # We need to assign H_i to X_i in a way that maximizes the area
        # The area is the area under the polygon formed by the points (X_i, H_p_i)
        # The polygon is closed by connecting (X_N, 0) to (X_1, 0) and back to (X_1, H_p_1)
        # The area can be computed as the sum of trapezoids between consecutive points
        
        # To maximize the area, we need to assign the largest H values to the points with the largest X differences
        # So we sort the H values in descending order and assign them to the X points in ascending order
        
        # Sort H in descending order
        H_sorted = sorted(H, reverse=True)
        
        # Assign H_sorted[i] to X[i]
        # Compute the area
        area = 0
        for i in range(N-1):
            area += (X[i+1] - X[i]) * (H_sorted[i] + H_sorted[i+1]) // 2
        
        # Add the area of the last trapezoid from (X_N, 0) to (X_1, 0) to (X_1, H_p_1)
        area += (X[N-1] - X[0]) * (H_sorted[N-1] + 0) // 2
        
        results.append(str(2 * area))
    
    print('\n'.join(results))