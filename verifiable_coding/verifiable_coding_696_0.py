import sys
import collections

def solve():
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
        graph = collections.defaultdict(list)
        for L, R in intervals:
            graph[L].append(R)
            graph[R].append(L)
        
        # Find connected components
        visited = [False] * (N + 1)
        components = []
        for i in range(1, N + 1):
            if not visited[i]:
                stack = [i]
                visited[i] = True
                comp = []
                while stack:
                    node = stack.pop()
                    comp.append(node)
                    for neighbor in graph[node]:
                        if not visited[neighbor]:
                            visited[neighbor] = True
                            stack.append(neighbor)
                components.append(comp)
        
        # Check if the permutation can be achieved
        possible = True
        for comp in components:
            # Get the positions in this component
            pos = [i for i in range(1, N + 1) if i in comp]
            # Get the values in this component of the target permutation
            val = [P[i-1] for i in pos]
            # Check if the values are a permutation of the positions
            if sorted(val) != sorted(pos):
                possible = False
                break
        
        results.append("Possible" if possible else "Impossible")
    
    print("\n".join(results))