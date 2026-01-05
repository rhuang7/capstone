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
            for neighbor in tree[node]:
                if not visited[neighbor]:
                    dfs(neighbor, node)
        dfs(u, -1)
        path2 = []
        visited = [False] * N
        def dfs2(node, parent):
            visited[node] = True
            path2.append(node)
            for neighbor in tree[node]:
                if not visited[neighbor]:
                    dfs2(neighbor, node)
        dfs2(v, -1)
        common = []
        i = 0
        j = 0
        while i < len(path) and j < len(path2):
            if path[i] == path2[j]:
                common.append(path[i])
                i += 1
                j += 1
            elif path[i] < path2[j]:
                i += 1
            else:
                j += 1
        return common

    def solve():
        for t, x, y in queries:
            path = get_path(x, y)
            values = [A[i] for i in path]
            min_diff = float('inf')
            max_diff = 0
            for i in range(len(values)):
                for j in range(i+1, len(values)):
                    diff = abs(values[i] - values[j])
                    if diff < min_diff:
                        min_diff = diff
                    if diff > max_diff:
                        max_diff = diff
            if t == 'C':
                print(min_diff)
            else:
                print(max_diff)

    if __name__ == '__main__':
        solve()