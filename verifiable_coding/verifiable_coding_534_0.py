import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(T):
        n = int(data[idx])
        m = int(data[idx+1])
        idx += 2
        adj = [[] for _ in range(n+1)]
        for _ in range(m):
            u = int(data[idx])
            v = int(data[idx+1])
            adj[u].append(v)
            adj[v].append(u)
            idx += 2
        
        # Maximum antimatching is the maximum number of edges such that no two share a vertex
        # This is equivalent to finding a maximum matching in the line graph of the original graph
        # But since the line graph is not directly available, we can use the fact that the maximum antimatching
        # is the maximum matching in the original graph, but with the edges being non-overlapping
        
        # We can use a greedy approach to find the maximum antimatching
        used = [False] * (n + 1)
        count = 0
        
        for u in range(1, n + 1):
            if not used[u]:
                for v in adj[u]:
                    if not used[v]:
                        used[u] = True
                        used[v] = True
                        count += 1
                        break
        
        results.append(str(count))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()