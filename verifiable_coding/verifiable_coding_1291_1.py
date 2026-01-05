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
        if DIRE == 'R':
            earth_dx = 1
        elif DIRE == 'L':
            earth_dx = -1
        elif DIRE == 'U':
            earth_dy = 1
        elif DIRE == 'D':
            earth_dy = -1
        
        # Check each asteroid
        for (XA, YA, DIRA) in asteroids:
            # Asteroid's movement direction
            ast_dx = 0
            ast_dy = 0
            if DIRA == 'R':
                ast_dx = 1
            elif DIRA == 'L':
                ast_dx = -1
            elif DIRA == 'U':
                ast_dy = 1
            elif DIRA == 'D':
                ast_dy = -1
            
            # Calculate relative movement
            rel_dx = earth_dx - ast_dx
            rel_dy = earth_dy - ast_dy
            
            # Calculate initial distance
            dx = XE - XA
            dy = YE - YA
            
            # Check if they are moving towards each other
            if rel_dx == 0 and rel_dy == 0:
                # Same direction, no collision
                continue
            
            # Check if they are moving away from each other
            if rel_dx * dx >= 0 and rel_dy * dy >= 0:
                # Moving away, no collision
                continue
            
            # Calculate time of collision
            # Time = distance / relative speed
            # Distance is the absolute value of dx and dy
            # But since they are moving towards each other, we can calculate the time
            # based on the relative movement
            # The collision occurs when the distance between them is zero
            # So, solve for t: dx + rel_dx * t = 0 and dy + rel_dy * t = 0
            # But since they are moving in different directions, we need to find t where
            # (XE + earth_dx * t) = (XA + ast_dx * t) and (YE + earth_dy * t) = (YA + ast_dy * t)
            # Which simplifies to t = (XE - XA) / rel_dx and t = (YE - YA) / rel_dy
            # So, we need to find t where both equations are satisfied
            # So, t must be the same for both equations
            # So, t = (XE - XA) / rel_dx = (YE - YA) / rel_dy
            # So, check if (XE - XA) * rel_dy == (YE - YA) * rel_dx
            # If not, then they will not collide
            # If yes, then t is (XE - XA) / rel_dx
            # But need to check if t is positive
            # Also, need to check if the direction is such that they are moving towards each other
            
            # Check if the relative movement is such that they are moving towards each other
            if (rel_dx * dx) < 0 and (rel_dy * dy) < 0:
                # Moving towards each other
                t1 = (XE - XA) / rel_dx
                t2 = (YE - YA) / rel_dy
                if t1 == t2:
                    min_time = min(min_time, t1)
        
        if min_time != float('inf'):
            results.append(f"{min_time:.1f}")
        else:
            results.append("SAFE")
    
    print("\n".join(results))

if __name__ == '__main__':
    solve()