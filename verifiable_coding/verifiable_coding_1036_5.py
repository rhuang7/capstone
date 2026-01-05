import sys
import math

def read_input():
    data = sys.stdin.buffer.read().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    for _ in range(T):
        x11 = int(data[idx])
        y11 = int(data[idx+1])
        x12 = int(data[idx+2])
        y12 = int(data[idx+3])
        idx += 4
        x21 = int(data[idx])
        y21 = int(data[idx+1])
        x22 = int(data[idx+2])
        y22 = int(data[idx+3])
        idx += 4
        results.append((x11, y11, x12, y12, x21, y21, x22, y22))
    return results

def get_cells(start, end):
    x1, y1, x2, y2 = start, end
    cells = set()
    if x1 == x2:
        for y in range(min(y1, y2), max(y1, y2) + 1):
            cells.add((x1, y))
    else:
        for x in range(min(x1, x2), max(x1, x2) + 1):
            cells.add((x, y1))
    return cells

def get_edges(cells1, cells2):
    edges = set()
    for (x, y) in cells1:
        if (x, y) in cells2:
            edges.add((min(x, y), max(x, y)))
            edges.add((max(x, y), min(x, y)))
    return edges

def is_valid(cells1, cells2, edges):
    all_cells = cells1 | cells2
    degree = {}
    for (x, y) in all_cells:
        degree[(x, y)] = 0
    for (x1, y1), (x2, y2) in edges:
        degree[(x1, y1)] += 1
        degree[(x2, y2)] += 1
    for (x, y), d in degree.items():
        if d > 2:
            return False
    return True

def solve():
    data = read_input()
    for x11, y11, x12, y12, x21, y21, x22, y22 in data:
        cells1 = get_cells((x11, y11), (x12, y12))
        cells2 = get_cells((x21, y21), (x22, y22))
        edges = get_edges(cells1, cells2)
        if is_valid(cells1, cells2, edges):
            print("yes")
        else:
            print("no")

if __name__ == '__main__':
    solve()