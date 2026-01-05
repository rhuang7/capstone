import sys
from collections import deque

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def get_state(s):
    return tuple(map(int, s.split()))

def get_neighbors(state):
    neighbors = []
    pos = [i for i in range(9) if state[i] != 0]
    for i in range(9):
        if state[i] == 0:
            for j in range(i-1, i+2):
                if 0 <= j < 9 and j != i:
                    if is_prime(state[i] + state[j]):
                        new_state = list(state)
                        new_state[i], new_state[j] = new_state[j], new_state[i]
                        neighbors.append(tuple(new_state))
    return neighbors

def bfs(start):
    visited = set()
    queue = deque()
    queue.append((start, 0))
    visited.add(start)
    while queue:
        state, steps = queue.popleft()
        if state == (1, 2, 3, 4, 5, 6, 7, 8, 9):
            return steps
        for neighbor in get_neighbors(state):
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
        while idx < len(input) and input[idx].strip() == '':
            idx += 1
        if idx >= len(input):
            break
        grid = []
        for _ in range(3):
            while idx < len(input) and input[idx].strip() == '':
                idx += 1
            if idx >= len(input):
                break
            grid.append(list(map(int, input[idx].split())))
            idx += 1
        start = tuple(grid[0] + grid[1] + grid[2])
        print(bfs(start))

if __name__ == '__main__':
    solve()