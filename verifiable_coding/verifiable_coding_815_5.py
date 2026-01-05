import sys
import math
from collections import deque

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
    state_list = list(state)
    for i in range(9):
        for j in range(9):
            if i % 3 == 0 and j % 3 == 0:
                continue
            if abs(i - j) == 1 and (i // 3 == j // 3 or (i % 3 == j % 3)):
                if is_prime(state_list[i] + state_list[j]):
                    new_state = list(state_list)
                    new_state[i], new_state[j] = new_state[j], new_state[i]
                    neighbors.append(tuple(tuple(row) for row in new_state))
    return neighbors

def bfs(start):
    target = (1, 2, 3, 4, 5, 6, 7, 8, 9)
    if start == target:
        return 0
    visited = set()
    queue = deque()
    queue.append((start, 0))
    visited.add(start)
    while queue:
        current, steps = queue.popleft()
        for neighbor in get_neighbors(current):
            if neighbor == target:
                return steps + 1
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
            while idx < len(input) and input[idx].strip() == '':
                idx += 1
            row = list(map(int, input[idx].strip().split()))
            grid.append(row)
            idx += 1
        start = get_state_tuple(grid)
        result = bfs(start)
        print(result)

if __name__ == '__main__':
    solve()