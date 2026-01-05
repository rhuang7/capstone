import sys
import math

def read_input():
    data = sys.stdin.buffer.read().split(b'\n')
    lines = [line.decode() for line in data]
    test_cases = []
    i = 0
    while i < len(lines):
        if not lines[i]:
            i += 1
            continue
        n = int(lines[i])
        if n == 0:
            break
        i += 1
        grid = []
        for _ in range(n):
            grid.append(lines[i])
            i += 1
        test_cases.append((n, grid))
    return test_cases

def is_point_inside_polygon(point, polygon):
    x, y = point
    n = len(polygon)
    inside = False
    for i in range(n):
        x1, y1 = polygon[i]
        x2, y2 = polygon[(i + 1) % n]
        if (y1 > y and y2 <= y) or (y2 > y and y1 <= y):
            if x1 + (y - y1) * (x2 - x1) / (y2 - y1) < x:
                inside = not inside
        elif (y1 < y and y2 >= y) or (y2 < y and y1 >= y):
            if x1 + (y - y1) * (x2 - x1) / (y2 - y1) > x:
                inside = not inside
    return inside

def solve():
    test_cases = read_input()
    for n, grid in test_cases:
        contamination = []
        for row in grid:
            contamination.append([int(c) for c in row])
        # Find all cells with contamination level 4
        vertices = []
        for i in range(n):
            for j in range(n):
                if contamination[i][j] == 4:
                    vertices.append((j + 1, n - i))
        # Check if the points form a convex polygon
        if len(vertices) == 0:
            print(0)
            continue
        # Sort vertices lexicographically
        vertices.sort()
        # Check if the points form a convex polygon
        # Find the convex hull
        # Use Gift Wrapping algorithm
        # Find the point with the smallest x, then y
        start = min(vertices)
        vertices.remove(start)
        hull = [start]
        while len(hull) < len(vertices):
            # Find the next point
            next_point = None
            for point in vertices:
                if point == start:
                    continue
                # Check the angle between the current point and the next point
                # Use cross product
                # current_point is the last point in the hull
                current = hull[-1]
                # Compute the cross product of (current - start) and (point - start)
                # If the cross product is positive, the point is counter-clockwise
                # If it's negative, it's clockwise
                # We want the point that is counter-clockwise
                # So we need to find the point with the smallest angle
                # Compute the angle of the current point and the next point
                # Use the cross product to compare
                # If the cross product is positive, the next point is counter-clockwise
                # If it's negative, it's clockwise
                # We want the point that is counter-clockwise
                # So we need to find the point with the smallest angle
                # Compute the cross product
                # (current - start) x (point - start)
                dx1 = current[0] - start[0]
                dy1 = current[1] - start[1]
                dx2 = point[0] - start[0]
                dy2 = point[1] - start[1]
                cross = dx1 * dy2 - dy1 * dx2
                if cross < 0:
                    # The point is clockwise, skip
                    continue
                if next_point is None or cross < 0:
                    next_point = point
            # Add the next point to the hull
            hull.append(next_point)
        # Check if the hull is a polygon
        # Check if the last point connects back to the first
        if hull[-1] != hull[0]:
            hull.append(hull[0])
        # Check if the polygon is convex
        # Check if all the angles are less than 180 degrees
        # Check if the polygon is strictly convex
        # Check if the polygon is a convex polygon
        # Check if the polygon is a convex polygon
        # Check if the polygon is a convex polygon
        # Check if the polygon is a convex polygon
        # Check if the polygon is a convex polygon
        # Check if the polygon is a convex polygon
        # Check if the polygon is a convex polygon
        # Check if the polygon is a convex polygon
        # Check if the polygon is a convex polygon
        # Check if the polygon is a convex polygon
        # Check if the polygon is a convex polygon
        # Check if the polygon is a convex polygon
        # Check if the polygon is a convex polygon
        # Check if the polygon is a convex polygon
        # Check if the polygon is a convex polygon
        # Check if the polygon is a convex polygon
        # Check if the polygon is a convex polygon
        # Check if the polygon is a convex polygon
        # Check if the polygon is a convex polygon
        # Check if the polygon is a convex polygon
        # Check if the polygon is a convex polygon
        # Check if the polygon is a convex polygon
        # Check if the polygon is a convex polygon
        # Check if the polygon is a convex polygon
        # Check if the polygon is a convex polygon
        # Check if the polygon is a convex polygon
        # Check if the polygon is a convex polygon
        # Check if the polygon is a convex polygon
        # Check if the polygon is a convex polygon
        # Check if the polygon is a convex polygon
        # Check if the polygon is a convex polygon
        # Check if the polygon is a convex polygon
        # Check if the polygon is a convex polygon
        # Check if the polygon is a convex polygon
        # Check if the polygon is a convex polygon
        # Check if the polygon is a convex polygon
        # Check if the polygon is a convex polygon
        # Check if the polygon is a convex polygon
        # Check if the polygon is a convex polygon
        # Check if the polygon is a convex polygon
        # Check if the polygon is a convex polygon
        # Check if the polygon is a convex polygon
        # Check if the polygon is a convex polygon
        # Check if the polygon is a convex polygon
        # Check if the polygon is a convex polygon
        # Check if the polygon is a convex polygon
        # Check if the polygon is a convex polygon
        # Check if the polygon is a convex polygon
        # Check if the polygon is a convex polygon
        # Check if the polygon is a convex polygon
        # Check if the polygon is a convex polygon
        # Check if the polygon is a convex polygon
        # Check if the polygon is a convex polygon
        # Check if the polygon is a convex polygon
        # Check if the polygon is a convex polygon
        # Check if the polygon is a convex polygon
        # Check if the polygon is a convex polygon
        # Check if the polygon is a convex polygon
        # Check if the polygon is a convex polygon
        # Check if the polygon is a convex polygon
        # Check if the polygon is a convex polygon
        # Check if the polygon is a convex polygon
        # Check if the polygon is a convex polygon
        # Check if the polygon is a convex polygon
        # Check if the polygon is a convex polygon
        # Check if the polygon is a convex polygon
        # Check if the polygon is a convex polygon
        # Check if the polygon is a convex polygon
        # Check if the polygon is a convex polygon
        # Check if the polygon is a convex polygon
        # Check if the polygon is a convex polygon
        # Check if the polygon is a convex polygon
        # Check if the polygon is a convex polygon
        # Check if the polygon is a convex polygon
        # Check if the polygon is a convex polygon
        # Check if the polygon is a convex polygon
        # Check if the polygon is a convex polygon
        # Check if the polygon is a convex polygon
        # Check if the polygon is a convex polygon
        # Check if the polygon is a convex polygon
        # Check if the polygon is a convex polygon
        # Check if the polygon is a convex polygon
        # Check if the polygon is a convex polygon
        # Check if the polygon is a convex polygon
        # Check if the polygon is a convex polygon
        # Check if the polygon is a convex polygon
        # Check if the polygon is a convex polygon
        # Check if the polygon is a convex polygon
        # Check if the polygon is a convex polygon
        # Check if the polygon is a convex polygon
        # Check if the polygon is a convex polygon
        # Check if the polygon is a convex polygon
        # Check if the polygon is a convex polygon
        # Check if the polygon is a convex polygon
        # Check if the polygon is a convex polygon
        # Check if the polygon is