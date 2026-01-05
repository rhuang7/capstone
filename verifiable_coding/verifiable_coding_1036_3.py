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
        idx +=4
        x21 = int(data[idx])
        y21 = int(data[idx+1])
        x22 = int(data[idx+2])
        y22 = int(data[idx+3])
        idx +=4
        
        # Function to get all cells in a snake
        def get_cells(x1, y1, x2, y2):
            if x1 == x2:
                # Same row
                start = min(y1, y2)
                end = max(y1, y2)
                return [(x1, y) for y in range(start, end+1)]
            else:
                # Same column
                start = min(x1, x2)
                end = max(x1, x2)
                return [(x, y1) for x in range(start, end+1)]
        
        snake1 = get_cells(x11, y11, x12, y12)
        snake2 = get_cells(x21, y21, x22, y22)
        
        # Combine cells
        all_cells = set(snake1 + snake2)
        
        # Build graph
        graph = {}
        for (x, y) in all_cells:
            graph[(x, y)] = []
        
        # Add edges from snake1
        for i in range(len(snake1)-1):
            x1, y1 = snake1[i]
            x2, y2 = snake1[i+1]
            graph[(x1, y1)].append((x2, y2))
            graph[(x2, y2)].append((x1, y1))
        
        # Add edges from snake2
        for i in range(len(snake2)-1):
            x1, y1 = snake2[i]
            x2, y2 = snake2[i+1]
            graph[(x1, y1)].append((x2, y2))
            graph[(x2, y2)].append((x1, y1))
        
        # Check if all degrees are <= 2
        for v in graph:
            if len(graph[v]) > 2:
                results.append("no")
                break
        else:
            # Check if the graph is connected
            visited = set()
            start = next(iter(all_cells))
            stack = [start]
            visited.add(start)
            while stack:
                v = stack.pop()
                for neighbor in graph[v]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        stack.append(neighbor)
            if len(visited) != len(all_cells):
                results.append("no")
            else:
                results.append("yes")
    
    print('\n'.join(results))