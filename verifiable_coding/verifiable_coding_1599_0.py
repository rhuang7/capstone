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
        
        # Compute parity of distance between all pairs
        # Using BFS for each node
        parity = [0] * (N + 1)
        for start in range(1, N + 1):
            visited = [False] * (N + 1)
            q = deque()
            q.append(start)
            visited[start] = True
            dist = 0
            while q:
                for _ in range(len(q)):
                    u = q.popleft()
                    if u == start:
                        dist += 1
                    for v in adj[u]:
                        if not visited[v]:
                            visited[v] = True
                            q.append(v)
                if q:
                    dist += 1
            parity[start] = dist % 2
        
        # Compute number of pairs (c_c, c_m) where parity of bit difference equals parity of distance
        count = 0
        for i in range(N):
            for j in range(i, N):
                c_c = i + 1
                c_m = j + 1
                diff = bin(a[i] ^ a[j]).count('1')
                if (diff % 2) == parity[c_c]:
                    count += 1
        results.append(count)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()