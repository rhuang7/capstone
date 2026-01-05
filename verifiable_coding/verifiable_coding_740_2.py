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
        # The minimum fence length is equal to the total perimeter of the plant region minus the internal edges
        # We can use BFS to find the connected components of plants
        # For each connected component, the perimeter is 4 * number of cells - 2 * number of internal edges
        # So we need to find the number of internal edges between plants
        
        # Use BFS to find connected components
        visited = set()
        total_internal_edges = 0
        
        for (r, c) in plants:
            if (r, c) not in visited:
                # BFS to find the connected component
                q = [(r, c)]
                visited.add((r, c))
                component = [(r, c)]
                while q:
                    x, y = q.pop(0)
                    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        nx, ny = x + dx, y + dy
                        if (nx, ny) in plants and (nx, ny) not in visited:
                            visited.add((nx, ny))
                            q.append((nx, ny))
                            component.append((nx, ny))
                
                # Count internal edges
                for (x, y) in component:
                    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        nx, ny = x + dx, y + dy
                        if (nx, ny) in plants:
                            total_internal_edges += 1
        
        # Total perimeter is 4 * K - 2 * total_internal_edges
        total_perimeter = 4 * K - 2 * total_internal_edges
        results.append(total_perimeter)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()