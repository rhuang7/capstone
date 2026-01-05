import sys
import math
from collections import deque

def solve():
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
        
        A = []
        for _ in range(H):
            row = list(map(int, data[idx:idx+W]))
            A.append(row)
            idx += W
        
        queries = []
        for _ in range(Q):
            r = int(data[idx]) - 1
            c = int(data[idx+1]) - 1
            p = int(data[idx+2])
            queries.append((r, c, p))
            idx += 3
        
        # Preprocess for each cell, the maximum power it can be reached with
        # We'll use BFS for each cell to find the maximum power it can reach
        # But since Q is large, we need a better way
        # Instead, for each query, we'll perform BFS from the starting cell with the given power
        
        for r, c, p in queries:
            if A[r][c] >= p:
                results.append(0)
                continue
            
            visited = [[False]*W for _ in range(H)]
            q = deque()
            q.append((r, c))
            visited[r][c] = True
            count = 1
            
            while q:
                x, y = q.popleft()
                for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                    nx = x + dx
                    ny = y + dy
                    if 0 <= nx < H and 0 <= ny < W and not visited[nx][ny] and A[nx][ny] < p:
                        visited[nx][ny] = True
                        count += 1
                        q.append((nx, ny))
            
            results.append(count)
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()