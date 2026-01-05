import sys
import heapq

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    idx = 0
    T = int(data[idx])
    idx += 1
    
    for _ in range(T):
        n = int(data[idx])
        m = int(data[idx+1])
        idx += 2
        
        grid = []
        for i in range(n):
            row = data[idx]
            grid.append(row)
            idx += 1
        
        # Find all the positions of '*' (people)
        people = []
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '*':
                    people.append((i, j))
        
        if not people:
            print(0)
            continue
        
        # BFS to find the minimum time to infect all people
        # We need to find the optimal position to place the perfume
        # such that the maximum distance from that position to any person is minimized
        # This is the problem of finding the smallest maximum distance in a grid
        
        # For each cell, compute the maximum distance to any person
        # Then find the cell with the minimum such maximum distance
        
        # Precompute distances from all people to all cells
        # Using multi-source BFS
        
        dist = [[-1]*m for _ in range(n)]
        q = []
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '*':
                    dist[i][j] = 0
                    heapq.heappush(q, (0, i, j))
        
        dirs = [(-1, -1), (-1, 0), (-1, 1),
                (0, -1),          (0, 1),
                (1, -1),  (1, 0), (1, 1)]
        
        while q:
            d, i, j = heapq.heappop(q)
            for di, dj in dirs:
                ni, nj = i + di, j + dj
                if 0 <= ni < n and 0 <= nj < m and dist[ni][nj] == -1:
                    dist[ni][nj] = d + 1
                    heapq.heappush(q, (d + 1, ni, nj))
        
        # Now find the minimum of the maximum distance from any cell to all people
        min_time = float('inf')
        for i in range(n):
            for j in range(m):
                if dist[i][j] != -1:
                    max_dist = max(dist[i][j], 0)
                    min_time = min(min_time, max_dist)
        
        print(min_time)

if __name__ == '__main__':
    solve()