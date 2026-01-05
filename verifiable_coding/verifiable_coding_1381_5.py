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
        N, K, D = map(int, data[idx:idx+3])
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
        
        # Sort lanes by position
        lane1.sort()
        lane2.sort()
        
        # Find the maximum distance Chef can travel
        max_dist = 0
        current_lane = 1
        last_switch = -float('inf')
        last_pos = 0
        
        # Try starting in lane 1
        pos = 0
        last_switch = -float('inf')
        current_lane = 1
        for x in lane1:
            if x > last_pos:
                if last_switch != -float('inf') and x - last_pos < D:
                    continue
                last_switch = x
                last_pos = x
                current_lane = 2
            else:
                break
        if last_pos < K:
            max_dist = max(max_dist, K)
        
        # Try starting in lane 2
        pos = 0
        last_switch = -float('inf')
        current_lane = 2
        for x in lane2:
            if x > last_pos:
                if last_switch != -float('inf') and x - last_pos < D:
                    continue
                last_switch = x
                last_pos = x
                current_lane = 1
            else:
                break
        if last_pos < K:
            max_dist = max(max_dist, K)
        
        # Try switching lanes at obstacles
        # Try starting in lane 1
        pos = 0
        last_switch = -float('inf')
        current_lane = 1
        for x in lane1:
            if x > last_pos:
                if last_switch != -float('inf') and x - last_pos < D:
                    continue
                last_switch = x
                last_pos = x
                current_lane = 2
            else:
                break
        if last_pos < K:
            max_dist = max(max_dist, K)
        
        # Try starting in lane 2
        pos = 0
        last_switch = -float('inf')
        current_lane = 2
        for x in lane2:
            if x > last_pos:
                if last_switch != -float('inf') and x - last_pos < D:
                    continue
                last_switch = x
                last_pos = x
                current_lane = 1
            else:
                break
        if last_pos < K:
            max_dist = max(max_dist, K)
        
        results.append(str(max_dist))
    
    print('\n'.join(results))