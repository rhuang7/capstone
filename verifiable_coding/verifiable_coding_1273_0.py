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
        # We will try all living houses as the starting point and compute the max distance
        # The answer is the minimum of these max distances + 1 (time to place the perfume)
        
        min_time = float('inf')
        
        for (x, y) in living:
            # BFS from (x, y)
            q = collections.deque()
            q.append((x, y, 0))
            visited = set()
            visited.add((x, y))
            max_dist = 0
            
            while q:
                i, j, dist = q.popleft()
                max_dist = max(max_dist, dist)
                
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        if dx == 0 and dy == 0:
                            continue
                        ni = i + dx
                        nj = j + dy
                        if 0 <= ni < n and 0 <= nj < m and (ni, nj) not in visited:
                            visited.add((ni, nj))
                            q.append((ni, nj, dist + 1))
            
            min_time = min(min_time, max_dist + 1)
        
        results.append(min_time)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()