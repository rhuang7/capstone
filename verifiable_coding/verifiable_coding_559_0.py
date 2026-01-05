import sys
import math

def is_sharp_turn(a, b, c):
    # Compute vectors BA and BC
    ba = (a[0] - b[0], a[1] - b[1])
    bc = (c[0] - b[0], c[1] - b[1])
    
    # Compute the dot product and magnitudes
    dot = ba[0] * bc[0] + ba[1] * bc[1]
    mag_ba = math.hypot(ba[0], ba[1])
    mag_bc = math.hypot(bc[0], bc[1])
    
    # Compute the cosine of the angle between BA and BC
    cos_theta = dot / (mag_ba * mag_bc)
    
    # Compute the angle in radians and convert to degrees
    angle = math.degrees(math.acos(cos_theta))
    
    # Check if the angle is greater than 45 degrees
    return angle > 45

def solve():
    import sys
    input = sys.stdin.buffer.read().split()
    idx = 0
    T = int(input[idx])
    idx += 1
    results = []
    
    for _ in range(T):
        N = int(input[idx])
        idx += 1
        points = []
        for _ in range(N):
            x = int(input[idx])
            y = int(input[idx+1])
            points.append((x, y))
            idx += 2
        
        # Check if there is any sharp turn
        has_sharp = False
        for i in range(1, N-1):
            a = points[i-1]
            b = points[i]
            c = points[i+1]
            if is_sharp_turn(a, b, c):
                has_sharp = True
                break
        
        # If there is no sharp turn, output "yes yes"
        if not has_sharp:
            results.append("yes yes")
            continue
        
        # If there is a sharp turn, check if we can modify one point to remove it
        can_modify = False
        for i in range(N):
            x, y = points[i]
            for dx in range(-51, 51):
                for dy in range(-51, 51):
                    if dx == 0 and dy == 0:
                        continue
                    new_x = x + dx
                    new_y = y + dy
                    if new_x < 0 or new_x > 50 or new_y < 0 or new_y > 50:
                        continue
                    # Check if the new point is already in the list
                    if (new_x, new_y) in points:
                        continue
                    # Create a new list with the modified point
                    new_points = points.copy()
                    new_points[i] = (new_x, new_y)
                    # Check if there is any sharp turn in the new list
                    sharp = False
                    for j in range(1, len(new_points)-1):
                        a = new_points[j-1]
                        b = new_points[j]
                        c = new_points[j+1]
                        if is_sharp_turn(a, b, c):
                            sharp = True
                            break
                    if not sharp:
                        can_modify = True
                        break
                if can_modify:
                    break
            if can_modify:
                break
        
        results.append("no" + (" yes" if can_modify else " no"))
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()