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
        
        # Group points by (x - y) % (2*c) and (x + y) % (2*c)
        # Since moving by (c, c) or (-c, -c) changes (x + y) by 2c or -2c
        # So (x + y) mod 2c determines the group
        # Similarly, (x - y) mod 2c determines the group
        # But we need to group by (x + y) mod (2c) and (x - y) mod (2c)
        # However, since we can move points in steps of (c, c) or (-c, -c), the key is (x + y) mod (2c)
        # Because each move changes (x + y) by 2c or -2c
        # So all points in the same (x + y) mod (2c) group can be moved to the same checkpoint
        # But we also need to consider (x - y) mod (2c) to determine the position within the group
        
        # For each point, compute (x + y) mod (2c) and (x - y) mod (2c)
        # Then group points by these two values
        groups = defaultdict(list)
        for x, y in points:
            key1 = (x + y) % (2 * c)
            key2 = (x - y) % (2 * c)
            groups[(key1, key2)].append((x, y))
        
        # For each group, compute the minimal number of operations to move all points to a common checkpoint
        # The minimal number of operations is the sum of the distances from each point to the median of the group
        # But since we can only move in steps of (c, c) or (-c, -c), the checkpoints must be at positions (x + k*c, y + k*c)
        # So the minimal number of operations is the sum of |x_i - x_j| / c for each point in the group
        
        total_checkpoints = 0
        total_operations = 0
        
        for group in groups.values():
            # Extract x and y coordinates
            xs = [x for x, y in group]
            ys = [y for x, y in group]
            
            # Find the median of xs and ys
            xs.sort()
            ys.sort()
            median_x = xs[len(xs) // 2]
            median_y = ys[len(ys) // 2]
            
            # Calculate the number of checkpoints for this group
            # Since all points can be moved to the same checkpoint, we need only one checkpoint per group
            total_checkpoints += 1
            
            # Calculate the number of operations
            ops = 0
            for x, y in group:
                dx = abs(x - median_x)
                dy = abs(y - median_y)
                ops += dx + dy
            total_operations += ops
        
        results.append(f"{total_checkpoints} {total_operations}")
    
    for res in results:
        print(res)