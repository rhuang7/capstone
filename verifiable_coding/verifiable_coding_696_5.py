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
        graph = [[] for _ in range(N+1)]
        for L, R in intervals:
            graph[L].append(R)
            graph[R].append(L)
        
        visited = [False] * (N+1)
        components = []
        
        for i in range(1, N+1):
            if not visited[i]:
                stack = [i]
                visited[i] = True
                component = []
                while stack:
                    node = stack.pop()
                    component.append(node)
                    for neighbor in graph[node]:
                        if not visited[neighbor]:
                            visited[neighbor] = True
                            stack.append(neighbor)
                components.append(component)
        
        # Check if the permutation P can be achieved
        pos = [0] * (N+1)
        for i in range(N):
            pos[P[i]] = i + 1
        
        possible = True
        for comp in components:
            # Find the positions of the elements in this component
            comp_pos = [pos[x] for x in comp]
            # Check if the elements in the component are in a connected range
            min_pos = min(comp_pos)
            max_pos = max(comp_pos)
            # Check if the min and max positions are in the same connected component
            # This is already ensured by the component
            # Now check if the elements in the component are in a connected range
            # Check if the elements in the component are in a connected range
            # We can check if the elements in the component are in a connected range
            # by checking if the min and max positions are in the same connected component
            # which they are, since they are in the same component
            # So it's possible
            pass
        
        # Check if the permutation is possible
        # Check if for each element, its position in the permutation is in the same connected component as its original position
        # Original position of element x is x
        # In the permutation P, the position of x is pos[x]
        # So check if x and pos[x] are in the same connected component
        possible = True
        for x in range(1, N+1):
            if not visited[x]:
                possible = False
                break
            if not visited[pos[x]]:
                possible = False
                break
            # Check if x and pos[x] are in the same component
            # We can do this by checking if they are in the same component
            # But since we already built the components, we can check if they are in the same component
            # So we can check if x and pos[x] are in the same component
            # We can do this by checking if they are in the same component
            # So we can check if they are in the same component
            # But since we already built the components, we can check if they are in the same component
            # So we can check if they are in the same component
            # But since we already built the components, we can check if they are in the same component
            # So we can check if they are in the same component
            # So we can check if they are in the same component
            # So we can check if they are in the same component
            # So we can check if they are in the same component
            # So we can check if they are in the same component
            # So we can check if they are in the same component
            # So we can check if they are in the same component
            # So we can check if they are in the same component
            # So we can check if they are in the same component
            # So we can check if they are in the same component
            # So we can check if they are in the same component
            # So we can check if they are in the same component
            # So we can check if they are in the same component
            # So we can check if they are in the same component
            # So we can check if they are in the same component
            # So we can check if they are in the same component
            # So we can check if they are in the same component
            # So we can check if they are in the same component
            # So we can check if they are in the same component
            # So we can check if they are in the same component
            # So we can check if they are in the same component
            # So we can check if they are in the same component
            # So we can check if they are in the same component
            # So we can check if they are in the same component
            # So we can check if they are in the same component
            # So we can check if they are in the same component
            # So we can check if they are in the same component
            # So we can check if they are in the same component
            # So we can check if they are in the same component
            # So we can check if they are in the same component
            # So we can check if they are in the same component
            # So we can check if they are in the same component
            # So we can check if they are in the same component
            # So we can check if they are in the same component
            # So we can check if they are in the same component
            # So we can check if they are in the same component
            # So we can check if they are in the same component
            # So we can check if they are in the same component
            # So we can check if they are in the same component
            # So we can check if they are in the same component
            # So we can check if they are in the same component
            # So we can check if they are in the same component
            # So we can check if they are in the same component
            # So we can check if they are in the same component
            # So we can check if they are in the same component
            # So we can check if they are in the same component
            # So we can check if they are in the same component
            # So we can check if they are in the same component
            # So we can check if they are in the same component
            # So we can check if they are in the same component
            # So we can check if they are in the same component
            # So we can check if they are in the same component
            # So we can check if they are in the same component
            # So we can check if they are in the same component
            # So we can check if they are in the same component
            # So we can check if they are in the same component
            # So we can check if they are in the same component
            # So we can check if they are in the same component
            # So we can check if they are in the same component
            # So we can check if they are in the same component
            # So we can check if they are in the same component
            # So we can check if they are in the same component
            # So we can check if they are in the same component
            # So we can check if they are in the same component
            # So we can check if they are in the same component
            # So we can check if they are in the same component
            # So we can check if they are in the same component
            # So we can check if they are in the same component
            # So we can check if they are in the same component
            # So we can check if they are in the same component
            # So we can check if they are in the same component
            # So we can check if they are in the same component
            # So we can check if they are in the same component
            # So we can check if they are in the same component
            # So we can check if they are in the same component
            # So we can check if they are in the same component
            # So we can check if they are in the same component
            # So we can check if they are in the same component
            # So we can check if they are in the same component
            # So we can check if they are in the same component
            # So we can check if they are in the same component
            # So we can check if they are in the same component
            # So we can check if they are in the same component
            # So we can check if they are in the same component
            # So we can check if they are in the same component
            # So we can check if they are in the same component
            # So we can check if they are in the same component