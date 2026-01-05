import sys
from collections import deque, defaultdict
import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def get_state_tuple(grid):
    return tuple(tuple(row) for row in grid)

def get_neighbors(state):
    neighbors = []
    pos = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                pos = i * 3 + j
                break
        else:
            continue
        break
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dx, dy in directions:
        nx, ny = i + dx, j + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [list(row) for row in state]
            new_state[i][j], new_state[nx][ny] = new_state[nx][ny], new_state[i][j]
            new_state_tuple = get_state_tuple(new_state)
            if is_prime(new_state[i][j] + new_state[nx][ny]):
                neighbors.append(new_state_tuple)
    return neighbors

def bfs(start):
    target = (1, 2, 3, 4, 5, 6, 7, 8, 9)
    visited = set()
    queue = deque()
    queue.append((start, 0))
    visited.add(start)
    while queue:
        current, steps = queue.popleft()
        if current == target:
            return steps
        for neighbor in get_neighbors(current):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, steps + 1))
    return -1

def solve():
    import sys
    input = sys.stdin.buffer.read().split(b'\n')
    idx = 0
    t = int(input[idx])
    idx += 1
    for _ in range(t):
        grid = []
        while idx < len(input) and input[idx].strip() == '':
            idx += 1
        for _ in range(3):
            if idx >= len(input):
                break
            row = list(map(int, input[idx].strip().split()))
            grid.append(row)
            idx += 1
        start = get_state_tuple(grid)
        result = bfs(start)
        print(result)

if __name__ == '__main__':
    solve()