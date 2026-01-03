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
        
        # Try all possible colorings with 0, 1, 2
        # Since N is small (<=100), we can try all possible colorings
        # However, this is not feasible for N=100, so we need a smarter approach
        
        # Use BFS to find the minimum possible unattractiveness
        # We can try all possible colorings for the root and then propagate
        # But this is still not efficient. Instead, we can use a binary search approach
        
        # Binary search on the answer
        low = 0
        high = 2
        answer = 2
        
        while low <= high:
            mid = (low + high) // 2
            # Check if it's possible to color the tree with max difference <= mid
            # We can use BFS to try to color the tree
            # Start with root (0), try all possible colors (0, 1, 2)
            # Then for each child, try colors that differ by at most mid from parent
            # If we can color the entire tree, then mid is possible
            # Otherwise, we need to try higher
            
            # Try all possible colors for root
            possible = False
            for root_color in [0, 1, 2]:
                # BFS
                visited = [False] * N
                queue = deque()
                queue.append((0, root_color))
                visited[0] = True
                valid = True
                while queue:
                    node, color = queue.popleft()
                    for neighbor in range(N):
                        if neighbor == node:
                            continue
                        if visited[neighbor]:
                            continue
                        # Check if the color can be assigned
                        if abs(color - markers[neighbor]) > mid:
                            valid = False
                            break
                        visited[neighbor] = True
                        queue.append((neighbor, markers[neighbor]))
                    if not valid:
                        break
                if valid:
                    possible = True
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