import sys
import math

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(T):
        XE = int(data[idx])
        YE = int(data[idx+1])
        DIRE = data[idx+2]
        idx += 3
        N = int(data[idx])
        idx += 1
        asteroids = []
        for _ in range(N):
            XA = int(data[idx])
            YA = int(data[idx+1])
            DIRA = data[idx+2]
            asteroids.append((XA, YA, DIRA))
            idx += 3
        
        min_time = float('inf')
        earth_dx = 0
        earth_dy = 0
        if DIRE == 'U':
            earth_dy = 1
        elif DIRE == 'D':
            earth_dy = -1
        elif DIRE == 'R':
            earth_dx = 1
        elif DIRE == 'L':
            earth_dx = -1
        
        for (XA, YA, DIRA) in asteroids:
            ast_dx = 0
            ast_dy = 0
            if DIRA == 'U':
                ast_dy = 1
            elif DIRA == 'D':
                ast_dy = -1
            elif DIRA == 'R':
                ast_dx = 1
            elif DIRA == 'L':
                ast_dx = -1
            
            # Calculate the relative movement
            dx = earth_dx - ast_dx
            dy = earth_dy - ast_dy
            
            # Check if the paths are parallel (no collision)
            if dx == 0 and dy == 0:
                continue
            
            # Calculate the time when they meet
            # The Earth and asteroid move towards each other or away
            # The relative position is (XE - XA, YE - YA)
            # The relative velocity is (dx, dy)
            # The time is when (XE + earth_dx * t) = XA + ast_dx * t and (YE + earth_dy * t) = YA + ast_dy * t
            # Solve for t: t = (XE - XA) / dx = (YE - YA) / dy
            # Check if the time is positive and same for both equations
            # Also check if the path is intersecting
            
            # Calculate time for x-coordinate
            if dx != 0:
                t_x = (XE - XA) / dx
            else:
                t_x = float('inf')
            
            # Calculate time for y-coordinate
            if dy != 0:
                t_y = (YE - YA) / dy
            else:
                t_y = float('inf')
            
            # Check if the times are equal and positive
            if t_x == t_y and t_x > 0:
                min_time = min(min_time, t_x)
        
        if min_time != float('inf'):
            results.append(f"{min_time:.1f}")
        else:
            results.append("SAFE")
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()