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
        # and edges represent allowed swaps (difference of D)
        graph = {}
        for val in P:
            graph[val] = []
        
        # Build the graph
        for val in P:
            if val + D in graph:
                graph[val].append(val + D)
                graph[val + D].append(val)
            if val - D in graph:
                graph[val].append(val - D)
                graph[val - D].append(val)
        
        # Find the number of cycles in the graph
        visited = set()
        cycles = 0
        for val in P:
            if val not in visited:
                cycle = []
                current = val
                while current not in visited:
                    visited.add(current)
                    cycle.append(current)
                    current = graph[current][0]
                cycles += 1
        
        # For each cycle, the number of swaps needed is (cycle length - 1)
        # But we need to check if the cycle is valid (i.e., the elements in the cycle are in the correct positions)
        # So we need to check if the cycle is a cycle in the sorted array
        
        # Rebuild the graph based on the sorted array
        graph_sorted = {}
        for val in sorted_P:
            graph_sorted[val] = []
        
        for val in sorted_P:
            if val + D in graph_sorted:
                graph_sorted[val].append(val + D)
                graph_sorted[val + D].append(val)
            if val - D in graph_sorted:
                graph_sorted[val].append(val - D)
                graph_sorted[val - D].append(val)
        
        # Find the number of cycles in the graph_sorted
        visited_sorted = set()
        cycles_sorted = 0
        for val in sorted_P:
            if val not in visited_sorted:
                cycle = []
                current = val
                while current not in visited_sorted:
                    visited_sorted.add(current)
                    cycle.append(current)
                    current = graph_sorted[current][0]
                cycles_sorted += 1
        
        # Now, for each cycle in the original graph, check if it is a cycle in the sorted graph
        # If it is, then the number of swaps is (cycle length - 1)
        # Otherwise, it is impossible
        
        # Create a mapping from value to its position in the sorted array
        pos_sorted = {val: i for i, val in enumerate(sorted_P)}
        
        # Create a mapping from value to its position in the original array
        pos_original = {val: i for i, val in enumerate(P)}
        
        # For each cycle in the original graph, check if it is a cycle in the sorted graph
        # If it is, then the number of swaps is (cycle length - 1)
        # Otherwise, it is impossible
        
        # Create a list of cycles in the original graph
        visited_cycle = set()
        cycles_original = []
        for val in P:
            if val not in visited_cycle:
                cycle = []
                current = val
                while current not in visited_cycle:
                    visited_cycle.add(current)
                    cycle.append(current)
                    current = graph[current][0]
                cycles_original.append(cycle)
        
        # For each cycle in the original graph, check if it is a cycle in the sorted graph
        # If it is, then the number of swaps is (cycle length - 1)
        # Otherwise, it is impossible
        
        total_swaps = 0
        for cycle in cycles_original:
            # Check if this cycle is a cycle in the sorted graph
            # Check if the elements in the cycle are in the same order as in the sorted array
            # So, for each element in the cycle, check if the next element is the next in the sorted array
            # If not, then it is not a valid cycle
            is_valid = True
            for i in range(len(cycle)):
                current = cycle[i]
                next_val = cycle[(i + 1) % len(cycle)]
                if next_val != sorted_P[pos_sorted[current] + 1] if pos_sorted[current] + 1 < N else None:
                    is_valid = False
                    break
            if not is_valid:
                results.append("-1")
                break
            total_swaps += len(cycle) - 1
        
        else:
            results.append(str(total_swaps))
    
    print("\n".join(results))