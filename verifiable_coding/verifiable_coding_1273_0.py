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
        # We need to find the optimal position to place the perfume
        # such that the maximum distance from this position to any person is minimized
        # This is the problem of finding the smallest maximum distance in a grid
        
        # Function to compute the maximum distance from a given position to all people
        def max_dist(x, y):
            q = collections.deque()
            q.append((x, y, 0))
            visited = set()
            visited.add((x, y))
            max_time = 0
            while q:
                i, j, time = q.popleft()
                max_time = max(max_time, time)
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        if dx == 0 and dy == 0:
                            continue
                        ni, nj = i + dx, j + dy
                        if 0 <= ni < n and 0 <= nj < m and (ni, nj) not in visited:
                            visited.add((ni, nj))
                            q.append((ni, nj, time + 1))
            return max_time
        
        # Find the optimal position to place the perfume
        min_max_time = float('inf')
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '.':
                    current_max = max_dist(i, j)
                    if current_max < min_max_time:
                        min_max_time = current_max
        
        results.append(min_max_time)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()