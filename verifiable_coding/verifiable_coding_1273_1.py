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
        
        # Find all positions of '*' (people)
        people = []
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '*':
                    people.append((i, j))
        
        if not people:
            results.append(0)
            continue
        
        # BFS to find the minimum time to infect all people
        # We need to find the best position to put the perfume such that the maximum distance from it to any person is minimized
        # This is equivalent to finding the minimum radius of a circle that covers all people, with the center being a cell in the grid
        
        # For each person, perform BFS to find the minimum time to infect all people if we put the perfume at that person's position
        # The answer is the minimum of these maximum times
        
        min_time = float('inf')
        
        for (x, y) in people:
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
                            max_dist = max(max_dist, visited[nx][ny])
                            q.append((nx, ny))
            
            min_time = min(min_time, max_dist)
        
        results.append(min_time)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()