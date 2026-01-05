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
        N = int(data[idx])
        A = int(data[idx+1])
        B = int(data[idx+2])
        C = int(data[idx+3])
        D = int(data[idx+4])
        P = int(data[idx+5])
        Q = int(data[idx+6])
        Y = int(data[idx+7])
        idx += 8
        
        x = list(map(int, data[idx:idx+N]))
        idx += N
        
        # Convert city numbers to 0-based indices
        A -= 1
        B -= 1
        C -= 1
        D -= 1
        
        # Get positions of cities A, B, C, D
        xA = x[A]
        xB = x[B]
        xC = x[C]
        xD = x[D]
        
        # Time to walk directly from A to B
        dist_walk = abs(xB - xA)
        time_walk = dist_walk * P
        
        # Time to take the train
        # Check if the train is available at time Y
        # Time to reach city C by walking
        time_to_C = abs(xC - xA) * P
        if time_to_C > Y:
            time_train = float('inf')
        else:
            # Time to take the train from C to D
            dist_train = abs(xD - xC)
            time_train = dist_train * Q
            # Time to walk from D to B
            time_to_B = abs(xB - xD) * P
            time_train += time_to_B
        
        # Minimum time
        min_time = min(time_walk, time_train)
        results.append(str(min_time))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()