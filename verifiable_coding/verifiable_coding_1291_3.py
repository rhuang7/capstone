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
        
        for (XA, YA, DIRA) in asteroids:
            ast_x, ast_y = XA, YA
            ast_dx, ast_dy = 0, 0
            if DIRA == 'U':
                ast_dy = 1
            elif DIRA == 'D':
                ast_dy = -1
            elif DIRA == 'R':
                ast_dx = 1
            elif DIRA == 'L':
                ast_dx = -1
            
            # Calculate relative movement
            dx = earth_dx - ast_dx
            dy = earth_dy - ast_dy
            
            # Check if they move towards each other
            if dx == 0 and dy == 0:
                # Same direction, no collision
                continue
            
            # Calculate time when they meet
            # Earth's position at time t: (XE + earth_dx * t, YE + earth_dy * t)
            # Asteroid's position at time t: (XA + ast_dx * t, YA + ast_dy * t)
            # Solve for t where XE + earth_dx * t = XA + ast_dx * t and YE + earth_dy * t = YA + ast_dy * t
            # Rearranged: t = (XA - XE) / (earth_dx - ast_dx) and t = (YA - YE) / (earth_dy - ast_dy)
            # So, need to find t that satisfies both equations
            
            # Check if they are moving towards each other in x and y directions
            # For x direction: (XE - XA) * (earth_dx - ast_dx) > 0
            # For y direction: (YE - YA) * (earth_dy - ast_dy) > 0
            # If both are true, then they are moving towards each other and will meet at some time
            # If not, then they will never meet
            
            # Calculate time for x and y directions
            try:
                t_x = (XA - XE) / (earth_dx - ast_dx)
            except ZeroDivisionError:
                t_x = float('inf')
            try:
                t_y = (YA - YE) / (earth_dy - ast_dy)
            except ZeroDivisionError:
                t_y = float('inf')
            
            # Check if they are moving towards each other in x and y directions
            if (XE - XA) * (earth_dx - ast_dx) > 0 and (YE - YA) * (earth_dy - ast_dy) > 0:
                # They are moving towards each other, so they will meet
                t = max(t_x, t_y)
                if t < min_time:
                    min_time = t
            else:
                # They are not moving towards each other, so no collision
                continue
        
        if min_time != float('inf'):
            results.append(f"{min_time:.1f}")
        else:
            results.append("SAFE")
    
    print("\n".join(results))

if __name__ == '__main__':
    solve()