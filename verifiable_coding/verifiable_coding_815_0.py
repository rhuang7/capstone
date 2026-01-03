import sys
import itertools
from collections import deque

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def get_state(board):
    return tuple(tuple(row) for row in board)

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
        board = []
        for i in range(3):
            row = list(map(int, input[idx].split()))
            board.append(row)
            idx += 1
        while idx < len(input) and input[idx].strip() == b'':
            idx += 1
        goal = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
        start = get_state(board)
        if start == goal:
            print(0)
            continue
        visited = set()
        queue = deque()
        queue.append((start, 0))
        visited.add(start)
        found = False
        while queue:
            current, steps = queue.popleft()
            for neighbor in get_neighbors(current):
                if neighbor == goal:
                    print(steps + 1)
                    found = True
                    break
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, steps + 1))
            if found:
                break
        if not found:
            print(-1)

if __name__ == '__main__':
    solve()