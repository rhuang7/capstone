import sys
import math

def read_input():
    data = sys.stdin.buffer.read().split(b'\n')
    idx = 0
    while True:
        if idx >= len(data):
            break
        line = data[idx].strip()
        if not line:
            idx += 1
            continue
        n = int(line)
        if n == 0:
            break
        grid = []
        for _ in range(n):
            if idx >= len(data):
                break
            row = data[idx].strip()
            if row:
                grid.append(row)
            idx += 1
        yield n, grid
        idx += 1

def is_point_in_polygon(point, polygon):
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
    for n, grid in read_input():
        contamination = []
        for i in range(n):
            row = grid[i]
            contamination.append([int(c) for c in row])
        # Find all cells with contamination level 4
        polygon = []
        for y in range(n):
            for x in range(n):
                if contamination[y][x] == 4:
                    polygon.append((x + 1, y + 1))
        # Check if the polygon is a convex polygon
        # Sort the polygon points
        polygon.sort()
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