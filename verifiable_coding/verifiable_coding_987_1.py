import sys

import math

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    
    results = []
    
    for _ in range(T):
        finish = int(data[index])
        distancetoBolt = int(data[index+1])
        tigerAcceleration = int(data[index+2])
        boltSpeed = int(data[index+3])
        index += 4
        
        # Distance Bolt needs to run
        bolt_distance = finish
        
        # Time for Bolt to reach finish
        time_bolt = bolt_distance / boltSpeed
        
        # Distance Tiger needs to run
        tiger_distance = distancetoBolt + finish
        
        # Solve for time when Tiger reaches finish
        # tiger_distance = 0.5 * tigerAcceleration * t^2
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