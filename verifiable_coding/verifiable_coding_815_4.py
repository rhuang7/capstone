import sys
import itertools
from collections import deque

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

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
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for dx, dy in directions:
        nx, ny = i + dx, j + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [list(row) for row in state]
            new_state[i][j], new_state[nx][ny] = new_state[nx][ny], new_state[i][j]
            if is_prime(new_state[i][j] + new_state[nx][ny]):
                neighbors.append(tuple(tuple(row) for row in new_state))
    return neighbors

def solve():
    input = sys.stdin.buffer.read().split(b'\n')
    idx = 0
    t = int(input[idx])
    idx += 1
    for _ in range(t):
        while idx < len(input) and input[idx].strip() == b'':
            idx += 1
        if idx >= len(input):
            break
        state = []
        for _ in range(3):
            while idx < len(input) and input[idx].strip() == b'':
                idx += 1
            if idx >= len(input):
                break
            row = list(map(int, input[idx].strip().split()))
            state.append(tuple(row))
            idx += 1
        target = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
        visited = set()
        queue = deque()
        queue.append((tuple(tuple(row) for row in state), 0))
        visited.add(tuple(tuple(row) for row in state))
        found = False
        while queue:
            current, steps = queue.popleft()
            if current == target:
                print(steps)
                found = True
                break
            for neighbor in get_neighbors(current):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, steps + 1))
        if not found:
            print(-1)

if __name__ == '__main__':
    solve()