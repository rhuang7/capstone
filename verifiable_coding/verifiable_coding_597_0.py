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
        points = sorted(zip(X, H), key=lambda x: x[0])
        X_sorted = [x for x, h in points]
        H_sorted = [h for x, h in points]
        # We need to assign H values to points such that the area is maximized
        # This is equivalent to finding a permutation of H_sorted that maximizes the area
        # The optimal way is to sort H in non-decreasing order and assign them to X in non-decreasing order
        # But since X is already sorted, we can sort H in non-decreasing order and assign them to X in non-decreasing order
        H_sorted.sort()
        # Now compute the area
        # The area is the sum of trapezoids between consecutive points
        # Area = sum_{i=1 to N-1} (X[i] - X[i-1]) * (H[i] + H[i-1]) / 2
        # But since we are to compute 2 * S, it becomes sum_{i=1 to N-1} (X[i] - X[i-1]) * (H[i] + H[i-1])
        # So we can compute this directly
        total = 0
        for i in range(1, N):
            total += (X_sorted[i] - X_sorted[i-1]) * (H_sorted[i] + H_sorted[i-1])
        results.append(total)
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()