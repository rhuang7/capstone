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
        N, M = int(data[idx]), int(data[idx+1])
        idx += 2
        P = list(map(int, data[idx:idx+N]))
        idx += N
        intervals = []
        for _ in range(M):
            L = int(data[idx])
            R = int(data[idx+1])
            intervals.append((L, R))
            idx += 2
        
        # Build graph of connected components
        graph = [[] for _ in range(N+1)]  # 1-based
        for L, R in intervals:
            graph[L].append(R)
            graph[R].append(L)
        
        visited = [False] * (N+1)
        components = []
        
        def dfs(u):
            stack = [u]
            visited[u] = True
            component = []
            while stack:
                node = stack.pop()
                component.append(node)
                for neighbor in graph[node]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        stack.append(neighbor)
            return component
        
        for i in range(1, N+1):
            if not visited[i]:
                components.append(dfs(i))
        
        # Check if the permutation can be achieved
        pos = [0] * (N+1)  # pos[value] = position in permutation
        for i in range(N):
            pos[P[i]] = i + 1
        
        possible = True
        for comp in components:
            # Get the values in this component
            values = [P[i-1] for i in comp]
            # Check if the values can be rearranged within the component
            # The values must be a permutation of the positions in the component
            # So the values must be exactly the positions in the component
            if sorted(values) != sorted(comp):
                possible = False
                break
        
        results.append("Possible" if possible else "Impossible")
    
    sys.stdout.write('\n'.join(results) + '\n')

if __name__ == '__main__':
    solve()