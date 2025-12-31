import sys
import math
from collections import defaultdict, deque

def main():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(T):
        n = int(data[idx])
        m = int(data[idx+1])
        idx += 2
        edges = []
        for i in range(m):
            u = int(data[idx]) - 1
            v = int(data[idx+1]) - 1
            edges.append((u, v))
            idx += 2
        
        # Try to find a matching of size n
        # Use a greedy approach to find a matching
        match = []
        used = [False] * (3 * n)
        for i in range(m):
            u, v = edges[i]
            if not used[u] and not used[v]:
                match.append(i + 1)
                used[u] = True
                used[v] = True
                if len(match) == n:
                    results.append("Matching")
                    results.append(' '.join(map(str, match)))
                    break
        else:
            # No matching found, try to find an independent set of size n
            # Use a greedy approach to find an independent set
            # Select vertices with the least degree
            degree = [0] * (3 * n)
            for u, v in edges:
                degree[u] += 1
                degree[v] += 1
            # Sort vertices by degree
            vertices = sorted(range(3 * n), key=lambda x: degree[x])
            ind_set = []
            for v in vertices:
                if len(ind_set) == n:
                    break
                # Check if v is not connected to any in ind_set
                valid = True
                for u in ind_set:
                    if (u, v) in edges or (v, u) in edges:
                        valid = False
                        break
                if valid:
                    ind_set.append(v)
            if len(ind_set) == n:
                results.append("IndSet")
                results.append(' '.join(map(str, [x + 1 for x in ind_set])))
            else:
                results.append("Impossible")
    
    print('\n'.join(results))

if __name__ == '__main__':
    main()