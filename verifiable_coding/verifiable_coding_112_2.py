import sys
import math

def read_input():
    data = sys.stdin.buffer.read().split(b'\n')
    lines = [line.decode() for line in data if line]
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

def is_clockwise(p1, p2, p3):
    return (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0]) > 0

def solve():
    for case in read_input():
        n, grid = case
        contamination = []
        for row in grid:
            contamination.append([int(c) for c in row])
        # Convert grid to coordinates (x, y)
        # Rows are y from N down to 1, columns are x from 1 to N
        # So (x, y) is (col+1, row+1)
        # We need to find all cells with contamination 4, as those are the corners of the polygon
        # But we need to check which cells are on the border of the polygon
        # The polygon is strictly convex and has vertices on lattice points
        # The contamination of a cell is the number of its corners inside or on the polygon
        # So a cell with contamination 4 must be a corner of the polygon
        # So we can find all cells with contamination 4, and those are the vertices of the polygon
        # But wait, not exactly. Because a cell with contamination 4 could be a corner of the polygon
        # So we need to find all cells with contamination 4, and then check which of those are vertices of the polygon
        # But how to do that?
        # The polygon is strictly convex and has vertices on lattice points
        # So the vertices of the polygon are the cells with contamination 4
        # But we need to check if the cell is a corner of the polygon
        # So the approach is:
        # 1. Find all cells with contamination 4
        # 2. For each such cell, check if it is a vertex of the polygon
        # 3. The vertices of the polygon are the cells with contamination 4 that are corners of the polygon
        # 4. Then, we need to order them clockwise, starting from the lexicographically smallest
        # So first, find all cells with contamination 4
        vertices = []
        for y in range(n):
            for x in range(n):
                if contamination[y][x] == 4:
                    # Cell (x+1, y+1) has contamination 4
                    vertices.append((x+1, y+1))
        # Now, we need to check which of these are vertices of the polygon
        # The polygon is strictly convex and has vertices on lattice points
        # So the vertices are the cells with contamination 4 that are corners of the polygon
        # So we need to find the convex hull of these points
        # But wait, the polygon is strictly convex, so the convex hull is the polygon
        # So the vertices of the polygon are the convex hull of the points with contamination 4
        # So we can compute the convex hull of the points with contamination 4
        # But we need to check that the convex hull is indeed the polygon
        # So the steps are:
        # 1. Find all cells with contamination 4
        # 2. Compute their convex hull
        # 3. Check if the convex hull is indeed the polygon
        # 4. Output the convex hull in clockwise order, starting from the lexicographically smallest
        # So first, find the convex hull
        # But how to compute the convex hull?
        # We can use the Andrew monotone chain algorithm
        def cross(o, a, b):
            return (a[0]-o[0])*(b[1]-o[1]) - (a[1]-o[1])*(b[0]-o[0])
        def convex_hull(points):
            points = sorted(set(points))
            if len(points) <= 1:
                return points
            lower = []
            for p in points:
                while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
                    lower.pop()
                lower.append(p)
            upper = []
            for p in reversed(points):
                while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
                    upper.pop()
                upper.append(p)
            return lower[:-1] + upper[:-1]
        hull = convex_hull(vertices)
        # Now, we need to check if the hull is indeed the polygon
        # But the problem says that the solution is unique and exists
        # So we can assume that the convex hull is the polygon
        # Now, we need to output the hull in clockwise order, starting from the lexicographically smallest
        # So first, find the lexicographically smallest point
        min_point = min(hull)
        # Find the index of the min_point in the hull
        idx = hull.index(min_point)
        # Rotate the hull to start from the min_point
        hull = hull[idx:] + hull[:idx]
        # Now, check if the hull is clockwise
        # If not, reverse it
        # Check if the hull is clockwise
        if not is_clockwise(hull[0], hull[1], hull[-1]):
            hull = hull[::-1]
        # Output the result
        print(len(hull))
        for x, y in hull:
            print(x, y)

if __name__ == '__main__':
    solve()