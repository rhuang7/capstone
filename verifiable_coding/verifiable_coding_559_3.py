import sys
import math

def is_sharp_turn(A, B, C):
    # Vector AB
    ab_x = B[0] - A[0]
    ab_y = B[1] - A[1]
    # Vector BC
    bc_x = C[0] - B[0]
    bc_y = C[1] - B[1]
    # Compute the angle between AB and BC
    # Using the dot product formula
    dot_product = ab_x * bc_x + ab_y * bc_y
    # Length of AB
    len_ab = math.hypot(ab_x, ab_y)
    # Length of BC
    len_bc = math.hypot(bc_x, bc_y)
    # Compute cosine of the angle
    cos_theta = dot_product / (len_ab * len_bc)
    # Clamp to avoid numerical issues
    cos_theta = max(min(cos_theta, 1.0), -1.0)
    # Compute the angle in radians
    theta = math.acos(cos_theta)
    # Convert to degrees
    theta_deg = math.degrees(theta)
    # Check if the angle is greater than 45 degrees
    return theta_deg > 45

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
            A = points[i-1]
            B = points[i]
            C = points[i+1]
            if is_sharp_turn(A, B, C):
                has_sharp = True
                break
        # If there is no sharp turn, output "yes yes"
        if not has_sharp:
            results.append("yes yes")
            continue
        # If there is a sharp turn, check if we can fix it by changing one point
        can_fix = False
        for i in range(N):
            # Try changing the i-th point
            for dx in range(-50, 51):
                for dy in range(-50, 51):
                    if dx == 0 and dy == 0:
                        continue
                    new_point = (points[i][0] + dx, points[i][1] + dy)
                    # Check if new_point is distinct from all other points
                    valid = True
                    for j in range(N):
                        if i == j:
                            continue
                        if new_point == points[j]:
                            valid = False
                            break
                    if not valid:
                        continue
                    # Check if the new point makes no sharp turns
                    new_points = [p for p in points]
                    new_points[i] = new_point
                    sharp = False
                    for k in range(1, N-1):
                        A = new_points[k-1]
                        B = new_points[k]
                        C = new_points[k+1]
                        if is_sharp_turn(A, B, C):
                            sharp = True
                            break
                    if not sharp:
                        can_fix = True
                        break
                if can_fix:
                    break
            if can_fix:
                break
        results.append("no" + (" yes" if can_fix else " no"))
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()