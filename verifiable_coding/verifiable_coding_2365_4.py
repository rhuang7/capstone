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
        
        # Build a graph where edges represent possible positions
        graph = [[] for _ in range(n)]
        for seg in segments:
            for i in range(len(seg)):
                for j in range(i+1, len(seg)):
                    a = seg[i]
                    b = seg[j]
                    graph[a-1].append(b-1)
                    graph[b-1].append(a-1)
        
        # Find the permutation using BFS
        visited = [False] * n
        permutation = [0] * n
        q = []
        for i in range(n):
            if len(graph[i]) == 0:
                q.append(i)
                visited[i] = True
                permutation[i] = i + 1
        
        while q:
            u = q.pop(0)
            for v in graph[u]:
                if not visited[v]:
                    visited[v] = True
                    permutation[v] = v + 1
                    q.append(v)
        
        results.append(' '.join(map(str, permutation)) + ' ')
    
    print(''.join(results))

if __name__ == '__main__':
    solve()