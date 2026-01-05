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
        
        obstacles = []
        for x, l in zip(X, L):
            obstacles.append((x, l))
        
        # Sort obstacles by position
        obstacles.sort()
        
        # Track positions where Chef can switch lanes
        switch_points = []
        for x, l in obstacles:
            switch_points.append(x)
        
        # Sort switch points
        switch_points.sort()
        
        # Track the current lane and the last switch position
        current_lane = 1
        last_switch = -1
        max_distance = 0
        
        # Process obstacles in order
        for x, l in obstacles:
            # Check if we can switch lanes
            if last_switch != -1 and x - last_switch >= D:
                # Switch lanes
                current_lane = 2 if current_lane == 1 else 1
                last_switch = x
            # Check if current lane is blocked
            if l == current_lane:
                # Chef can't pass this obstacle
                max_distance = x
                break
        
        # If no obstacles are blocked, Chef can reach the restaurant
        if max_distance == 0:
            max_distance = K
        
        results.append(str(max_distance))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()