import sys
import math
from collections import defaultdict, deque

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(T):
        N = int(data[idx])
        idx += 1
        adj = [[] for _ in range(N + 1)]
        for _ in range(N - 1):
            A = int(data[idx])
            B = int(data[idx + 1])
            adj[A].append(B)
            adj[B].append(A)
            idx += 2
        a = list(map(int, data[idx:idx + N]))
        idx += N
        
        # Precompute distances between all pairs of nodes
        # Using BFS for each node
        dist = [ [0] * (N + 1) for _ in range(N + 1) ]
        
        for start in range(1, N + 1):
            visited = [False] * (N + 1)
            q = deque()
            q.append(start)
            visited[start] = True
            while q:
                u = q.popleft()
                for v in adj[u]:
                    if not visited[v]:
                        visited[v] = True
                        dist[start][v] = dist[start][u] + 1
                        q.append(v)
        
        # Precompute XOR for all pairs
        xor = [0] * (N + 1)
        for i in range(1, N + 1):
            xor[i] = a[i - 1]
        
        # Count valid pairs
        count = 0
        for c_c in range(1, N + 1):
            for c_m in range(1, N + 1):
                xor_val = xor[c_c] ^ xor[c_m]
                diff = bin(xor_val).count('1')
                path_len = dist[c_c][c_m]
                if (diff % 2) == (path_len % 2):
                    count += 1
        results.append(count)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()