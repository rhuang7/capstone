import sys

import math

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    idx = 1
    
    results = []
    
    for _ in range(T):
        finish = int(data[idx])
        distancetoBolt = int(data[idx+1])
        tigerAcceleration = int(data[idx+2])
        boltSpeed = int(data[idx+3])
        idx += 4
        
        # Distance for Bolt
        bolt_distance = finish
        
        # Time for Bolt to finish
        time_bolt = bolt_distance / boltSpeed
        
        # Distance for Tiger
        tiger_distance = distancetoBolt + finish
        
        # Solve for time when tiger reaches finish line
        # S = ut + 0.5 * a * t^2
        # tiger_distance = 0 * t + 0.5 * tigerAcceleration * t^2
        # t^2 = (2 * tiger_distance) / tigerAcceleration
        # t = sqrt(2 * tiger_distance / tigerAcceleration)
        t_tiger = math.sqrt(2 * tiger_distance / tigerAcceleration)
        
        if time_bolt < t_tiger:
            results.append("Bolt")
        else:
            results.append("Tiger")
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()