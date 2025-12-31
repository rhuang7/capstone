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

def is_clockwise(p1, p2, p3):
    return (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0]) > 0

def solve():
    for n, grid in read_input():
        contamination = []
        for i in range(n):
            row = grid[i]
            contamination.append([int(c) for c in row])
        # Find all cells with contamination level 4
        vertices = []
        for y in range(n):
            for x in range(n):
                if contamination[y][x] == 4:
                    vertices.append((x + 1, y + 1))
        # Check if the vertices form a convex polygon
        if len(vertices) == 0:
            print(0)
            continue
        # Find the lexicographically smallest vertex
        min_vertex = min(vertices)
        # Sort the vertices in clockwise order
        vertices.sort(key=lambda p: (p[0], p[1]))
        # Check if the polygon is convex
        is_convex = True
        for i in range(len(vertices)):
            p1 = vertices[i]
            p2 = vertices[(i + 1) % len(vertices)]
            p3 = vertices[(i + 2) % len(vertices)]
            if not is_clockwise(p1, p2, p3):
                is_convex = False
                break
        if not is_convex:
            print(0)
            continue
        # Output the result
        print(len(vertices))
        for x, y in vertices:
            print(x, y)

if __name__ == '__main__':
    solve()