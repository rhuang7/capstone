import sys
import math

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
        graph = [[] for _ in range(N+1)]  # 1-based
        for L, R in intervals:
            for i in range(L, R+1):
                graph[i].append(i+1)
                graph[i+1].append(i)
        
        # Find connected components
        visited = [False] * (N+1)
        components = []
        for i in range(1, N+1):
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
        
        # Check if the target permutation is possible
        possible = True
        for comp in components:
            # Get the positions in the component
            positions = comp
            # Get the values in the target permutation at these positions
            values = [P[i-1] for i in positions]
            # Check if the values can be rearranged within the component
            # The values must be a permutation of the positions
            if sorted(values) != sorted(positions):
                possible = False
                break
        
        results.append("Possible" if possible else "Impossible")
    
    sys.stdout.write('\n'.join(results) + '\n')

if __name__ == '__main__':
    solve()