import sys

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
        
        # Function to get all cells in a snake
        def get_cells(x1, y1, x2, y2):
            cells = set()
            if x1 == x2:
                for y in range(min(y1, y2), max(y1, y2) + 1):
                    cells.add((x1, y))
            else:
                for x in range(min(x1, x2), max(x1, x2) + 1):
                    cells.add((x, y1))
            return cells
        
        cells1 = get_cells(x11, y11, x12, y12)
        cells2 = get_cells(x21, y21, x22, y22)
        
        # Combine cells
        all_cells = cells1.union(cells2)
        
        # Build graph
        graph = {}
        for cell in all_cells:
            graph[cell] = []
        
        # Add edges from first snake
        for i in range(len(cells1) - 1):
            cell1 = list(cells1)[i]
            cell2 = list(cells1)[i+1]
            graph[cell1].append(cell2)
            graph[cell2].append(cell1)
        
        # Add edges from second snake
        for i in range(len(cells2) - 1):
            cell1 = list(cells2)[i]
            cell2 = list(cells2)[i+1]
            graph[cell1].append(cell2)
            graph[cell2].append(cell1)
        
        # Check if all cells are connected
        visited = set()
        start = next(iter(all_cells))
        stack = [start]
        visited.add(start)
        while stack:
            cell = stack.pop()
            for neighbor in graph[cell]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    stack.append(neighbor)
        if len(visited) != len(all_cells):
            results.append("no")
            continue
        
        # Check if all degrees are <= 2
        for cell in all_cells:
            if len(graph[cell]) > 2:
                results.append("no")
                break
        else:
            results.append("yes")
    
    print("\n".join(results))

if __name__ == '__main__':
    solve()