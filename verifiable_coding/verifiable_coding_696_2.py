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
        ranges = []
        for _ in range(M):
            L = int(data[idx])
            R = int(data[idx+1])
            ranges.append((L, R))
            idx += 2
        
        # Build graph of connected components
        graph = [[] for _ in range(N)]
        for L, R in ranges:
            graph[L-1].append(R-1)
            graph[R-1].append(L-1)
        
        # Find connected components
        visited = [False] * N
        components = []
        for i in range(N):
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
            pos = [i for i in comp]
            # Get the values in the permutation at these positions
            val = [P[i] for i in comp]
            # Sort the values
            val_sorted = sorted(val)
            # Check if the sorted values can be arranged within the component
            # Since we can shuffle any range, the values in the component must be a permutation of the sorted values
            # So the sorted values must be a permutation of the values in the component
            if sorted(val) != val_sorted:
                possible = False
                break
        
        results.append("Possible" if possible else "Impossible")
    
    sys.stdout.write('\n'.join(results) + '\n')

if __name__ == '__main__':
    solve()