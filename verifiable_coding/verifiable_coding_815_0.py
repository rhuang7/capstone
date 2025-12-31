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

def get_state(board):
    return tuple(tuple(row) for row in board)

def get_neighbors(state):
    neighbors = []
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < 3 and 0 <= nj < 3:
                        new_state = [list(row) for row in state]
                        new_state[i][j], new_state[ni][nj] = new_state[ni][nj], new_state[i][j]
                        if is_prime(new_state[i][j] + new_state[ni][nj]):
                            neighbors.append(tuple(tuple(row) for row in new_state))
                break
    return neighbors

def solve():
    import sys
    input = sys.stdin.buffer.read().split(b'\n')
    cases = []
    idx = 0
    while idx < len(input):
        if input[idx].strip() == b'':
            idx += 1
            continue
        case = []
        for i in range(3):
            if idx >= len(input):
                break
            line = input[idx].strip().split()
            if not line:
                idx += 1
                continue
            case.append(list(map(int, line)))
            idx += 1
        if case:
            cases.append(case)
    
    target = (1, 2, 3, 4, 5, 6, 7, 8, 9)
    for case in cases:
        initial = get_state(case)
        if initial == target:
            print(0)
            continue
        visited = set()
        queue = deque()
        queue.append((initial, 0))
        visited.add(initial)
        found = False
        while queue:
            state, steps = queue.popleft()
            for neighbor in get_neighbors(state):
                if neighbor == target:
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