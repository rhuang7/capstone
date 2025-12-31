import sys
import math
from collections import deque

def main():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    
    N = int(data[idx])
    idx += 1
    
    A = list(map(int, data[idx:idx+N]))
    idx += N
    
    tree = [[] for _ in range(N+1)]
    for _ in range(N-1):
        u = int(data[idx])
        v = int(data[idx+1])
        tree[u].append(v)
        tree[v].append(u)
        idx += 2
    
    Q = int(data[idx])
    idx += 1
    
    queries = []
    for _ in range(Q):
        t = data[idx]
        x = int(data[idx+1])
        y = int(data[idx+2])
        queries.append((t, x, y))
        idx += 3
    
    def get_path(u, v):
        parent = [0]*(N+1)
        visited = [False]*(N+1)
        q = deque()
        q.append(u)
        visited[u] = True
        while q:
            node = q.popleft()
            if node == v:
                break
            for nei in tree[node]:
                if not visited[nei]:
                    visited[nei] = True
                    parent[nei] = node
                    q.append(nei)
        path = []
        while v != 0:
            path.append(v)
            v = parent[v]
        path.append(u)
        return path[::-1]
    
    def get_min_diff(path):
        min_diff = float('inf')
        values = [A[node-1] for node in path]
        for i in range(len(values)):
            for j in range(i+1, len(values)):
                diff = abs(values[i] - values[j])
                if diff < min_diff:
                    min_diff = diff
        return min_diff
    
    def get_max_diff(path):
        values = [A[node-1] for node in path]
        max_diff = 0
        for i in range(len(values)):
            for j in range(i+1, len(values)):
                diff = abs(values[i] - values[j])
                if diff > max_diff:
                    max_diff = diff
        return max_diff
    
    for t, x, y in queries:
        path = get_path(x, y)
        if t == 'C':
            print(get_min_diff(path))
        else:
            print(get_max_diff(path))

if __name__ == '__main__':
    main()