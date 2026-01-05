import sys
import math
from collections import defaultdict, deque

def main():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    
    N = int(data[idx])
    idx += 1
    
    A = list(map(int, data[idx:idx+N]))
    idx += N
    
    tree = defaultdict(list)
    for _ in range(N-1):
        u = int(data[idx]) - 1
        v = int(data[idx+1]) - 1
        tree[u].append(v)
        tree[v].append(u)
        idx += 2
    
    Q = int(data[idx])
    idx += 1
    
    queries = []
    for _ in range(Q):
        t = data[idx]
        x = int(data[idx+1]) - 1
        y = int(data[idx+2]) - 1
        queries.append((t, x, y))
        idx += 3
    
    def get_path(u, v):
        path = []
        visited = [False] * N
        def dfs(node, parent):
            visited[node] = True
            path.append(node)
            for nei in tree[node]:
                if not visited[nei]:
                    dfs(nei, node)
        dfs(u, -1)
        idx = path.index(v)
        return path[:idx+1]
    
    def solve():
        for t, x, y in queries:
            path = get_path(x, y)
            values = [A[i] for i in path]
            if t == 'C':
                min_diff = float('inf')
                for i in range(len(values)):
                    for j in range(i+1, len(values)):
                        diff = abs(values[i] - values[j])
                        if diff < min_diff:
                            min_diff = diff
                print(min_diff)
            else:
                max_diff = 0
                for i in range(len(values)):
                    for j in range(i+1, len(values)):
                        diff = abs(values[i] - values[j])
                        if diff > max_diff:
                            max_diff = diff
                print(max_diff)
    
    if __name__ == '__main__':
        solve()

main()