import sys
import math

def is_sharp_turn(a, b, c):
    # Vector AB
    ab = (b[0] - a[0], b[1] - a[1])
    # Vector BC
    bc = (c[0] - b[0], c[1] - b[1])
    
    # Compute the dot product
    dot_product = ab[0] * bc[0] + ab[1] * bc[1]
    
    # Compute the magnitudes of AB and BC
    mag_ab = math.hypot(ab[0], ab[1])
    mag_bc = math.hypot(bc[0], bc[1])
    
    # Compute the cosine of the angle between AB and BC
    cos_theta = dot_product / (mag_ab * mag_bc)
    
    # Compute the angle in radians
    theta = math.acos(cos_theta)
    
    # Compute the angle DBC (angle between BA and BC)
    # Since BA is the reverse of AB, the angle DBC is the same as the angle between AB and BC
    # But we need to check if the turn is sharp, which is when the angle is greater than 45 degrees
    return theta > math.radians(45)

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
        
        # If there is a sharp turn, check if it can be fixed by changing one point
        can_fix = False
        for i in range(N):
            x, y = points[i]
            # Try changing x coordinate
            for new_x in range(0, 51):
                if new_x == x:
                    continue
                new_point = (new_x, y)
                points_new = points.copy()
                points_new[i] = new_point
                has_sharp_new = False
                for j in range(1, N-1):
                    a = points_new[j-1]
                    b = points_new[j]
                    c = points_new[j+1]
                    if is_sharp_turn(a, b, c):
                        has_sharp_new = True
                        break
                if not has_sharp_new:
                    can_fix = True
                    break
            if can_fix:
                break
            # Try changing y coordinate
            for new_y in range(0, 51):
                if new_y == y:
                    continue
                new_point = (x, new_y)
                points_new = points.copy()
                points_new[i] = new_point
                has_sharp_new = False
                for j in range(1, N-1):
                    a = points_new[j-1]
                    b = points_new[j]
                    c = points_new[j+1]
                    if is_sharp_turn(a, b, c):
                        has_sharp_new = True
                        break
                if not has_sharp_new:
                    can_fix = True
                    break
            if can_fix:
                break
        
        results.append("no" + (" yes" if can_fix else " no"))
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()