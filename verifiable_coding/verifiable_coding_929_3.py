import sys
import math
from collections import deque

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
        edges = []
        for _ in range(N-1):
            u = int(data[idx])
            v = int(data[idx+1])
            edges.append((u-1, v-1))
            idx += 2
        
        # Try all possible assignments of markers to nodes
        # Since N is small (<= 100), we can use backtracking
        # However, for efficiency, we can use a better approach
        
        # Since the answer is the minimum possible maximum difference, we can use binary search on the answer
        # We can try all possible values of answer from 0 to 2 (since markers are 0, 1, 2)
        # For each possible answer, check if it's possible to color the tree with that maximum difference
        
        # Try all possible values of answer from 0 to 2
        for ans in range(3):
            # Try to assign markers to nodes such that adjacent nodes have difference <= ans
            # We can use BFS to assign colors
            # We can try all possible starting colors (0, 1, 2)
            # For each starting color, try to assign colors to the tree
            # If any of them works, then ans is possible
            # If any of them works, then ans is the minimum possible
            # So we can break early
            
            # Try all possible starting colors
            for start in range(3):
                # Use BFS to assign colors
                # We need to check if it's possible to assign colors such that adjacent nodes have difference <= ans
                # We can use a BFS approach where we assign colors to nodes
                # We can use a queue to process nodes
                # We can use a color array to store the color of each node
                color = [-1] * N
                color[0] = start
                queue = deque([0])
                valid = True
                while queue:
                    u = queue.popleft()
                    for v in edges:
                        if v[0] == u:
                            if color[v[1]] == -1:
                                # Try to assign a color to v
                                # The color of v must be in [color[u] - ans, color[u] + ans]
                                # But since markers are 0, 1, 2, we can only choose from 0, 1, 2
                                # So we can try all possible colors in that range
                                for c in range(3):
                                    if abs(c - color[u]) <= ans:
                                        color[v[1]] = c
                                        queue.append(v[1])
                                        break
                                else:
                                    valid = False
                                    break
                        elif v[1] == u:
                            if color[v[0]] == -1:
                                # Try to assign a color to v
                                # The color of v must be in [color[u] - ans, color[u] + ans]
                                # But since markers are 0, 1, 2, we can only choose from 0, 1, 2
                                # So we can try all possible colors in that range
                                for c in range(3):
                                    if abs(c - color[u]) <= ans:
                                        color[v[0]] = c
                                        queue.append(v[0])
                                        break
                                else:
                                    valid = False
                                    break
                    if not valid:
                        break
                if valid:
                    # Check if all markers are used
                    # Since we have N markers, and we are using 0, 1, 2, we need to check if the count of each color is <= the count of markers
                    # But since the problem allows any assignment, we just need to check if the colors are valid
                    # So we can break and return ans as the answer
                    results.append(ans)
                    break
            else:
                # None of the starting colors worked, try the next ans
                continue
            break
        else:
            # None of the ans values worked, which is impossible since markers are 0, 1, 2
            results.append(2)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()