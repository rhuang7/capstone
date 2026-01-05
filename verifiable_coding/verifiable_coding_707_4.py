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
        graph = [[] for _ in range(N + 1)]
        for _ in range(N - 1):
            X = int(data[idx])
            Y = int(data[idx + 1])
            idx += 2
            graph[X].append(Y)
            graph[Y].append(X)
        
        # BFS to find the order
        visited = [False] * (N + 1)
        order = []
        q = [1]
        visited[1] = True
        
        while q:
            u = q.pop(0)
            order.append(u)
            for v in graph[u]:
                if not visited[v]:
                    visited[v] = True
                    q.append(v)
        
        results.append(' '.join(map(str, order)))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()