import sys
import math
from collections import defaultdict

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(T):
        N = int(data[idx])
        idx += 1
        markers = list(map(int, data[idx:idx+N]))
        idx += N
        edges = []
        for _ in range(N-1):
            u = int(data[idx])
            v = int(data[idx+1])
            edges.append((u-1, v-1))
            idx += 2
        
        # Try all possible color assignments and find the minimum unattractiveness
        # Since N is small (<= 100), we can try all possible colorings
        # However, trying all colorings directly is not feasible, so we use a binary search approach
        
        # Binary search on the answer
        low = 0
        high = 2
        answer = 2
        
        while low <= high:
            mid = (low + high) // 2
            # Check if it's possible to color the tree with max difference <= mid
            # We use BFS to try to color the tree
            color = [-1] * N
            possible = True
            # Try all possible starting colors (0, 1, 2)
            for start in range(3):
                color[0] = start
                queue = [0]
                visited = set([0])
                while queue:
                    u = queue.pop(0)
                    for v in edges:
                        if v[0] == u:
                            if color[v[1]] == -1:
                                color[v[1]] = color[u] ^ 1
                                if abs(color[v[1]] - color[u]) > mid:
                                    possible = False
                                    break
                                queue.append(v[1])
                                visited.add(v[1])
                            else:
                                if abs(color[v[1]] - color[u]) > mid:
                                    possible = False
                                    break
                    if not possible:
                        break
                if possible:
                    answer = mid
                    break
            if possible:
                high = mid - 1
            else:
                low = mid + 1
        
        results.append(str(answer))
    
    print('\n'.join(results))