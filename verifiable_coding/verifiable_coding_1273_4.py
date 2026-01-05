import sys
import collections

def solve():
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(T):
        n = int(data[idx])
        m = int(data[idx+1])
        idx += 2
        grid = []
        for i in range(n):
            row = data[idx]
            grid.append(row)
            idx += 1
        
        # Find all living houses
        living = []
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '*':
                    living.append((i, j))
        
        if not living:
            results.append(0)
            continue
        
        # BFS to find the minimum time to infect all living houses
        # We need to find the best position to place the perfume such that the maximum distance to any living house is minimized
        # We'll perform BFS from each living house and find the maximum distance, then take the minimum of those maximum distances
        
        min_time = float('inf')
        
        for (x, y) in living:
            # BFS from (x, y)
            q = collections.deque()
            q.append((x, y, 0))
            visited = [[False]*m for _ in range(n)]
            visited[x][y] = True
            max_dist = 0
            
            while q:
                i, j, d = q.popleft()
                max_dist = max(max_dist, d)
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        if dx == 0 and dy == 0:
                            continue
                        ni, nj = i + dx, j + dy
                        if 0 <= ni < n and 0 <= nj < m and not visited[ni][nj]:
                            visited[ni][nj] = True
                            q.append((ni, nj, d + 1))
            
            min_time = min(min_time, max_dist)
        
        results.append(min_time)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()