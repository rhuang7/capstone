import sys
import math

def read_input():
    data = sys.stdin.buffer.read().split(b'\n')
    lines = [line.decode() for line in data if line.strip()]
    idx = 0
    while idx < len(lines):
        if not lines[idx]:
            idx += 1
            continue
        n = int(lines[idx])
        if n == 0:
            break
        idx += 1
        grid = []
        for _ in range(n):
            grid.append(lines[idx])
            idx += 1
        yield n, grid

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
    for n, grid in read_input():
        contamination = []
        for i in range(n):
            row = grid[i]
            contamination.append([int(c) for c in row])
        
        polygon = []
        for y in range(n):
            for x in range(n):
                count = 0
                for dx, dy in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
                    nx = x + dx
                    ny = y + dy
                    if 0 <= nx < n and 0 <= ny < n:
                        count += contamination[ny][nx]
                if count == 4:
                    polygon.append((x + 1, y + 1))
        
        polygon.sort()
        start = polygon[0]
        polygon = [p for p in polygon if p != start]
        for i in range(len(polygon)):
            if polygon[i] == start:
                polygon = polygon[i+1:] + polygon[:i]
                break
        
        print(len(polygon))
        for x, y in polygon:
            print(x, y)

if __name__ == '__main__':
    solve()