import sys

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
        
        # Track positions where Chef can switch lanes
        switch_points = []
        
        # Track current lane
        current_lane = 1
        
        # Track last switch position
        last_switch = -1
        
        # Process obstacles
        for x, lane in obstacles:
            # If current lane is same as obstacle lane, can't pass
            if lane == current_lane:
                # Check if we can switch before this obstacle
                if last_switch == -1 or x - last_switch >= D:
                    # Switch lanes
                    current_lane = 2 if current_lane == 1 else 1
                    last_switch = x
                else:
                    # Can't switch, so this obstacle blocks the path
                    results.append(x)
                    break
            else:
                # Can pass this obstacle, record switch point
                switch_points.append(x)
        
        else:
            # No obstacle blocked the path
            results.append(K)
        
        # Check if we can switch at the end
        if last_switch != -1 and K - last_switch >= D:
            results.append(K)
        else:
            results.append(K if len(results) == 0 else results[-1])
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()