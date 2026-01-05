import sys
import math
from collections import defaultdict

def solve():
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
        tree = defaultdict(list)
        for _ in range(N-1):
            u = int(data[idx]) - 1
            v = int(data[idx+1]) - 1
            tree[u].append(v)
            tree[v].append(u)
            idx += 2
        
        # Try all possible color combinations
        # Since markers can be 0, 1, 2, we can try all possible colorings
        # But since N can be up to 100, brute force is not feasible
        # Instead, we can use a binary search approach on the possible answer
        
        # Binary search on the answer
        low = 0
        high = 2
        answer = 2
        
        while low <= high:
            mid = (low + high) // 2
            # Try to color the tree with colors 0, 1, 2 such that adjacent nodes differ by at most mid
            # We can do this with BFS
            color = [-1] * N
            possible = True
            for start in range(N):
                if color[start] == -1:
                    queue = [start]
                    color[start] = 0
                    while queue:
                        node = queue.pop(0)
                        for neighbor in tree[node]:
                            if color[neighbor] == -1:
                                color[neighbor] = 1 - color[node]
                                queue.append(neighbor)
                            elif color[neighbor] == color[node]:
                                possible = False
                                break
                        if not possible:
                            break
                    if not possible:
                        break
            if possible:
                answer = mid
                high = mid - 1
            else:
                low = mid + 1
        
        results.append(str(answer))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()