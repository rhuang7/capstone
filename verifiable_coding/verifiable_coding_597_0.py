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
        
        # Sort the points by X coordinate (already sorted in input)
        # We need to assign heights to points such that the area is maximized
        # The area is the integral under the polyline, which can be computed using the trapezoidal rule
        # To maximize the area, we need to assign the largest heights to the points with the largest X differences
        
        # Sort the points by X coordinate (already sorted)
        # We will assign heights in a way that the largest heights are assigned to the points with the largest X differences
        
        # Sort the points by X coordinate (already sorted)
        # We will assign heights in a way that the largest heights are assigned to the points with the largest X differences
        
        # To maximize the area, we need to assign the largest heights to the points with the largest X differences
        # So we sort the heights in descending order and assign them to the points in the order of increasing X differences
        
        # Sort the points by X coordinate (already sorted)
        # We will assign the heights in a way that the largest heights are assigned to the points with the largest X differences
        
        # To maximize the area, we need to assign the largest heights to the points with the largest X differences
        # So we sort the heights in descending order and assign them to the points in the order of increasing X differences
        
        # Sort the points by X coordinate (already sorted)
        # We will assign the heights in a way that the largest heights are assigned to the points with the largest X differences
        
        # Sort the heights in descending order
        H_sorted = sorted(H, reverse=True)
        
        # Assign the largest heights to the points with the largest X differences
        # We can do this by assigning the largest height to the first point, the second largest to the second point, etc.
        
        # Create a list of tuples (X_i, H_i)
        points = list(zip(X, H))
        
        # Sort the points by X coordinate (already sorted)
        # We will assign the heights in a way that the largest heights are assigned to the points with the largest X differences
        
        # Sort the points by X coordinate (already sorted)
        # We will assign the heights in a way that the largest heights are assigned to the points with the largest X differences
        
        # To maximize the area, we need to assign the largest heights to the points with the largest X differences
        # So we sort the heights in descending order and assign them to the points in the order of increasing X differences
        
        # Sort the points by X coordinate (already sorted)
        # We will assign the heights in a way that the largest heights are assigned to the points with the largest X differences
        
        # Assign the sorted heights to the points
        for i in range(N):
            points[i] = (points[i][0], H_sorted[i])
        
        # Compute the area
        area = 0
        prev_x = points[0][0]
        prev_h = points[0][1]
        for i in range(1, N):
            curr_x = points[i][0]
            curr_h = points[i][1]
            area += (curr_x - prev_x) * (prev_h + curr_h) // 2
            prev_x = curr_x
            prev_h = curr_h
        
        # Add the area of the triangle formed by the last point, the ground, and the first point
        area += (points[-1][0] - points[0][0]) * prev_h // 2
        
        # Compute 2 * S
        results.append(2 * area)
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()