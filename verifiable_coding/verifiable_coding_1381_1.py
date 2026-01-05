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
        
        # Track the current lane Chef is in
        current_lane = 1
        last_switch = -1
        max_distance = 0
        
        # Process obstacles in order
        for i in range(N):
            x, l = obstacles[i]
            if l == current_lane:
                # Obstacle in current lane, cannot pass
                max_distance = x
                break
            # Check if we can switch lanes
            if last_switch == -1 or x - last_switch >= D:
                # Switch lanes
                current_lane = l
                last_switch = x
        
        # If no obstacle is encountered
        if max_distance == 0:
            max_distance = K
        
        results.append(str(max_distance))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()