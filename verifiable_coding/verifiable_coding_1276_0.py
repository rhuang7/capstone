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
        N, K = int(data[idx]), int(data[idx+1])
        idx += 2
        A = list(map(int, data[idx:idx+N]))
        idx += N
        
        # Function to generate all possible OR values
        def generate_or_values(arr):
            or_set = set()
            n = len(arr)
            for mask in range(1 << n):
                or_val = 0
                for i in range(n):
                    if mask & (1 << i):
                        or_val |= arr[i]
                or_set.add(or_val)
            return or_set
        
        # Function to find the minimum number of elements to insert
        def min_insertions(arr, K):
            current_set = set(arr)
            size = len(current_set)
            while True:
                if size == (1 << K):
                    return 0
                next_set = set()
                for x in current_set:
                    for y in current_set:
                        next_set.add(x | y)
                current_set = next_set
                size = len(current_set)
                if size == 0:
                    return -1  # Not possible, but per problem statement it's always possible
                
        # Initial set of elements
        initial_set = set(A)
        # Check if the initial set already satisfies the condition
        if len(initial_set) == (1 << K):
            results.append(0)
            continue
        
        # Compute the minimal insertions
        # We need to find the minimal number of elements to add such that the final set has size 2^K
        # We can use BFS to find the minimal steps
        from collections import deque
        
        target_size = 1 << K
        queue = deque()
        queue.append((initial_set, 0))
        visited = set()
        visited.add(frozenset(initial_set))
        
        while queue:
            current_set, steps = queue.popleft()
            if len(current_set) == target_size:
                results.append(steps)
                break
            # Generate next set by OR-ing all pairs
            next_set = set()
            for x in current_set:
                for y in current_set:
                    next_set.add(x | y)
            next_set_frozen = frozenset(next_set)
            if next_set_frozen not in visited:
                visited.add(next_set_frozen)
                queue.append((next_set, steps + 1))
        else:
            # If no solution found, which shouldn't happen per problem statement
            results.append(0)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()