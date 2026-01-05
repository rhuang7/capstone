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
        
        # Earth's movement direction
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
            # Asteroid's movement direction
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
            rel_dx = earth_dx - ast_dx
            rel_dy = earth_dy - ast_dy
            
            # Calculate initial distance between earth and asteroid
            dx = XE - XA
            dy = YE - YA
            
            # Check if they are moving towards each other
            if rel_dx == 0 and rel_dy == 0:
                # Same direction and same speed, no collision
                continue
            
            # Check if they are moving away from each other
            if rel_dx == 0 and rel_dy < 0:
                # Moving away, no collision
                continue
            
            if rel_dy == 0 and rel_dx < 0:
                # Moving away, no collision
                continue
            
            # Calculate time of collision
            # The relative movement must bring them to the same position
            # Solve for t in: dx + rel_dx * t = 0 and dy + rel_dy * t = 0
            # Since they move in straight lines, we need to find t where both equations are satisfied
            # But since they are moving in straight lines, we can find t for one equation and check if it satisfies the other
            
            # Solve for t from x-coordinate
            if rel_dx != 0:
                t_x = dx / rel_dx
            else:
                t_x = float('inf')
            
            # Solve for t from y-coordinate
            if rel_dy != 0:
                t_y = dy / rel_dy
            else:
                t_y = float('inf')
            
            # Find the time when both equations are satisfied
            # Since they are moving in straight lines, the collision time is the same for both
            # So we need to find t that satisfies both equations
            # But since they are moving in straight lines, we can find t for one equation and check if it satisfies the other
            
            # Check if t_x and t_y are valid
            if t_x == float('inf') or t_y == float('inf'):
                continue
            
            # Check if t_x and t_y are the same
            if abs(t_x - t_y) < 1e-9:
                min_time = min(min_time, t_x)
        
        if min_time != float('inf'):
            results.append(f"{min_time:.1f}")
        else:
            results.append("SAFE")
    
    print("\n".join(results))

if __name__ == '__main__':
    solve()