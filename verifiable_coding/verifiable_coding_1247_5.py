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
        N, D = int(data[idx]), int(data[idx+1])
        idx += 2
        P = list(map(int, data[idx:idx+N]))
        idx += N
        
        # Create a sorted version of P
        sorted_P = sorted(P)
        
        # Create a position map for the sorted array
        pos = {val: i for i, val in enumerate(sorted_P)}
        
        # Create a graph of allowed swaps
        graph = [[] for _ in range(N)]
        for i in range(N):
            val = P[i]
            target = val + D
            if target < N and pos[target] != i:
                graph[i].append(pos[target])
            target = val - D
            if target >= 0 and pos[target] != i:
                graph[i].append(pos[target])
        
        # Find cycles in the graph
        visited = [False] * N
        swaps = 0
        for i in range(N):
            if not visited[i]:
                cycle = []
                j = i
                while not visited[j]:
                    visited[j] = True
                    cycle.append(j)
                    j = graph[j][0] if graph[j] else -1
                    if j == -1:
                        break
                if j == -1:
                    results.append(-1)
                    break
                # Calculate the number of swaps needed for this cycle
                swaps += len(cycle) - 1
        else:
            results.append(swaps)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()