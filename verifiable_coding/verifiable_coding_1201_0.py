import sys
import bisect
from collections import deque

def main():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(T):
        H = int(data[idx])
        W = int(data[idx+1])
        Q = int(data[idx+2])
        idx += 3
        
        grid = []
        for _ in range(H):
            row = list(map(int, data[idx:idx+W]))
            grid.append(row)
            idx += W
        
        # Preprocess for each cell, sort the neighbors by height
        # For each cell (i,j), store a list of (height, (i,j)) of adjacent cells
        # But since we need to find all cells reachable with height < p, we can precompute for each cell the sorted list of heights
        # and use binary search to find the maximum height that is less than p
        # However, since the grid is large (up to 1000x1000), we need an efficient way to handle queries
        
        # For each cell (i,j), precompute the sorted list of heights of adjacent cells
        # But since we need to find all cells reachable with height < p, we can use BFS with a priority queue (Dijkstra-like approach)
        # However, for each query, doing BFS would be too slow for Q up to 2e5
        
        # Alternative approach: For each query (r, c, p), check if A[r-1][c-1] >= p, if so, output 0
        # Otherwise, perform BFS starting from (r-1, c-1) and count all cells with height < p
        
        # But with Q up to 2e5 and H, W up to 1000, this would be O(Q*H*W) which is too slow
        
        # So we need a better approach
        
        # Let's try to precompute for each cell (i,j) the set of cells that can be reached from it with height < p, for all p
        # But this is not feasible
        
        # So we'll use the BFS approach for each query, but optimize it as much as possible
        
        # Read the queries
        queries = []
        for _ in range(Q):
            r = int(data[idx])
            c = int(data[idx+1])
            p = int(data[idx+2])
            queries.append((r-1, c-1, p))  # convert to 0-based
            idx += 3
        
        # Process each query
        for r, c, p in queries:
            if grid[r][c] >= p:
                results.append(0)
                continue
            # BFS
            visited = set()
            q = deque()
            q.append((r, c))
            visited.add((r, c))
            count = 0
            while q:
                x, y = q.popleft()
                count += 1
                for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                    nx = x + dx
                    ny = y + dy
                    if 0 <= nx < H and 0 <= ny < W and (nx, ny) not in visited and grid[nx][ny] < p:
                        visited.add((nx, ny))
                        q.append((nx, ny))
            results.append(count)
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    main()