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
        # Sort the points by X
        X.sort()
        # We need to assign H values to X in a way that maximizes the area
        # The optimal way is to use a greedy approach: for each point, assign the highest possible H that hasn't been used yet
        # But since the points are sorted, we can use a stack-based approach
        # We will use a monotonic stack to find the maximum area
        # The area is the sum of the areas of the trapezoids between consecutive points
        # The area between X[i] and X[i+1] is (X[i+1] - X[i]) * (H[i] + H[i+1]) / 2
        # But since we can assign H values to points, we need to choose the best H values
        # The optimal assignment is to sort H in descending order and assign them to X in sorted order
        # So we sort H in descending order and assign them to X in sorted order
        H.sort(reverse=True)
        # Now compute the area
        area = 0
        for i in range(N-1):
            area += (X[i+1] - X[i]) * (H[i] + H[i+1]) // 2
        # Add the area of the base
        area += X[-1] * H[-1]
        results.append(2 * area)
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()