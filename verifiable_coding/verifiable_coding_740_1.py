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
            r = int(data[idx])
            c = int(data[idx+1])
            plants.append((r, c))
            idx += 2
        
        # Convert to 0-based indices
        plants = [(r-1, c-1) for r, c in plants]
        
        # Compute the minimum fence length
        # The minimum fence length is the perimeter of the bounding box of the plants
        # minus the number of edges between adjacent plants (each such edge reduces the perimeter by 2)
        min_fences = 0
        
        # Find the bounding box
        min_r, max_r = min(p[0] for p in plants), max(p[0] for p in plants)
        min_c, max_c = min(p[1] for p in plants), max(p[1] for p in plants)
        
        # Perimeter of the bounding box
        perimeter = 2 * ((max_r - min_r + 1) + (max_c - min_c + 1))
        
        # Count the number of adjacent plant pairs
        adj_count = 0
        plant_set = set(plants)
        for r, c in plants:
            if (r, c+1) in plant_set:
                adj_count += 1
            if (r+1, c) in plant_set:
                adj_count += 1
        
        # Each adjacent pair reduces the perimeter by 2
        min_fences = perimeter - 2 * adj_count
        
        results.append(str(min_fences))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()