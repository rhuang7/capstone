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
        
        # Track the current lane and last switch position
        current_lane = 1
        last_switch = -1
        max_dist = 0
        
        # Track the positions of obstacles in each lane
        lane1 = []
        lane2 = []
        for x, l in obstacles:
            if l == 1:
                lane1.append(x)
            else:
                lane2.append(x)
        
        # Use binary search to find the farthest point in each lane
        def get_farthest(lane_pos):
            if not lane_pos:
                return K
            # Find the first obstacle in the lane that is after the last switch
            # or beyond K
            low = 0
            high = len(lane_pos)
            while low < high:
                mid = (low + high) // 2
                if lane_pos[mid] > last_switch + D:
                    low = mid + 1
                else:
                    high = mid
            return lane_pos[low - 1] if low - 1 >= 0 else K
        
        # Try both lanes as starting point
        # Start in lane 1
        lane1_pos = get_farthest(lane1)
        max_dist = max(max_dist, lane1_pos)
        # Start in lane 2
        lane2_pos = get_farthest(lane2)
        max_dist = max(max_dist, lane2_pos)
        
        # Try switching lanes at obstacles
        # Sort obstacles by position
        obstacles = sorted(obstacles, key=lambda x: x[0])
        
        # Try all possible switches
        for i in range(len(obstacles)):
            x, l = obstacles[i]
            # Switch to the other lane
            if l == 1:
                other_lane = lane2
            else:
                other_lane = lane1
            # Find the farthest point in the other lane after this switch
            # The switch can happen at x, but we need to ensure that we can switch
            # after D distance from the last switch
            # So the last switch must be at most x - D
            # We can use binary search to find the farthest point in the other lane
            # that is after x - D
            low = 0
            high = len(other_lane)
            while low < high:
                mid = (low + high) // 2
                if other_lane[mid] > x - D:
                    low = mid + 1
                else:
                    high = mid
            farthest = other_lane[low - 1] if low - 1 >= 0 else K
            max_dist = max(max_dist, farthest)
            # Update last switch to x
            last_switch = x
            # Update current lane
            current_lane = l
        
        results.append(str(max_dist))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()