import sys

def solve():
    import sys
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    idx = 1
    for _ in range(T):
        path = input[idx]
        idx += 1
        distance = 0
        direction = (0, 0)  # (x, y)
        parts = path.split()
        for part in parts:
            if part.isdigit():
                distance += int(part)
            else:
                if direction == (0, 0):
                    if part == 'R':
                        direction = (0, 1)
                    else:
                        direction = (0, -1)
                else:
                    if part == 'R':
                        direction = (direction[1], -direction[0])
                    else:
                        direction = (direction[1], direction[0])
        if direction == (0, 0):
            print(f"{distance}.00")
        else:
            dx, dy = direction
            if dx > 0:
                if dy > 0:
                    dir = "NE"
                else:
                    dir = "SE"
            elif dx < 0:
                if dy > 0:
                    dir = "NW"
                else:
                    dir = "SW"
            elif dy > 0:
                dir = "N"
            else:
                dir = "S"
            print(f"{distance}.0{dir}")

if __name__ == '__main__':
    solve()