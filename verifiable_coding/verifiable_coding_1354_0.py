import sys
MOD = 10**9 + 7

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    for _ in range(T):
        n, k = int(data[idx]), int(data[idx+1])
        idx += 2
        edges = []
        for _ in range(n-1):
            u = int(data[idx]) - 1
            v = int(data[idx+1]) - 1
            edges.append((u, v))
            idx += 2
        # Build adjacency list
        from collections import defaultdict
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        # Perform BFS to find the number of connected components
        visited = [False] * n
        components = 0
        for i in range(n):
            if not visited[i]:
                components += 1
                queue = [i]
                visited[i] = True
                while queue:
                    node = queue.pop(0)
                    for neighbor in adj[node]:
                        if not visited[neighbor]:
                            visited[neighbor] = True
                            queue.append(neighbor)
        # The number of ways is k^components
        # But if k == 1, then it's 1
        if k == 1:
            results.append(1)
        else:
            results.append(pow(k, components, MOD))
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()