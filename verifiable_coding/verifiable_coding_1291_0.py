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
        
        earth_x, earth_y = XE, YE
        earth_dir = DIRE
        
        min_time = float('inf')
        
        # Determine Earth's movement
        if earth_dir == 'U':
            earth_dy = 1
            earth_dx = 0
        elif earth_dir == 'D':
            earth_dy = -1
            earth_dx = 0
        elif earth_dir == 'R':
            earth_dx = 1
            earth_dy = 0
        elif earth_dir == 'L':
            earth_dx = -1
            earth_dy = 0
        
        # Process each asteroid
        for (XA, YA, DIRA) in asteroids:
            # Determine asteroid's movement
            if DIRA == 'U':
                ast_dy = 1
                ast_dx = 0
            elif DIRA == 'D':
                ast_dy = -1
                ast_dx = 0
            elif DIRA == 'R':
                ast_dx = 1
                ast_dy = 0
            elif DIRA == 'L':
                ast_dx = -1
                ast_dy = 0
            
            # Calculate relative positions
            dx = XA - earth_x
            dy = YA - earth_y
            
            # Check if collision is possible
            if (dx == 0 and dy == 0):
                continue  # Not possible as per problem statement
            
            # Determine if paths intersect
            # Earth's position at time t: (earth_x + earth_dx * t, earth_y + earth_dy * t)
            # Asteroid's position at time t: (XA + ast_dx * t, YA + ast_dy * t)
            
            # Solve for t where earth_x + earth_dx * t = XA + ast_dx * t and earth_y + earth_dy * t = YA + ast_dy * t
            # This is a system of linear equations
            # Solve for t
            
            # Check if paths are parallel
            if earth_dx == ast_dx and earth_dy == ast_dy:
                # Same direction, no collision
                continue
            
            # Check if paths are perpendicular
            if earth_dx * ast_dx + earth_dy * ast_dy == 0:
                # Perpendicular, no collision
                continue
            
            # Solve for t
            # From x-coordinate: earth_x + earth_dx * t = XA + ast_dx * t => t = (XA - earth_x) / (earth_dx - ast_dx)
            # From y-coordinate: earth_y + earth_dy * t = YA + ast_dy * t => t = (YA - earth_y) / (earth_dy - ast_dy)
            # These two t's must be equal
            
            # Calculate t from x-coordinate
            t1 = (XA - earth_x) / (earth_dx - ast_dx)
            # Calculate t from y-coordinate
            t2 = (YA - earth_y) / (earth_dy - ast_dy)
            
            # Check if t1 and t2 are equal
            if abs(t1 - t2) < 1e-9:
                # Collision possible at time t1
                t = t1
                # Check if t is non-negative and if the positions are the same
                if t >= 0:
                    # Check if positions are the same
                    earth_x_t = earth_x + earth_dx * t
                    earth_y_t = earth_y + earth_dy * t
                    ast_x_t = XA + ast_dx * t
                    ast_y_t = YA + ast_dy * t
                    if abs(earth_x_t - ast_x_t) < 1e-9 and abs(earth_y_t - ast_y_t) < 1e-9:
                        min_time = min(min_time, t)
        
        if min_time != float('inf'):
            results.append(f"{min_time:.1f}")
        else:
            results.append("SAFE")
    
    print("\n".join(results))

if __name__ == '__main__':
    solve()