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
        tiger_distance = finish + distancetoBolt
        
        # Solve for time when tiger reaches finish line
        # S = ut + 0.5 * a * t^2
        # tiger_distance = 0 * t + 0.5 * tigerAcceleration * t^2
        # t^2 * tigerAcceleration / 2 = tiger_distance
        # t^2 = (2 * tiger_distance) / tigerAcceleration
        # t = sqrt( (2 * tiger_distance) / tigerAcceleration )
        
        # Check if tiger can reach finish line in time_bolt
        # If tiger's time is <= time_bolt, Tiger wins
        # Else, Bolt wins
        
        try:
            time_tiger = math.sqrt( (2 * tiger_distance) / tigerAcceleration )
        except:
            # If acceleration is 0, tiger never moves
            time_tiger = float('inf')
        
        if time_tiger <= time_bolt:
            results.append("Tiger")
        else:
            results.append("Bolt")
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()