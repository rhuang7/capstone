import sys
import heapq

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
        idx += 1
        adj = [[] for _ in range(N + 1)]
        for _ in range(N - 1):
            X = int(data[idx])
            Y = int(data[idx + 1])
            idx += 2
            adj[X].append(Y)
            adj[Y].append(X)
        
        # Perform BFS starting from node 1
        visited = [False] * (N + 1)
        q = [1]
        visited[1] = True
        order = []
        
        while q:
            u = q.pop(0)
            order.append(u)
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    q.append(v)
        
        results.append(' '.join(map(str, order)))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()