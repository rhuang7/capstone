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
    x1, y1, x2, y2 = start[0], start[1], end[0], end[1]
    cells = set()
    if x1 == x2:
        for y in range(min(y1, y2), max(y1, y2) + 1):
            cells.add((x1, y))
    else:
        for x in range(min(x1, x2), max(x1, x2) + 1):
            cells.add((x, y1))
    return cells

def solve():
    data = read_input()
    for case in data:
        x11, y11, x12, y12, x21, y21, x22, y22 = case
        snake1 = [(x11, y11), (x12, y12)]
        snake2 = [(x21, y21), (x22, y22)]
        cells1 = get_cells(snake1[0], snake1[1])
        cells2 = get_cells(snake2[0], snake2[1])
        all_cells = cells1.union(cells2)
        adj = {}
        for cell in all_cells:
            adj[cell] = []
        # Build adjacency based on snake1
        for i in range(len(snake1) - 1):
            curr = snake1[i]
            next_ = snake1[i+1]
            adj[curr].append(next_)
            adj[next_].append(curr)
        # Build adjacency based on snake2
        for i in range(len(snake2) - 1):
            curr = snake2[i]
            next_ = snake2[i+1]
            adj[curr].append(next_)
            adj[next_].append(curr)
        # Check if all cells are connected
        visited = set()
        start_cell = next(iter(all_cells))
        stack = [start_cell]
        visited.add(start_cell)
        while stack:
            curr = stack.pop()
            for neighbor in adj[curr]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    stack.append(neighbor)
        if len(visited) != len(all_cells):
            print("no")
            continue
        # Check if all degrees are <= 2
        for cell in all_cells:
            if len(adj[cell]) > 2:
                print("no")
                break
        else:
            print("yes")

if __name__ == '__main__':
    solve()