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
        distance = abs(xB - xA)
        time_walk = distance * P
        
        # Time to take the train
        # Check if Guru can take the train at time Y
        # He must be at city C at or before time Y
        # He must leave the train at city D
        # Time to reach city C by time Y
        distance_to_C = abs(xC - xA)
        time_to_C = distance_to_C * P
        if time_to_C > Y:
            time_train = float('inf')
        else:
            # Time to take the train from C to D
            distance_train = abs(xD - xC)
            time_train = distance_train * Q
            # Time to walk from D to B
            distance_from_D_to_B = abs(xB - xD)
            time_train += distance_from_D_to_B * P
        
        # Minimum time is the minimum of walking directly or taking the train
        min_time = min(time_walk, time_train)
        results.append(str(min_time))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()