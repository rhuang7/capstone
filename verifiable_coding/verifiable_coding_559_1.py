import sys
import math

def is_sharp_turn(A, B, C):
    # Vector AB
    AB = (B[0] - A[0], B[1] - A[1])
    # Vector BC
    BC = (C[0] - B[0], C[1] - B[1])
    
    # Compute the dot product
    dot_product = AB[0] * BC[0] + AB[1] * BC[1]
    
    # Compute the magnitudes of AB and BC
    mag_AB = math.hypot(AB[0], AB[1])
    mag_BC = math.hypot(BC[0], BC[1])
    
    # Compute the cosine of the angle between AB and BC
    cos_theta = dot_product / (mag_AB * mag_BC)
    
    # Compute the angle in radians
    theta = math.acos(cos_theta)
    
    # Compute the angle DBC (the angle of the turn)
    # This is the angle between AB and BC, but measured in the other direction
    # So we take the supplementary angle
    angle_DBC = math.pi - theta
    
    # Check if the angle is greater than 45 degrees (0.7854 radians)
    return angle_DBC > math.pi / 4

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
        
        # Check if there is a sharp turn
        sharp = False
        for i in range(1, N-1):
            A = points[i-1]
            B = points[i]
            C = points[i+1]
            if is_sharp_turn(A, B, C):
                sharp = True
                break
        
        # If there is a sharp turn, check if we can fix it by changing one point
        if sharp:
            can_fix = False
            for i in range(N):
                for dx in range(-51, 51):
                    for dy in range(-51, 51):
                        if dx == 0 and dy == 0:
                            continue
                        new_point = (points[i][0] + dx, points[i][1] + dy)
                        if new_point in points or new_point[0] < 0 or new_point[0] > 50 or new_point[1] < 0 or new_point[1] > 50:
                            continue
                        # Create a new list of points with the modified point
                        new_points = points.copy()
                        new_points[i] = new_point
                        # Check if there is any sharp turn
                        sharp_fixed = False
                        for j in range(1, len(new_points)-1):
                            A = new_points[j-1]
                            B = new_points[j]
                            C = new_points[j+1]
                            if is_sharp_turn(A, B, C):
                                sharp_fixed = True
                                break
                        if not sharp_fixed:
                            can_fix = True
                            break
                    if can_fix:
                        break
                if can_fix:
                    break
        
        results.append("no" if sharp else "yes")
        results.append("yes" if can_fix else "no")
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()