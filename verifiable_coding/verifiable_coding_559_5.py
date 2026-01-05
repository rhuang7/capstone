import sys
import math

def is_sharp_turn(A, B, C):
    # Vectors AB and BC
    AB = (B[0] - A[0], B[1] - A[1])
    BC = (C[0] - B[0], C[1] - B[1])
    
    # Compute the angle between AB and BC using the dot product
    dot_product = AB[0] * BC[0] + AB[1] * BC[1]
    len_AB = math.hypot(AB[0], AB[1])
    len_BC = math.hypot(BC[0], BC[1])
    
    # Avoid division by zero
    if len_AB == 0 or len_BC == 0:
        return False
    
    cos_theta = dot_product / (len_AB * len_BC)
    # Clamp cos_theta to avoid floating point errors
    cos_theta = max(min(cos_theta, 1.0), -1.0)
    theta = math.acos(cos_theta)
    
    # Check if the angle is greater than 45 degrees
    return theta > math.radians(45)

def can_modify_to_remove_sharp_turn(points):
    N = len(points)
    for i in range(1, N - 1):
        A = points[i - 1]
        B = points[i]
        C = points[i + 1]
        if is_sharp_turn(A, B, C):
            # Try modifying each point to see if we can remove the sharp turn
            for j in range(N):
                for dx in range(-51, 51):
                    for dy in range(-51, 51):
                        if dx == 0 and dy == 0:
                            continue
                        new_point = points[j]
                        new_point = (new_point[0] + dx, new_point[1] + dy)
                        if new_point in points or new_point[0] < 0 or new_point[0] > 50 or new_point[1] < 0 or new_point[1] > 50:
                            continue
                        # Create a new list of points with the modified point
                        new_points = points[:]
                        new_points[j] = new_point
                        # Check if there are any sharp turns in the new points
                        sharp = False
                        for k in range(1, len(new_points) - 1):
                            if is_sharp_turn(new_points[k - 1], new_points[k], new_points[k + 1]):
                                sharp = True
                                break
                        if not sharp:
                            return True
    return False

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
            y = int(input[idx + 1])
            points.append((x, y))
            idx += 2
        # Check if there is any sharp turn
        has_sharp = False
        for i in range(1, N - 1):
            if is_sharp_turn(points[i - 1], points[i], points[i + 1]):
                has_sharp = True
                break
        # Check if it's possible to modify one point to remove sharp turn
        can_modify = can_modify_to_remove_sharp_turn(points)
        # Prepare the result
        if not has_sharp:
            results.append("yes yes")
        else:
            results.append("no" + (" yes" if can_modify else " no"))
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()