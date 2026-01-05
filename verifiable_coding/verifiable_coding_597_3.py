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
        
        # Sort the points by X-coordinate (already sorted in input)
        # We need to assign heights to points such that the area under the roof is maximized
        # This is equivalent to finding a permutation of H that maximizes the area of the polygon
        
        # The area S is the area under the polyline formed by the points (X_i, H_p_i)
        # The area can be computed as the sum of trapezoids between consecutive points
        # S = sum_{i=1 to N-1} (X_{i+1} - X_i) * (H_p_i + H_p_{i+1}) / 2
        # To maximize S, we need to maximize the sum of (H_p_i + H_p_{i+1}) for each i
        
        # This is equivalent to finding a permutation of H such that the sum of adjacent pairs is maximized
        # This is a classic problem that can be solved by sorting H in non-decreasing order and then alternating between high and low values
        
        # Sort H in non-decreasing order
        H.sort()
        # Assign the largest to the first point, second largest to the second point, etc.
        # This is the optimal way to maximize the sum of adjacent pairs
        # We can do this by placing the largest in the middle and alternately placing the next largest on either side
        
        # Create a new array for the assigned heights
        assigned = [0] * N
        left = 0
        right = N - 1
        # Start from the middle and alternate placing the largest remaining
        for i in range(N):
            if i % 2 == 0:
                assigned[i] = H[right]
                right -= 1
            else:
                assigned[i] = H[left]
                left += 1
        
        # Compute the area
        S = 0
        for i in range(N - 1):
            S += (X[i + 1] - X[i]) * (assigned[i] + assigned[i + 1]) // 2
        
        # The answer is 2 * S
        results.append(2 * S)
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()