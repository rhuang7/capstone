import sys
import sys
sys.setrecursionlimit(10000)

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(T):
        N = int(data[idx])
        M = int(data[idx+1])
        idx += 2
        adj = [[] for _ in range(N)]
        for _ in range(M):
            a = int(data[idx])
            b = int(data[idx+1])
            adj[a].append(b)
            adj[b].append(a)
            idx += 2
        
        visited = [False] * N
        count = 0
        
        def dfs(u):
            visited[u] = True
            for v in adj[u]:
                if not visited[v]:
                    dfs(v)
        
        for i in range(N):
            if not visited[i]:
                dfs(i)
                count += 1
        
        results.append(str(count))
    
    print('\n'.join(results)) if results else None

if __name__ == '__main__':
    solve()