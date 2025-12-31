import sys
import math

def is_sharp_turn(a, b, c):
    # Vector AB
    ab = (b[0] - a[0], b[1] - a[1])
    # Vector BC
    bc = (c[0] - b[0], c[1] - b[1])
    
    # Calculate the dot product
    dot_product = ab[0] * bc[0] + ab[1] * bc[1]
    
    # Calculate the magnitudes of AB and BC
    mag_ab = math.hypot(ab[0], ab[1])
    mag_bc = math.hypot(bc[0], bc[1])
    
    # Calculate the cosine of the angle between AB and BC
    cos_theta = dot_product / (mag_ab * mag_bc)
    
    # Calculate the angle in radians
    theta = math.acos(cos_theta)
    
    # Check if the angle is greater than 45 degrees (0.7854 radians)
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
        
        # Check for sharp turns
        sharp = False
        for i in range(1, N-1):
            a = points[i-1]
            b = points[i]
            c = points[i+1]
            if is_sharp_turn(a, b, c):
                sharp = True
                break
        
        # Check if it's possible to modify one point to remove sharp turns
        possible = False
        for i in range(N):
            x, y = points[i]
            for dx in range(-50, 51):
                for dy in range(-50, 51):
                    if dx == 0 and dy == 0:
                        continue
                    new_x = x + dx
                    new_y = y + dy
                    if new_x < 0 or new_x > 50 or new_y < 0 or new_y > 50:
                        continue
                    # Check if new point is unique
                    if (new_x, new_y) in points:
                        continue
                    # Create new points list
                    new_points = points.copy()
                    new_points[i] = (new_x, new_y)
                    # Check for sharp turns
                    sharp_new = False
                    for j in range(1, len(new_points)-1):
                        a = new_points[j-1]
                        b = new_points[j]
                        c = new_points[j+1]
                        if is_sharp_turn(a, b, c):
                            sharp_new = True
                            break
                    if not sharp_new:
                        possible = True
                        break
                if possible:
                    break
            if possible:
                break
        
        results.append("no" if sharp else "yes")
        results.append("yes" if possible else "no")
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()