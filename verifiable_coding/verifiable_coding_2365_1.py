import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        segments = []
        for _ in range(n-1):
            k = int(data[idx])
            idx += 1
            seg = list(map(int, data[idx:idx+k]))
            idx += k
            segments.append(seg)
        
        # Build a graph where each node is a number and edges represent possible positions
        graph = {i: [] for i in range(1, n+1)}
        for seg in segments:
            for i in range(len(seg)):
                for j in range(i+1, len(seg)):
                    a = seg[i]
                    b = seg[j]
                    graph[a].append(b)
                    graph[b].append(a)
        
        # Find the permutation using DFS
        visited = [False] * (n+1)
        result = [0] * n
        
        def dfs(u, pos):
            visited[u] = True
            result[pos] = u
            for v in graph[u]:
                if not visited[v]:
                    dfs(v, pos+1)
        
        # Start with the number that has no incoming edges (the first element)
        # Find the number with no incoming edges
        start = 1
        for i in range(1, n+1):
            if len(graph[i]) == 0:
                start = i
                break
        
        dfs(start, 0)
        results.append(' '.join(map(str, result)) + ' ')
    
    print(''.join(results))

if __name__ == '__main__':
    solve()