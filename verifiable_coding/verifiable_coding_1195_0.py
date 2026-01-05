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
        
        # Time to take the train
        # Check if the train is available at time Y
        # Check if A is at C and B is at D
        # Check if the train can be taken at C and left at D
        # Check if the train starts at Y and the current time is <= Y
        # Check if the train is going from C to D (xC < xD)
        if xC < xD and Y <= 0:
            dist_train = abs(xD - xC)
            time_train = dist_train * Q
            # Time to reach C and get on the train
            time_train += abs(xC - xA) * P
            # Time to get off the train and reach B
            time_train += abs(xB - xD) * P
            # Check if the train is available at time Y
            if Y <= 0:
                time_train += Y
            else:
                time_train = float('inf')
        else:
            time_train = float('inf')
        
        # Find the minimum time
        min_time = min(time_walk, time_train)
        results.append(str(min_time))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()