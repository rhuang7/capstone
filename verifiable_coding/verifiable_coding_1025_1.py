import sys
import sys
from sys import stdin
import sys
input = sys.stdin.buffer.read
import sys
from collections import defaultdict, deque

def solve():
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    for _ in range(T):
        N, Q = int(data[idx]), int(data[idx+1])
        idx += 2
        A = list(map(int, data[idx:idx+N]))
        idx += N
        tree = defaultdict(list)
        for _ in range(N-1):
            u = int(data[idx]) - 1
            v = int(data[idx+1]) - 1
            tree[u].append(v)
            tree[v].append(u)
            idx += 2
        queries = []
        for _ in range(Q):
            queries.append(int(data[idx]) - 1)
            idx += 1
        # BFS to compute depth and parent
        depth = [0] * N
        parent = [ -1 ] * N
        visited = [False] * N
        q = deque()
        q.append(0)
        visited[0] = True
        while q:
            u = q.popleft()
            for v in tree[u]:
                if not visited[v] and v != parent[u]:
                    visited[v] = True
                    parent[v] = u
                    depth[v] = depth[u] + 1
                    q.append(v)
        # Process queries
        for v in queries:
            # Find all nodes in subtree of v with even distance from v (excluding v itself)
            # Perform BFS from v, only traverse subtree
            visited = [False] * N
            q = deque()
            q.append((v, 0))
            visited[v] = True
            while q:
                u, d = q.popleft()
                if d % 2 == 0 and u != v:
                    A[v] += A[u]
                    A[u] = 0
                for nei in tree[u]:
                    if not visited[nei] and nei != parent[u]:
                        visited[nei] = True
                        q.append((nei, d + 1))
        results.append(' '.join(map(str, A)))
    print('\n'.join(results))