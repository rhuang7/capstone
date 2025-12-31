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

def get_edges(cells):
    edges = set()
    for (x, y) in cells:
        if x > 0:
            edges.add(( (x-1, y), (x, y) ))
        if x < 10**9:
            edges.add(( (x+1, y), (x, y) ))
        if y > 0:
            edges.add(( (x, y-1), (x, y) ))
        if y < 10**9:
            edges.add(( (x, y+1), (x, y) ))
    return edges

def is_valid(cells):
    edge_set = get_edges(cells)
    adj = {}
    for (x, y) in cells:
        adj[(x, y)] = []
    for a, b in edge_set:
        adj[a].append(b)
        adj[b].append(a)
    for (x, y) in cells:
        if len(adj[(x, y)]) > 2:
            return False
    return True

def solve():
    data = read_input()
    for x11, y11, x12, y12, x21, y21, x22, y22 in data:
        cells1 = get_cells((x11, y11), (x12, y12))
        cells2 = get_cells((x21, y21), (x22, y22))
        union = cells1.union(cells2)
        if not is_valid(union):
            print("no")
            continue
        # Check if the union is connected
        visited = set()
        stack = [next(iter(union))]
        visited.add(stack[0])
        while stack:
            node = stack.pop()
            for neighbor in adj[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    stack.append(neighbor)
        if len(visited) != len(union):
            print("no")
        else:
            print("yes")

if __name__ == '__main__':
    solve()