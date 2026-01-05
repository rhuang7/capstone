import sys
import math

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
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
        
        # Function to get the snake cells
        def get_cells(start, end):
            x1, y1 = start
            x2, y2 = end
            cells = set()
            if x1 == x2:
                for y in range(min(y1, y2), max(y1, y2) + 1):
                    cells.add((x1, y))
            else:
                for x in range(min(x1, x2), max(x1, x2) + 1):
                    cells.add((x, y1))
            return cells
        
        snake1 = get_cells((x11, y11), (x12, y12))
        snake2 = get_cells((x21, y21), (x22, y22))
        
        # Function to check if two cells are adjacent in either snake
        def is_adjacent(a, b):
            if a == b:
                return True
            x1, y1 = a
            x2, y2 = b
            if x1 == x2:
                return abs(y1 - y2) == 1
            else:
                return abs(x1 - x2) == 1
        
        # Build graph
        graph = {}
        for cell in snake1 | snake2:
            graph[cell] = []
        for cell in snake1 | snake2:
            for neighbor in snake1 | snake2:
                if is_adjacent(cell, neighbor):
                    graph[cell].append(neighbor)
        
        # Check if the union is connected
        def is_connected(start, end):
            visited = set()
            queue = [start]
            visited.add(start)
            while queue:
                current = queue.pop(0)
                if current == end:
                    return True
                for neighbor in graph[current]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
            return False
        
        start = next(iter(snake1 | snake2))
        end = next(iter(snake1 | snake2))
        if not is_connected(start, end):
            results.append("no")
            continue
        
        # Check if all nodes have degree <= 2
        valid = True
        for cell in graph:
            if len(graph[cell]) > 2:
                valid = False
                break
        if valid:
            results.append("yes")
        else:
            results.append("no")
    
    print('\n'.join(results))