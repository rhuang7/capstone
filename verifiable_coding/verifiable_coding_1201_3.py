import sys
import math
from collections import deque

def solve():
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
        
        # Preprocess for each cell, the maximum power it can be part of
        # For each cell (i,j), store the maximum power value such that A[i][j] < power
        max_power = [[0]*W for _ in range(H)]
        for i in range(H):
            for j in range(W):
                max_power[i][j] = 10**18  # a very large number
        
        # For each cell, find the maximum power it can be part of
        # This is simply the value of A[i][j] + 1, since A[i][j] < power
        for i in range(H):
            for j in range(W):
                max_power[i][j] = A[i][j] + 1
        
        # For each query, perform BFS
        for r, c, p in queries:
            if A[r][c] >= p:
                results.append(0)
                continue
            visited = [[False]*W for _ in range(H)]
            q = deque()
            q.append((r, c))
            visited[r][c] = True
            count = 0
            while q:
                x, y = q.popleft()
                count += 1
                for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                    nx = x + dx
                    ny = y + dy
                    if 0 <= nx < H and 0 <= ny < W and not visited[nx][ny] and A[nx][ny] < p:
                        visited[nx][ny] = True
                        q.append((nx, ny))
            results.append(count)
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()