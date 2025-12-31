import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    n = int(data[0])
    a = list(map(int, data[1:]))

    from collections import deque

    # Build a graph of possible transitions
    graph = {}
    for num in a:
        graph[num] = []

    for num in a:
        if num * 2 in graph:
            graph[num].append(num * 2)
        if num % 3 == 0:
            graph[num].append(num // 3)

    # Find the starting number (the one with no incoming edges)
    start = None
    for num in a:
        if num not in graph or len(graph[num]) == 0:
            start = num
            break

    # Perform BFS to find the correct order
    visited = set()
    queue = deque([start])
    result = []

    while queue:
        current = queue.popleft()
        result.append(current)
        visited.add(current)
        for neighbor in graph[current]:
            if neighbor not in visited:
                queue.append(neighbor)

    print(' '.join(map(str, result)))

if __name__ == '__main__':
    solve()