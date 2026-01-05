import sys
import heapq
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
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dx, dy in directions:
        nx, ny = i + dx, j + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [list(row) for row in state]
            new_state[i][j], new_state[nx][ny] = new_state[nx][ny], new_state[i][j]
            if is_prime(new_state[i][j] + new_state[nx][ny]):
                neighbors.append(tuple(tuple(row) for row in new_state))
    return neighbors

def solve():
    import sys
    input = sys.stdin.buffer.read().split(b'\n')
    cases = []
    i = 0
    while i < len(input):
        if input[i].strip() == b'':
            i += 1
            continue
        case = []
        for j in range(3):
            if i >= len(input):
                break
            line = input[i].strip().split()
            if len(line) == 3:
                case.append(list(map(int, line)))
            i += 1
        if case:
            cases.append(case)
    for case in cases:
        start = tuple(tuple(row) for row in case)
        target = ( (1, 2, 3), (4, 5, 6), (7, 8, 9) )
        if start == target:
            print(0)
            continue
        visited = set()
        queue = deque()
        queue.append( (start, 0) )
        visited.add( start )
        found = False
        while queue:
            current, steps = queue.popleft()
            for neighbor in get_neighbors(current):
                if neighbor == target:
                    print(steps + 1)
                    found = True
                    break
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append( (neighbor, steps + 1) )
            if found:
                break
        if not found:
            print(-1)

if __name__ == '__main__':
    solve()