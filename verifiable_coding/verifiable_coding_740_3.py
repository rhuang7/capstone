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
        for _ in range(K):
            r = int(data[idx]) - 1
            c = int(data[idx+1]) - 1
            plants.append((r, c))
            idx += 2
        
        # Compute the minimum fence length
        # The minimum fence length is equal to the perimeter of the union of all plant cells
        # We can compute this by finding the minimum and maximum row and column of the plants
        min_r = min(p[0] for p in plants)
        max_r = max(p[0] for p in plants)
        min_c = min(p[1] for p in plants)
        max_c = max(p[1] for p in plants)
        
        # The perimeter is 2*(width + height)
        perimeter = 2 * ((max_r - min_r) + (max_c - min_c))
        results.append(perimeter)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()