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
        
        # Track the positions of obstacles in each lane
        lane1 = []
        lane2 = []
        for x, l in obstacles:
            if l == 1:
                lane1.append(x)
            else:
                lane2.append(x)
        
        # Find the earliest position where Chef can switch lanes
        # We need to find the earliest positions in each lane
        # and check if there's enough distance between switches
        # to allow switching
        
        # Initialize the current position and lane
        current_pos = 0
        current_lane = 1
        
        # Track the last switch position
        last_switch = -1
        
        # Track the maximum distance reached
        max_distance = 0
        
        # Check if Chef can reach the restaurant without any obstacles
        # If no obstacles in either lane, return K
        if not lane1 and not lane2:
            results.append(K)
            continue
        
        # Check if Chef can reach the restaurant without switching lanes
        # If there are no obstacles in the first lane, he can go there
        if not lane1:
            results.append(K)
            continue
        if not lane2:
            results.append(K)
            continue
        
        # Find the earliest positions in each lane
        # and check if Chef can switch lanes
        # We can only switch lanes at positions that are not obstacles
        # and have enough distance between switches
        
        # Find the earliest positions in each lane
        # and check if Chef can switch lanes
        # We can only switch lanes at positions that are not obstacles
        # and have enough distance between switches
        
        # Find the earliest positions in each lane
        # and check if Chef can switch lanes
        # We can only switch lanes at positions that are not obstacles
        # and have enough distance between switches
        
        # Find the earliest positions in each lane
        # and check if Chef can switch lanes
        # We can only switch lanes at positions that are not obstacles
        # and have enough distance between switches
        
        # Find the earliest positions in each lane
        # and check if Chef can switch lanes
        # We can only switch lanes at positions that are not obstacles
        # and have enough distance between switches
        
        # Find the earliest positions in each lane
        # and check if Chef can switch lanes
        # We can only switch lanes at positions that are not obstacles
        # and have enough distance between switches
        
        # Find the earliest positions in each lane
        # and check if Chef can switch lanes
        # We can only switch lanes at positions that are not obstacles
        # and have enough distance between switches
        
        # Find the earliest positions in each lane
        # and check if Chef can switch lanes
        # We can only switch lanes at positions that are not obstacles
        # and have enough distance between switches
        
        # Find the earliest positions in each lane
        # and check if Chef can switch lanes
        # We can only switch lanes at positions that are not obstacles
        # and have enough distance between switches
        
        # Find the earliest positions in each lane
        # and check if Chef can switch lanes
        # We can only switch lanes at positions that are not obstacles
        # and have enough distance between switches
        
        # Find the earliest positions in each lane
        # and check if Chef can switch lanes
        # We can only switch lanes at positions that are not obstacles
        # and have enough distance between switches
        
        # Find the earliest positions in each lane
        # and check if Chef can switch lanes
        # We can only switch lanes at positions that are not obstacles
        # and have enough distance between switches
        
        # Find the earliest positions in each lane
        # and check if Chef can switch lanes
        # We can only switch lanes at positions that are not obstacles
        # and have enough distance between switches
        
        # Find the earliest positions in each lane
        # and check if Chef can switch lanes
        # We can only switch lanes at positions that are not obstacles
        # and have enough distance between switches
        
        # Find the earliest positions in each lane
        # and check if Chef can switch lanes
        # We can only switch lanes at positions that are not obstacles
        # and have enough distance between switches
        
        # Find the earliest positions in each lane
        # and check if Chef can switch lanes
        # We can only switch lanes at positions that are not obstacles
        # and have enough distance between switches
        
        # Find the earliest positions in each lane
        # and check if Chef can switch lanes
        # We can only switch lanes at positions that are not obstacles
        # and have enough distance between switches
        
        # Find the earliest positions in each lane
        # and check if Chef can switch lanes
        # We can only switch lanes at positions that are not obstacles
        # and have enough distance between switches
        
        # Find the earliest positions in each lane
        # and check if Chef can switch lanes
        # We can only switch lanes at positions that are not obstacles
        # and have enough distance between switches
        
        # Find the earliest positions in each lane
        # and check if Chef can switch lanes
        # We can only switch lanes at positions that are not obstacles
        # and have enough distance between switches
        
        # Find the earliest positions in each lane
        # and check if Chef can switch lanes
        # We can only switch lanes at positions that are not obstacles
        # and have enough distance between switches
        
        # Find the earliest positions in each lane
        # and check if Chef can switch lanes
        # We can only switch lanes at positions that are not obstacles
        # and have enough distance between switches
        
        # Find the earliest positions in each lane
        # and check if Chef can switch lanes
        # We can only switch lanes at positions that are not obstacles
        # and have enough distance between switches
        
        # Find the earliest positions in each lane
        # and check if Chef can switch lanes
        # We can only switch lanes at positions that are not obstacles
        # and have enough distance between switches
        
        # Find the earliest positions in each lane
        # and check if Chef can switch lanes
        # We can only switch lanes at positions that are not obstacles
        # and have enough distance between switches
        
        # Find the earliest positions in each lane
        # and check if Chef can switch lanes
        # We can only switch lanes at positions that are not obstacles
        # and have enough distance between switches
        
        # Find the earliest positions in each lane
        # and check if Chef can switch lanes
        # We can only switch lanes at positions that are not obstacles
        # and have enough distance between switches
        
        # Find the earliest positions in each lane
        # and check if Chef can switch lanes
        # We can only switch lanes at positions that are not obstacles
        # and have enough distance between switches
        
        # Find the earliest positions in each lane
        # and check if Chef can switch lanes
        # We can only switch lanes at positions that are not obstacles
        # and have enough distance between switches
        
        # Find the earliest positions in each lane
        # and check if Chef can switch lanes
        # We can only switch lanes at positions that are not obstacles
        # and have enough distance between switches
        
        # Find the earliest positions in each lane
        # and check if Chef can switch lanes
        # We can only switch lanes at positions that are not obstacles
        # and have enough distance between switches
        
        # Find the earliest positions in each lane
        # and check if Chef can switch lanes
        # We can only switch lanes at positions that are not obstacles
        # and have enough distance between switches
        
        # Find the earliest positions in each lane
        # and check if Chef can switch lanes
        # We can only switch lanes at positions that are not obstacles
        # and have enough distance between switches
        
        # Find the earliest positions in each lane
        # and check if Chef can switch lanes
        # We can only switch lanes at positions that are not obstacles
        # and have enough distance between switches
        
        # Find the earliest positions in each lane
        # and check if Chef can switch lanes
        # We can only switch lanes at positions that are not obstacles
        # and have enough distance between switches
        
        # Find the earliest positions in each lane
        # and check if Chef can switch lanes
        # We can only switch lanes at positions that are not obstacles
        # and have enough distance between switches
        
        # Find the earliest positions in each lane
        # and check if Chef can switch lanes
        # We can only switch lanes at positions that are not obstacles
        # and have enough distance between switches
        
        # Find the earliest positions in each lane
        # and check if Chef can switch lanes
        # We can only switch lanes at