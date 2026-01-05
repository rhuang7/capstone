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
        
        # Create a mapping from value to its position in the sorted array
        pos = {val: i for i, val in enumerate(sorted_P)}
        
        # Create a graph where each node is a value in the permutation
        # and edges represent allowed swaps (difference D)
        graph = [[] for _ in range(N + 1)]
        for val in P:
            if val + D <= N:
                graph[val].append(val + D)
            if val - D >= 1:
                graph[val].append(val - D)
        
        # Find cycles in the graph
        visited = [False] * (N + 1)
        cycle_count = 0
        total_swaps = 0
        
        for i in range(1, N + 1):
            if not visited[i]:
                # Start a new cycle
                cycle = []
                current = i
                while not visited[current]:
                    visited[current] = True
                    cycle.append(current)
                    current = graph[current][0]  # Assuming each node has exactly one neighbor (for simplicity)
                
                # Check if the cycle is valid (i.e., the values in the cycle form a sorted sequence)
                # and calculate the number of swaps needed
                if len(cycle) == 1:
                    continue  # No swap needed
                # Check if the cycle is a valid permutation cycle
                valid = True
                for j in range(len(cycle) - 1):
                    if abs(cycle[j] - cycle[j + 1]) != D:
                        valid = False
                        break
                if not valid:
                    results.append(-1)
                    break
                # Calculate the number of swaps needed for this cycle
                # Each cycle of length k requires (k - 1) swaps
                total_swaps += len(cycle) - 1
                cycle_count += 1
        
        if results[-1] == -1:
            pass
        else:
            results.append(total_swaps)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()