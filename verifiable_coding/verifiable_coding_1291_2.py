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
        
        # Earth's movement direction
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
        
        # Check each asteroid
        for (XA, YA, DIRA) in asteroids:
            # Asteroid's movement direction
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
            
            # Calculate relative movement
            rel_dx = earth_dx - ast_dx
            rel_dy = earth_dy - ast_dy
            
            # Calculate initial distance between earth and asteroid
            dx = XE - XA
            dy = YE - YA
            
            # Check if they are moving towards each other
            if rel_dx == 0 and rel_dy == 0:
                # Same direction and speed, no collision
                continue
            elif rel_dx == 0:
                # Moving along Y-axis
                if (earth_dy > 0 and ast_dy > 0) or (earth_dy < 0 and ast_dy < 0):
                    # Same direction, no collision
                    continue
                # Opposite directions
                if (earth_dy > 0 and ast_dy < 0) or (earth_dy < 0 and ast_dy > 0):
                    # Calculate time to collision
                    time = abs(dy) / (earth_dy - ast_dy)
                    if time < min_time:
                        min_time = time
            elif rel_dy == 0:
                # Moving along X-axis
                if (earth_dx > 0 and ast_dx > 0) or (earth_dx < 0 and ast_dx < 0):
                    # Same direction, no collision
                    continue
                # Opposite directions
                if (earth_dx > 0 and ast_dx < 0) or (earth_dx < 0 and ast_dx > 0):
                    # Calculate time to collision
                    time = abs(dx) / (earth_dx - ast_dx)
                    if time < min_time:
                        min_time = time
            else:
                # Moving in different directions along both axes
                # Check if they are moving towards each other
                # Calculate time to collision
                # dx = XE - XA
                # dy = YE - YA
                # rel_dx = earth_dx - ast_dx
                # rel_dy = earth_dy - ast_dy
                # Time to collision is when dx + rel_dx * t = 0 and dy + rel_dy * t = 0
                # Solve for t
                # t = dx / rel_dx = dy / rel_dy
                # Check if dx * rel_dy == dy * rel_dx
                if dx * rel_dy != dy * rel_dx:
                    continue
                t = dx / rel_dx
                if t >= 0 and (dx + rel_dx * t == 0 and dy + rel_dy * t == 0):
                    if t < min_time:
                        min_time = t
        
        if min_time != float('inf'):
            results.append(f"{min_time:.1f}")
        else:
            results.append("SAFE")
    
    print('\n'.join(results))