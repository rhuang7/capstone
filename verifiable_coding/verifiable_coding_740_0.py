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
        
        # Compute the minimum fence length
        # The minimum fence length is the perimeter of the convex hull of the plants
        # We need to compute the convex hull of the plant positions
        # Then compute the perimeter of the convex hull
        # But since N and M are up to 1e9, we cannot use standard convex hull algorithms
        # Instead, we can use the fact that the minimum fence is the perimeter of the minimal rectangle that contains all plants
        # But that's not correct either, because the plants may form a connected region
        # The correct approach is to find the minimal perimeter that separates the plants from the weeds
        # This is equivalent to finding the minimal perimeter of the connected component of plants
        # But since the plants are sparse, we can use a BFS or DFS to find the connected component
        # However, since N and M are up to 1e9, we cannot store the grid
        # Instead, we can use a BFS on the plant positions to find the connected component
        # Then compute the perimeter of that component
        
        # Convert plant positions to a set for O(1) lookups
        plant_set = set(plants)
        
        # BFS to find connected component
        visited = set()
        queue = []
        for r, c in plants:
            if (r, c) not in visited:
                queue.append((r, c))
                visited.add((r, c))
                while queue:
                    x, y = queue.pop(0)
                    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        nx, ny = x + dx, y + dy
                        if (nx, ny) in plant_set and (nx, ny) not in visited:
                            visited.add((nx, ny))
                            queue.append((nx, ny))
        
        # Now, compute the perimeter of the connected component
        # The perimeter is the number of edges between the component and the outside
        # We can compute this by checking for each plant whether its neighbors are outside the component
        # But since N and M are large, we can't check all neighbors
        # Instead, we can count the number of edges between the component and the outside
        # For each plant, check if the cell above, below, left, right is not in the component
        # But since the component is connected, we can use the fact that the perimeter is equal to the number of edges between the component and the outside
        # This is equivalent to the number of edges between the component and the outside, which can be computed as follows:
        # For each plant, check if the cell above is not in the component, and if so, add 1 to the perimeter
        # Similarly for the cell below, left, and right
        
        # But since the plants are sparse, we can check for each plant whether its neighbors are outside the component
        # So, we can iterate over all plants and check their four neighbors
        # But since the plants are sparse, this is feasible
        
        perimeter = 0
        for r, c in plants:
            # Check top
            if (r - 1, c) not in plant_set:
                perimeter += 1
            # Check bottom
            if (r + 1, c) not in plant_set:
                perimeter += 1
            # Check left
            if (r, c - 1) not in plant_set:
                perimeter += 1
            # Check right
            if (r, c + 1) not in plant_set:
                perimeter += 1
        
        results.append(perimeter)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()