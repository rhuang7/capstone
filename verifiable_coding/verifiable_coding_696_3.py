import sys
import collections

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
                component = []
                while stack:
                    node = stack.pop()
                    component.append(node)
                    for neighbor in graph[node]:
                        if not visited[neighbor]:
                            visited[neighbor] = True
                            stack.append(neighbor)
                components.append(component)
        
        # Check if the permutation can be achieved
        possible = True
        for comp in components:
            # Get the positions in the component
            pos = sorted(comp)
            # Get the values in the permutation at these positions
            vals = [P[i - 1] for i in pos]
            # Check if the values are a permutation of 1..N
            if sorted(vals) != list(range(1, N + 1)):
                possible = False
                break
        
        results.append("Possible" if possible else "Impossible")
    
    print("\n".join(results))

if __name__ == '__main__':
    solve()