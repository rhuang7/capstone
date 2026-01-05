import sys
import collections

def solve():
    import sys
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
        # So (x + y) mod 2c is invariant
        # Similarly, (x - y) mod 2c is invariant
        # So group by these two values
        groups = collections.defaultdict(list)
        for x, y in points:
            key1 = (x + y) % (2 * c)
            key2 = (x - y) % (2 * c)
            groups[(key1, key2)].append((x, y))
        
        # For each group, calculate the number of operations needed to move all points to the same checkpoint
        # The optimal checkpoint is the one that minimizes the total operations
        # For each group, we can choose any point as the target, and calculate the total operations
        # The minimal total operations for a group is the sum of the distances from each point to the median (in terms of (x + y) and (x - y))
        # However, since we can only move in steps of (c, c) or (-c, -c), the actual number of operations is the sum of the absolute differences divided by (2c)
        # But since we can choose any target, the optimal is to choose the median of (x + y) and (x - y)
        # So for each group, we can calculate the minimal operations
        
        checkpoints = 0
        total_ops = 0
        
        for group in groups.values():
            # Extract (x + y) and (x - y) for all points in the group
            s = [x + y for x, y in group]
            d = [x - y for x, y in group]
            
            # Sort and find median
            s.sort()
            d.sort()
            
            # The optimal checkpoint is the median of s and d
            # The number of operations is the sum of absolute differences from the median divided by (2c)
            # But since we can move in steps of (c, c) or (-c, -c), the number of operations is the sum of absolute differences divided by (2c)
            # However, since we can choose any target, the minimal total operations is the sum of absolute differences from the median
            
            # For s
            median_s = s[len(s) // 2]
            ops_s = sum(abs(s_i - median_s) for s_i in s)
            
            # For d
            median_d = d[len(d) // 2]
            ops_d = sum(abs(d_i - median_d) for d_i in d)
            
            # The total operations is the sum of the operations for s and d
            total_ops += ops_s + ops_d
            
            # Increment checkpoints
            checkpoints += 1
        
        results.append(f"{checkpoints} {total_ops}")
    
    print("\n".join(results))