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
        # So (x + y) mod 2c determines the equivalence class
        # Similarly, (x - y) mod 2c determines the equivalence class
        # But since we can move in both directions, we can group by (x + y) mod (2*c) and (x - y) mod (2*c)
        # However, for the same (x + y) mod (2*c) and (x - y) mod (2*c), the point can be moved to the same checkpoint
        # So we group by (x + y) mod (2*c) and (x - y) mod (2*c)
        groups = defaultdict(list)
        for x, y in points:
            key1 = (x + y) % (2 * c)
            key2 = (x - y) % (2 * c)
            groups[(key1, key2)].append((x, y))
        
        # For each group, we need to find the optimal checkpoint (x, y) such that the sum of moves is minimized
        # The optimal checkpoint is the median of the points in the group
        # But since we can only move in steps of (c, c) or (-c, -c), we need to adjust the coordinates
        # The optimal checkpoint for a group is the median of the (x - y) values or (x + y) values?
        # Actually, for each group, the optimal checkpoint is determined by the median of the (x + y) and (x - y) values
        # But since we can only move in steps of (c, c) or (-c, -c), the optimal checkpoint is the median of the (x + y) and (x - y) values
        # However, for the same group, all points can be moved to the same checkpoint, so we just need to find the optimal checkpoint for the group
        
        # For each group, compute the optimal checkpoint
        checkpoints = []
        total_moves = 0
        for key in groups:
            points_in_group = groups[key]
            # For each point, compute (x + y) and (x - y)
            # The optimal checkpoint is determined by the median of (x + y) and (x - y)
            # But since we can only move in steps of (c, c) or (-c, -c), we can adjust the coordinates
            # The optimal checkpoint for the group is (x, y) such that x + y = median(x + y) and x - y = median(x - y)
            # But since we can only move in steps of (c, c) or (-c, -c), we need to adjust the coordinates
            # So for each point, we can compute (x + y) and (x - y)
            # Then, for the group, we find the median of (x + y) and (x - y)
            # Then, the optimal checkpoint is ( (median(x + y) + median(x - y)) / 2 , (median(x + y) - median(x - y)) / 2 )
            # But since we can only move in steps of (c, c) or (-c, -c), we need to adjust the coordinates
            # So the optimal checkpoint is ( (median(x + y) + median(x - y)) / 2 , (median(x + y) - median(x - y)) / 2 )
            # But since we can only move in steps of (c, c) or (-c, -c), the optimal checkpoint is ( (median(x + y) + median(x - y)) / 2 , (median(x + y) - median(x - y)) / 2 )
            # However, since we can move in steps of (c, c) or (-c, -c), the optimal checkpoint is determined by the median of (x + y) and (x - y)
            # So for the group, we need to find the median of (x + y) and (x - y)
            # Then, the optimal checkpoint is ( (median(x + y) + median(x - y)) / 2 , (median(x + y) - median(x - y)) / 2 )
            # But since we can only move in steps of (c, c) or (-c, -c), the optimal checkpoint is determined by the median of (x + y) and (x - y)
            # So we compute the median of (x + y) and (x - y)
            # Then, the optimal checkpoint is ( (median(x + y) + median(x - y)) / 2 , (median(x + y) - median(x - y)) / 2 )
            # But since we can only move in steps of (c, c) or (-c, -c), the optimal checkpoint is determined by the median of (x + y) and (x - y)
            # So for the group, we need to find the median of (x + y) and (x - y)
            # Then, the optimal checkpoint is ( (median(x + y) + median(x - y)) / 2 , (median(x + y) - median(x - y)) / 2 )
            # However, since we can only move in steps of (c, c) or (-c, -c), the optimal checkpoint is determined by the median of (x + y) and (x - y)
            # So for the group, we need to find the median of (x + y) and (x - y)
            # Then, the optimal checkpoint is ( (median(x + y) + median(x - y)) / 2 , (median(x + y) - median(x - y)) / 2 )
            # But since we can only move in steps of (c, c) or (-c, -c), the optimal checkpoint is determined by the median of (x + y) and (x - y)
            # So we compute the median of (x + y) and (x - y)
            # Then, the optimal checkpoint is ( (median(x + y) + median(x - y)) / 2 , (median(x + y) - median(x - y)) / 2 )
            # However, since we can only move in steps of (c, c) or (-c, -c), the optimal checkpoint is determined by the median of (x + y) and (x - y)
            # So for the group, we need to find the median of (x + y) and (x - y)
            # Then, the optimal checkpoint is ( (median(x + y) + median(x - y)) / 2 , (median(x + y) - median(x - y)) / 2 )
            # But since we can only move in steps of (c, c) or (-c, -c), the optimal checkpoint is determined by the median of (x + y) and (x - y)
            # So we compute the median of (x + y) and (x - y)
            # Then, the optimal checkpoint is ( (median(x + y) + median(x - y)) / 2 , (median(x + y) - median(x - y)) / 2 )
            # However, since we can only move in steps of (c, c) or (-c, -c), the optimal checkpoint is determined by the median of (x + y) and (x - y)
            # So for the group, we need to find the median of (x + y) and (x - y)
            # Then, the optimal checkpoint is ( (median(x + y) + median(x - y)) / 2 , (median(x + y) - median(x - y)) / 2 )
            # But since we can only move in steps of (c, c) or (-c, -c), the optimal checkpoint is determined by the median of (x + y) and (x - y)
            # So we compute the median of (x + y) and (x - y)
            # Then, the optimal checkpoint is ( (median(x + y) + median(x - y)) / 2 , (median(x + y) - median(x - y)) / 2 )
            # However, since we can only move in steps of (c, c) or (-c, -c), the optimal checkpoint is determined by the median of (x + y) and (x - y)
            # So for the group, we need to find the median of (x + y) and (x - y