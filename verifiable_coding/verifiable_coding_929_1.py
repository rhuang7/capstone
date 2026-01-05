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
        
        # Try all possible color assignments and find the minimum unattractiveness
        # Since N is small (<= 100), we can use a brute-force approach with pruning
        # We'll use a recursive DFS to assign colors to nodes
        # The color can be 0, 1, or 2
        
        # Precompute the count of each marker
        count = [0] * 3
        for m in markers:
            count[m] += 1
        
        # Try all possible color assignments
        # We'll use a backtracking approach
        # We'll track the current color assignment and the current maximum difference
        # We'll also track the count of each color used
        
        def dfs(node, parent, color, used, max_diff, result):
            # If we've assigned all nodes
            if len(used) == N:
                result[0] = min(result[0], max_diff)
                return
            
            # Try all possible colors (0, 1, 2)
            for c in range(3):
                # Check if we have enough markers of this color
                if used[c] >= count[c]:
                    continue
                # Check if this color is compatible with the parent
                if parent != -1 and abs(c - color) < max_diff:
                    # Try this color
                    new_used = used[:]
                    new_used[c] += 1
                    dfs(node, -1, c, new_used, max_diff, result)
                else:
                    # Try this color
                    new_used = used[:]
                    new_used[c] += 1
                    dfs(node, -1, c, new_used, max_diff, result)
        
        # Initialize the result
        result = [float('inf')]
        # Start DFS from node 0
        used = [0] * 3
        dfs(0, -1, 0, used, float('inf'), result)
        
        results.append(result[0])
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()