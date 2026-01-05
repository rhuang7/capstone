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
            idx += 3
            asteroids.append((XA, YA, DIRA))
        
        min_time = float('inf')
        earth_x, earth_y = XE, YE
        earth_dx, earth_dy = 0, 0
        if DIRE == 'U':
            earth_dy = 1
        elif DIRE == 'D':
            earth_dy = -1
        elif DIRE == 'R':
            earth_dx = 1
        elif DIRE == 'L':
            earth_dx = -1
        
        for xa, ya, dira in asteroids:
            ast_x, ast_y = xa, ya
            ast_dx, ast_dy = 0, 0
            if dira == 'U':
                ast_dy = 1
            elif dira == 'D':
                ast_dy = -1
            elif dira == 'R':
                ast_dx = 1
            elif dira == 'L':
                ast_dx = -1
            
            # Calculate relative motion
            dx = earth_dx - ast_dx
            dy = earth_dy - ast_dy
            
            # Check if paths are parallel
            if dx == 0 and dy == 0:
                # Same direction, no collision
                continue
            
            # Check if they are moving towards each other
            if (dx > 0 and ast_dx < 0) or (dx < 0 and ast_dx > 0):
                # Moving towards each other in x direction
                pass
            else:
                # Not moving towards each other in x direction
                continue
            
            if (dy > 0 and ast_dy < 0) or (dy < 0 and ast_dy > 0):
                # Moving towards each other in y direction
                pass
            else:
                # Not moving towards each other in y direction
                continue
            
            # Calculate time of collision
            # Earth's position at time t: (XE + earth_dx * t, YE + earth_dy * t)
            # Asteroid's position at time t: (xa + ast_dx * t, ya + ast_dy * t)
            # Set equations equal and solve for t
            # XE + earth_dx * t = xa + ast_dx * t
            # YE + earth_dy * t = ya + ast_dy * t
            # Solve for t
            # From x equation: t = (xa - XE) / (earth_dx - ast_dx)
            # From y equation: t = (ya - YE) / (earth_dy - ast_dy)
            # Both must be equal and positive
            try:
                t_x = (xa - XE) / (earth_dx - ast_dx)
                t_y = (ya - YE) / (earth_dy - ast_dy)
                if t_x == t_y and t_x >= 0:
                    min_time = min(min_time, t_x)
            except ZeroDivisionError:
                pass
        
        if min_time != float('inf'):
            results.append(f"{min_time:.1f}")
        else:
            results.append("SAFE")
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()