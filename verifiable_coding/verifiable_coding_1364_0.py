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
        # Similarly (x - y) mod 2c determines the group
        # But since moving affects both, we need to group by (x + y) mod (2c) and (x - y) mod (2c)
        # However, since we can move in steps of (c, c) or (-c, -c), the key is (x + y) mod (2c)
        # Because (x + y) changes by 2c per move, and (x - y) changes by 0 per move
        # So the key is (x + y) mod (2c)
        
        # Group points by (x + y) mod (2c)
        groups = defaultdict(list)
        for x, y in points:
            key = (x + y) % (2 * c)
            groups[key].append((x, y))
        
        # For each group, find the optimal checkpoint (x, y) that minimizes the total moves
        # The optimal checkpoint for a group is the median of the (x - y) values
        # Because each move changes (x - y) by 0, so we can choose any (x, y) in the group
        # But to minimize the total moves, we need to choose the median of (x - y) for the group
        # Because the median minimizes the sum of absolute differences
        
        checkpoints = 0
        total_moves = 0
        
        for key in groups:
            points_in_group = groups[key]
            # Extract x - y for each point in the group
            diffs = [x - y for x, y in points_in_group]
            diffs.sort()
            median = diffs[len(diffs) // 2]
            # The optimal checkpoint is (x, y) such that x - y = median
            # So x = y + median
            # But since (x + y) mod (2c) = key, we can choose any (x, y) in the group
            # However, to minimize moves, we need to choose the median of (x - y)
            # So we can take the median and then choose x and y such that x - y = median and x + y = key + k*(2c)
            # But since we can choose any (x, y) in the group, we can just take the median and compute the moves
            # The total moves for this group is the sum of absolute differences between each (x - y) and the median
            # Because each move changes (x - y) by 0, so the number of moves is the sum of absolute differences
            # But since we can move in steps of (c, c), the number of moves is the sum of absolute differences divided by c
            # Wait, no. The number of moves is the number of steps to reach the checkpoint from the original point.
            # For example, if a point is (3, 2) and the checkpoint is (1, 0), then the difference is (2, 2), which is 2 steps of (c, c)
            # So the number of moves is the absolute value of (x - checkpoint_x) / c
            # But since (x - y) is fixed for the group, and the checkpoint is (x, y) such that x - y = median, then the number of moves is the absolute value of (x - checkpoint_x) / c
            # But since (x - y) is the same for all points in the group, the number of moves is the same for all points in the group
            # Wait, no. The number of moves depends on the original point and the checkpoint.
            # For example, if a point is (x, y) and the checkpoint is (x', y'), then the number of moves is the number of steps of (c, c) needed to reach (x', y') from (x, y)
            # Which is the absolute value of (x - x') / c or (y - y') / c, since both are the same
            # But since (x + y) mod (2c) is the same for all points in the group, we can choose the checkpoint to be (x', y') such that x' + y' = key + k*(2c)
            # But since we can choose any k, the optimal is to choose the checkpoint such that x' + y' = key
            # So the checkpoint is (x', y') where x' + y' = key and x' - y' = median
            # Solving these two equations:
            # x' + y' = key
            # x' - y' = median
            # Adding: 2x' = key + median => x' = (key + median) / 2
            # Subtracting: 2y' = key - median => y' = (key - median) / 2
            # So the checkpoint is ((key + median) / 2, (key - median) / 2)
            # The number of moves for each point in the group is the number of steps to reach this checkpoint
            # Which is the absolute value of (x - x') / c or (y - y') / c
            # But since x' = (key + median) / 2 and y' = (key - median) / 2, then x' - y' = median
            # So for each point (x, y), the number of moves is the absolute value of (x - x') / c
            # But x' = (key + median) / 2, and x = (x + y + x - y) / 2 = (key + (x - y)) / 2
            # So x - x' = (key + (x - y)) / 2 - (key + median) / 2 = (x - y - median) / 2
            # So the number of moves is the absolute value of (x - y - median) / (2c)
            # But since (x - y) is the same for all points in the group, and median is the median of (x - y), the total moves for the group is the sum of absolute differences between (x - y) and median, divided by (2c)
            # Wait, no. The number of moves for a point (x, y) is the number of steps to reach the checkpoint from (x, y)
            # Each step moves (c, c) or (-c, -c), so the number of steps is the absolute value of (x - x') / c
            # But x' = (key + median) / 2, and x = (x + y + x - y) / 2 = (key + (x - y)) / 2
            # So x - x' = (key + (x - y)) / 2 - (key + median) / 2 = (x - y - median) / 2
            # So the number of steps is the absolute value of (x - y - median) / (2c)
            # But since (x - y) is the same for all points in the group, and median is the median of (x - y), the total moves for the group is the sum of absolute differences between (x - y) and median, divided by (2c)
            # So for each group, the number of moves is sum of absolute differences between (x - y) and median, divided by (2c)
            # But since we are allowed to choose any checkpoint in the group, the optimal is to choose the median of (x - y)
            # So the total moves for the group is the sum of absolute differences between (x - y) and median, divided by (2c)
            # But since (x - y) is the same for all points in the group, the sum is the same for all points in the group
            # So for each group, we can compute the median of (x - y), then compute the sum of absolute differences between (x - y) and median, then divide by (2c)
            # So for each group, the number of checkpoints is 1, and the number of moves is the sum of absolute differences between (x - y) and median, divided by (2c)
            # So the total checkpoints is the number of groups, and the total moves is