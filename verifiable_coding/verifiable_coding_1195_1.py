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
        # Check if Guru can take the train at C and arrive at D
        if xc == x[C] and xd == x[D]:
            # Time to reach C
            dist_to_c = abs(xc - xa)
            time_to_c = dist_to_c * P
            if time_to_c > Y:
                # Cannot take the train
                time_train = float('inf')
            else:
                # Time on the train
                dist_train = abs(xd - xc)
                time_train = dist_train * Q
                # Time to reach B from D
                dist_to_b = abs(xb - xd)
                time_to_b = dist_to_b * P
                time_train = time_to_c + time_train + time_to_b
        
        # Minimum time
        min_time = min(time_walk, time_train)
        results.append(str(min_time))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()