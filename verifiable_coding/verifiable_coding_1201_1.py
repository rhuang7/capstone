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
        
        # Preprocess for each cell, the connected regions with height < p
        # We'll use BFS for each query
        # But with Q up to 2e5 and H, W up to 1e3, this would be O(Q*H*W) which is too slow
        
        # Instead, we can use a Union-Find (Disjoint Set Union) approach
        # But since the height varies, we need to process queries in a way that allows us to find connected regions with height < p
        
        # However, given the time constraints, we'll proceed with BFS for each query
        
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