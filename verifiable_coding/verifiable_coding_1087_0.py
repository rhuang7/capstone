import sys

def solve():
    import sys
    sys.setrecursionlimit(1000000)
    data = sys.stdin.buffer.read().split()
    idx = 0
    N = int(data[idx])
    idx += 1
    M = int(data[idx])
    idx += 1

    if M < N - 1:
        print("NO")
        return

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

    def dfs(node):
        visited[node] = True
        for neighbor in graph[node]:
            if not visited[neighbor]:
                if dfs(neighbor):
                    return True
            else:
                return True
        return False

    if dfs(1):
        print("NO")
    else:
        for i in range(2, N + 1):
            if not visited[i]:
                print("NO")
                return
        print("YES")

if __name__ == '__main__':
    solve()