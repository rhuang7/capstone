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
        N, A, B, C, D, P, Q, Y = map(int, data[idx:idx+8])
        idx += 8
        x = list(map(int, data[idx:idx+N]))
        idx += N
        
        A -= 1
        B -= 1
        C -= 1
        D -= 1
        
        # Get coordinates of cities A, B, C, D
        xA = x[A]
        xB = x[B]
        xC = x[C]
        xD = x[D]
        
        # Time to walk directly from A to B
        dist_walk = abs(xB - xA)
        time_walk = dist_walk * P
        
        # Time to take train
        # Check if train is available at time Y
        # Time to reach C by walking
        dist_walk_to_C = abs(xC - xA)
        time_walk_to_C = dist_walk_to_C * P
        if time_walk_to_C > Y:
            time_train = float('inf')
        else:
            # Time to take train from C to D
            dist_train = abs(xD - xC)
            time_train = dist_train * Q
            # Time to walk from D to B
            dist_walk_from_D = abs(xB - xD)
            time_walk_from_D = dist_walk_from_D * P
            time_train += time_walk_from_D
        
        # Minimum time
        min_time = min(time_walk, time_train)
        results.append(str(min_time))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()