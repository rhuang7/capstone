import sys
import math
from collections import defaultdict, deque

def solve():
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
        
        # Precompute parity of the number of bits
        # For each node, store the parity of the number of set bits in a[i]
        # Also, precompute the distance between all pairs of nodes
        # But since the tree is big, we need an efficient way to compute distances
        # We'll use BFS for each node to compute distances
        
        # Precompute parity of set bits
        parity = [0] * (N + 1)
        for i in range(1, N + 1):
            cnt = 0
            x = a[i - 1]
            while x:
                cnt += x & 1
                x >>= 1
            parity[i] = cnt % 2
        
        # Precompute distances using BFS
        dist = [dict() for _ in range(N + 1)]
        
        for start in range(1, N + 1):
            q = deque()
            q.append(start)
            visited = [False] * (N + 1)
            visited[start] = True
            dist[start][start] = 0
            while q:
                u = q.popleft()
                for v in adj[u]:
                    if not visited[v]:
                        visited[v] = True
                        dist[start][v] = dist[start][u] + 1
                        q.append(v)
        
        # Count valid pairs
        count = 0
        for c_c in range(1, N + 1):
            for c_m in range(1, N + 1):
                # Compute the number of differing bits
                diff = 0
                x = a[c_c - 1]
                y = a[c_m - 1]
                while x or y:
                    diff += (x & 1) ^ (y & 1)
                    x >>= 1
                    y >>= 1
                # Compute parity of diff
                parity_diff = diff % 2
                # Compute parity of distance
                parity_dist = dist[c_c][c_m] % 2
                if parity_diff == parity_dist:
                    count += 1
        results.append(count)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()