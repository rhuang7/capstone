import sys
import sys
sys.setrecursionlimit(1 << 25)

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    N = int(data[idx])
    idx += 1
    M = int(data[idx])
    idx += 1

    if M < N - 1:
        print("NO")
        return

    adj = [[] for _ in range(N + 1)]
    for _ in range(M):
        u = int(data[idx])
        idx += 1
        v = int(data[idx])
        idx += 1
        adj[u].append(v)
        adj[v].append(u)

    visited = [False] * (N + 1)

    def dfs(node, parent):
        visited[node] = True
        for neighbor in adj[node]:
            if not visited[neighbor]:
                if dfs(neighbor, node):
                    return True
            elif neighbor != parent:
                return True
        return False

    if dfs(1, -1) or sum(visited[1:]) != N:
        print("NO")
    else:
        print("YES")

if __name__ == '__main__':
    solve()