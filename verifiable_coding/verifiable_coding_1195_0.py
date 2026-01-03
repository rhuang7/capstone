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
        xa = x[A]
        xb = x[B]
        xc = x[C]
        xd = x[D]
        
        # Time to walk directly from A to B
        dist_walk = abs(xb - xa)
        time_walk = dist_walk * P
        
        # Time to take the train
        # Check if Guru can take the train at time Y
        # Time to reach city C by walking
        time_to_c = abs(xc - xa) * P
        if time_to_c > Y:
            time_train = float('inf')
        else:
            # Time to take the train from C to D
            dist_train = abs(xd - xc)
            time_train = dist_train * Q
            # Time to reach D from D (0)
            # Time to walk from D to B
            time_from_d = abs(xb - xd) * P
            total_time_train = time_train + time_from_d
            time_train = total_time_train
        
        # Minimum time
        min_time = min(time_walk, time_train)
        results.append(str(min_time))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()