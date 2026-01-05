import sys
import collections

def solve():
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
        
        # Find all positions of '*' (people)
        people = []
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '*':
                    people.append((i, j))
        
        if not people:
            print(0)
            continue
        
        # BFS to find the minimum time to infect all people
        # We need to find the best position to place the perfume such that the maximum distance from any person is minimized
        # We will try all possible positions to place the perfume and find the minimum maximum distance
        
        min_time = float('inf')
        
        # Try placing perfume at each person's position
        for (x, y) in people:
            # BFS from (x, y) to find the maximum distance to any person
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
        
        # Try placing perfume at each empty cell (not a person)
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '.':
                    # BFS from (i, j) to find the maximum distance to any person
                    visited = [[-1 for _ in range(m)] for _ in range(n)]
                    q = collections.deque()
                    q.append((i, j))
                    visited[i][j] = 0
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
        
        print(min_time + 1)  # +1 for the time to place the perfume

if __name__ == '__main__':
    solve()