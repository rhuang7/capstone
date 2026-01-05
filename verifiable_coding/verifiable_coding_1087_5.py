import sys
import sys
sys.setrecursionlimit(1000000)

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    N = int(data[0])
    M = int(data[1])
    edges = data[2:]

    if M != N - 1:
        print("NO")
        return

    from collections import defaultdict
    graph = defaultdict(list)
    for i in range(0, len(edges), 2):
        u = int(edges[i])
        v = int(edges[i+1])
        graph[u].append(v)
        graph[v].append(u)

    visited = [False] * (N + 1)

    def dfs(node):
        visited[node] = True
        for neighbor in graph[node]:
            if not visited[neighbor]:
                if not dfs(neighbor):
                    return False
            else:
                return False
        return True

    if not dfs(1):
        print("NO")
    else:
        for i in range(2, N + 1):
            if not visited[i]:
                print("NO")
                return
        print("YES")

if __name__ == '__main__':
    solve()