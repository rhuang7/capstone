import sys
import bisect

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(T):
        N = int(data[idx])
        K = int(data[idx+1])
        D = int(data[idx+2])
        idx += 3
        X = list(map(int, data[idx:idx+N]))
        idx += N
        L = list(map(int, data[idx:idx+N]))
        idx += N
        
        # Sort obstacles by position
        obstacles = sorted(zip(X, L))
        
        # Separate obstacles by lane
        lane1 = []
        lane2 = []
        for x, l in obstacles:
            if l == 1:
                lane1.append(x)
            else:
                lane2.append(x)
        
        # Sort obstacles in each lane
        lane1.sort()
        lane2.sort()
        
        # Precompute positions for each lane
        pos1 = lane1
        pos2 = lane2
        
        # Find the maximum distance Chef can travel
        max_dist = 0
        current_lane = 1
        last_switch = -D - 1
        
        # Try starting in lane 1
        if len(pos1) == 0:
            results.append(K)
            continue
        i = 0
        last_pos = 0
        while i < len(pos1):
            if pos1[i] > last_pos + D:
                last_pos = pos1[i]
                i += 1
            else:
                break
        max_dist = max(max_dist, last_pos)
        last_switch = last_pos
        current_lane = 1
        
        # Try starting in lane 2
        if len(pos2) == 0:
            results.append(K)
            continue
        i = 0
        last_pos = 0
        while i < len(pos2):
            if pos2[i] > last_pos + D:
                last_pos = pos2[i]
                i += 1
            else:
                break
        max_dist = max(max_dist, last_pos)
        last_switch = last_pos
        current_lane = 2
        
        # Try switching lanes
        # Find the earliest positions in both lanes
        pos1_idx = 0
        pos2_idx = 0
        while pos1_idx < len(pos1) and pos2_idx < len(pos2):
            if pos1[pos1_idx] < pos2[pos2_idx]:
                if pos1[pos1_idx] > last_switch + D:
                    last_switch = pos1[pos1_idx]
                    max_dist = max(max_dist, last_switch)
                    pos1_idx += 1
                else:
                    break
            else:
                if pos2[pos2_idx] > last_switch + D:
                    last_switch = pos2[pos2_idx]
                    max_dist = max(max_dist, last_switch)
                    pos2_idx += 1
                else:
                    break
        
        # Check if we can reach the end
        if max_dist < K:
            results.append(max_dist)
        else:
            results.append(K)
    
    for res in results:
        print(res)