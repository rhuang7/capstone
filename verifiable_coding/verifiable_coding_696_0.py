import sys
import math

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
        P = list(map(int, data[idx:idx+N]))
        idx += N
        intervals = []
        for _ in range(M):
            L = int(data[idx])
            R = int(data[idx+1])
            intervals.append((L, R))
            idx += 2
        
        # Build the graph of connected components
        graph = [[] for _ in range(N+1)]
        for L, R in intervals:
            graph[L].append(R)
            graph[R].append(L)
        
        # Find connected components using BFS
        visited = [False] * (N+1)
        components = []
        for i in range(1, N+1):
            if not visited[i]:
                q = [i]
                visited[i] = True
                comp = []
                while q:
                    u = q.pop()
                    comp.append(u)
                    for v in graph[u]:
                        if not visited[v]:
                            visited[v] = True
                            q.append(v)
                components.append(comp)
        
        # Check if the target permutation is achievable
        pos = [0] * (N+1)
        for i in range(N):
            pos[P[i]] = i + 1
        
        possible = True
        for comp in components:
            # Find the positions in the component in the target permutation
            comp_pos = [pos[x] for x in comp]
            comp_pos.sort()
            # Check if the positions in the component are contiguous
            start = comp_pos[0]
            end = comp_pos[-1]
            if end - start + 1 != len(comp):
                possible = False
                break
        
        results.append("Possible" if possible else "Impossible")
    
    sys.stdout.write('\n'.join(results) + '\n')

if __name__ == '__main__':
    solve()