import sys
import sys
sys.setrecursionlimit(1000000)

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    N = int(data[idx])
    idx += 1
    M = int(data[idx])
    idx += 1

    from collections import defaultdict
    graph = defaultdict(list)
    for _ in range(M):
        u = int(data[idx])
        idx += 1
        v = int(data[idx])
        idx += 1
        graph[u].append(v)
        graph[v].append(u)

    visited = [False] * (N + 1)
    parent = [0] * (N + 1)

    def dfs(node, p):
        visited[node] = True
        parent[node] = p
        for neighbor in graph[node]:
            if not visited[neighbor]:
                if dfs(neighbor, node):
                    return True
            elif neighbor != p:
                return True
        return False

    if M != N - 1:
        print("NO")
        return

    if dfs(1, -1):
        print("NO")
    else:
        print("YES")

if __name__ == '__main__':
    solve()