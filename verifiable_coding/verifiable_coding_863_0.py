import sys
import collections

def solve():
    import sys
    sys.setrecursionlimit(1 << 25)
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    N = int(data[idx])
    idx += 1
    traffic = [0] * (N + 1)
    for i in range(1, N + 1):
        traffic[i] = int(data[idx])
        idx += 1
    adj = [[] for _ in range(N + 1)]
    for _ in range(N - 1):
        u = int(data[idx])
        v = int(data[idx + 1])
        adj[u].append(v)
        adj[v].append(u)
        idx += 2

    def dfs(u, parent):
        # Choose to take u
        take = traffic[u]
        # Choose not to take u
        notake = 0
        for v in adj[u]:
            if v == parent:
                continue
            notake += max(dfs(v, u))
        # Choose to take u and not take neighbors
        for v in adj[u]:
            if v == parent:
                continue
            take += dfs(v, u)
        return max(take, notake)

    result = dfs(1, -1)
    print(result)

if __name__ == '__main__':
    solve()