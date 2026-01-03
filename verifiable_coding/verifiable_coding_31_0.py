import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    t = int(data[0])
    cases = data[1:t+1]

    directions = {
        'N': (0, 1),
        'S': (0, -1),
        'W': (-1, 0),
        'E': (1, 0)
    }

    for s in cases:
        x, y = 0, 0
        visited = set()
        visited.add((x, y))
        time = 0
        for move in s:
            dx, dy = directions[move]
            x += dx
            y += dy
            pos = (x, y)
            if pos in visited:
                time += 1
            else:
                time += 5
                visited.add(pos)
        print(time)

if __name__ == '__main__':
    solve()