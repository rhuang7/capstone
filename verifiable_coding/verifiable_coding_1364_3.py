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
        N, c = int(data[idx]), int(data[idx+1])
        idx += 2
        points = []
        for _ in range(N):
            x = int(data[idx])
            y = int(data[idx+1])
            points.append((x, y))
            idx += 2
        
        # For each point, compute (x - y) % (2*c) and (x + y) % (2*c)
        # These two values determine the equivalence class of the point
        # under the allowed moves
        key1 = []
        key2 = []
        for x, y in points:
            key1.append((x - y) % (2 * c))
            key2.append((x + y) % (2 * c))
        
        # Group points by their (key1, key2) pair
        groups = defaultdict(list)
        for i in range(N):
            groups[(key1[i], key2[i])].append(i)
        
        # Number of checkpoints is the number of groups
        num_checkpoints = len(groups)
        results.append(str(num_checkpoints))
        
        # Calculate total moves
        total_moves = 0
        for group in groups.values():
            # For each point in the group, calculate the number of moves needed
            # to reach the checkpoint (the first point in the group)
            first_x, first_y = points[group[0]]
            for i in group:
                x, y = points[i]
                # Calculate the number of moves needed to reach (first_x, first_y)
                # from (x, y)
                dx = x - first_x
                dy = y - first_y
                # Since we can move in steps of (c, c) or (-c, -c)
                # The number of moves is the absolute value of dx // c
                # or dy // c, whichever is larger
                moves = max(abs(dx // c), abs(dy // c))
                total_moves += moves
        
        results.append(str(total_moves))
    
    print('\n'.join(results))