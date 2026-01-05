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
        
        # Track the current lane and last switch position
        current_lane = 1
        last_switch = -1
        max_distance = 0
        
        # Process obstacles
        for x, l in obstacles:
            # Check if we can switch lanes
            if current_lane != l:
                if last_switch == -1 or x - last_switch >= D:
                    # Switch lanes
                    current_lane = l
                    last_switch = x
            # Update max distance
            max_distance = max(max_distance, x)
        
        # Check if we can reach the restaurant
        if max_distance < K:
            # Try to switch lanes at the end
            if last_switch == -1 or K - last_switch >= D:
                max_distance = K
        else:
            max_distance = K
        
        results.append(str(max_distance))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()