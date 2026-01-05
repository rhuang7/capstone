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
        # We need to find the best position to place the perfume such that the maximum distance from any living house is minimized
        # This is equivalent to finding the minimum radius of a circle that covers all living houses, where the circle is centered at some cell
        
        # For each living house, perform BFS to find the maximum distance to other living houses
        # The minimum of these maximum distances is the answer
        
        min_time = float('inf')
        
        for (x, y) in living:
            # BFS from (x, y)
            visited = [[-1 for _ in range(m)] for _ in range(n)]
            q = collections.deque()
            q.append((x, y))
            visited[x][y] = 0
            max_dist = 0
            
            while q:
                cx, cy = q.popleft()
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        if dx == 0 and dy == 0:
                            continue
                        nx = cx + dx
                        ny = cy + dy
                        if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == -1:
                            visited[nx][ny] = visited[cx][cy] + 1
                            q.append((nx, ny))
                            max_dist = max(max_dist, visited[nx][ny])
            
            min_time = min(min_time, max_dist)
        
        results.append(min_time)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()