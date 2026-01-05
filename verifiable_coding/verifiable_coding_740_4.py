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
        M = int(data[idx+1])
        K = int(data[idx+2])
        idx += 3
        plants = []
        for __ in range(K):
            r = int(data[idx])
            c = int(data[idx+1])
            plants.append((r, c))
            idx += 2
        # Compute the minimal fence length
        # The minimal fence length is the perimeter of the plant region
        # We can find the minimal and maximal row and column of plants
        min_r = min(p[0] for p in plants)
        max_r = max(p[0] for p in plants)
        min_c = min(p[1] for p in plants)
        max_c = max(p[1] for p in plants)
        # The perimeter is 2*(max_r - min_r + 1 + max_c - min_c + 1)
        # But we need to subtract 2 if there is a hole in the middle
        # To check for a hole, we can check if there is a cell (r, c) where r is between min_r and max_r, c is between min_c and max_c, and (r, c) is not in plants
        # But for large N and M, we can't check all cells
        # Instead, we can check if the number of plants is equal to (max_r - min_r + 1) * (max_c - min_c + 1)
        # If it is, then there is no hole, else there is a hole
        area = (max_r - min_r + 1) * (max_c - min_c + 1)
        if K == area:
            # No hole, perimeter is 2*(max_r - min_r + 1 + max_c - min_c + 1)
            perimeter = 2 * (max_r - min_r + 1 + max_c - min_c + 1)
        else:
            # There is a hole, perimeter is 2*(max_r - min_r + 1 + max_c - min_c + 1) - 4
            perimeter = 2 * (max_r - min_r + 1 + max_c - min_c + 1) - 4
        results.append(str(perimeter))
    print('\n'.join(results))