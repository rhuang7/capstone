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
        
        # For each asteroid, calculate collision time
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
            
            # Earth's position at time t: (XE + earth_dx * t, YE + earth_dy * t)
            # Asteroid's position at time t: (XA + ast_dx * t, YA + ast_dy * t)
            
            # Find t such that Earth and asteroid are at the same position
            # XE + earth_dx * t = XA + ast_dx * t
            # YE + earth_dy * t = YA + ast_dy * t
            
            # Solve for t
            # From x-coordinate: t*(earth_dx - ast_dx) = XA - XE
            # From y-coordinate: t*(earth_dy - ast_dy) = YA - YE
            
            # Check if the lines are parallel (no solution or infinite solutions)
            # If the lines are not parallel, solve for t
            # If they are parallel, check if the lines are the same (infinite solutions)
            
            # Calculate the time for x and y coordinates
            try:
                t_x = (XA - XE) / (earth_dx - ast_dx)
                t_y = (YA - YE) / (earth_dy - ast_dy)
            except ZeroDivisionError:
                # If the direction is same in x or y, check if they are on the same line
                # If they are on the same line, check if they will meet at some time
                # If not, no collision
                continue
            
            # Check if the lines are parallel (same direction in x and y)
            if (earth_dx == ast_dx) and (earth_dy == ast_dy):
                # Same direction, check if they are on the same line
                # If they are on the same line, check if they will meet at some time
                # If not, no collision
                # Check if the initial positions are on the same line
                # If yes, check if they will meet at some time
                # If not, no collision
                # If yes, then they will meet at some time
                # So, check if the initial positions are on the same line
                # The line is defined by the direction
                # If the direction is same, then the line is same
                # So, check if the initial positions are on the same line
                # For example, if both are moving right, then the line is x-axis
                # So, check if the y-coordinates are same
                if (earth_dy == ast_dy) and (earth_dx == ast_dx):
                    # Same direction, same line
                    # Check if they are on the same line
                    # If they are on the same line, check if they will meet at some time
                    # If not, no collision
                    # If yes, then they will meet at some time
                    # Check if the initial positions are on the same line
                    # For example, if both are moving right, then the line is x-axis
                    # So, check if the y-coordinates are same
                    if (YE == YA) and (earth_dx == ast_dx):
                        # Same line, same direction
                        # Check if they are moving towards each other
                        # If yes, then they will meet at some time
                        # If not, no collision
                        # If they are moving in same direction, check if they are on the same line
                        # If yes, check if they are moving in same direction
                        # If yes, then they will never meet
                        # If no, then they will meet at some time
                        # If they are moving in same direction, then they will never meet
                        if earth_dx == ast_dx:
                            # Same direction, same line
                            # They will never meet
                            continue
                        else:
                            # Opposite directions, same line
                            # They will meet at some time
                            # The time is (XA - XE) / (earth_dx - ast_dx)
                            # But since they are on the same line, this is valid
                            t = (XA - XE) / (earth_dx - ast_dx)
                            if t >= 0:
                                min_time = min(min_time, t)
                    else:
                        # Not on same line, no collision
                        continue
                else:
                    # Not same direction, not same line
                    continue
            else:
                # Not parallel, check if t_x and t_y are equal
                if abs(t_x - t_y) < 1e-9:
                    # They meet at time t_x
                    if t_x >= 0:
                        min_time = min(min_time, t_x)
        
        if min_time != float('inf'):
            # Round to 1 decimal place
            results.append(f"{min_time:.1f}")
        else:
            results.append("SAFE")
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()