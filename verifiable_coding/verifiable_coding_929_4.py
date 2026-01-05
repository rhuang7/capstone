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
        # Since N is small (<= 100), we can try all possibilities
        # But since there are 3^100 possibilities, this is not feasible
        
        # Instead, we can use a binary search approach on the answer
        # The minimum possible unattractiveness is 0, maximum is 2
        # We can binary search on the answer and check if it's possible to color the tree with max difference <= mid
        
        def is_possible(max_diff):
            # Try to color the tree with colors 0, 1, 2 such that adjacent nodes have difference <= max_diff
            # We can use BFS to assign colors
            # Start with any node, assign it color 0, then assign colors to neighbors based on the max_diff
            # This is a greedy approach, but may not work for all cases
            # We need to try all possible colorings for the root node
            # Since the tree is connected, we can use BFS or DFS
            
            # Try all possible colors for the root node (0, 1, 2)
            for root_color in range(3):
                color = [ -1 ] * N
                color[0] = root_color
                q = deque([0])
                while q:
                    u = q.popleft()
                    for v in range(N):
                        if u != v and edges[u][0] == v or edges[u][1] == v:
                            if color[v] == -1:
                                # Try to assign a color to v that is within max_diff of u's color
                                for candidate in range(3):
                                    if abs(candidate - color[u]) <= max_diff:
                                        color[v] = candidate
                                        q.append(v)
                                        break
                # Check if all nodes are colored
                if all(c != -1 for c in color):
                    return True
            return False
        
        # Binary search for the minimum possible unattractiveness
        low = 0
        high = 2
        answer = 2
        while low <= high:
            mid = (low + high) // 2
            if is_possible(mid):
                answer = mid
                high = mid - 1
            else:
                low = mid + 1
        results.append(answer)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()