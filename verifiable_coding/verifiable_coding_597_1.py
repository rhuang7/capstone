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
        
        # Sort the points by X-coordinate
        points = sorted(zip(X, H), key=lambda x: x[0])
        X_sorted = [x for x, h in points]
        H_sorted = [h for x, h in points]
        
        # We need to assign H_i to points such that the area is maximized
        # The optimal way is to sort H in non-decreasing order and assign them to points in non-decreasing order
        # So we sort H in non-decreasing order and assign to points in non-decreasing order
        H_sorted_desc = sorted(H_sorted, reverse=True)
        
        # Compute the area
        area = 0
        prev_x = X_sorted[0]
        prev_h = H_sorted_desc[0]
        area += prev_h * (X_sorted[1] - prev_x)
        
        for i in range(1, N):
            curr_x = X_sorted[i]
            curr_h = H_sorted_desc[i]
            area += (curr_h - prev_h) * (curr_x - prev_x)
            prev_x = curr_x
            prev_h = curr_h
        
        # Add the base area
        area += prev_h * (X_sorted[-1] - X_sorted[0])
        
        # The answer is 2 * area
        results.append(str(2 * area))
    
    sys.stdout.write('\n'.join(results) + '\n')

if __name__ == '__main__':
    solve()