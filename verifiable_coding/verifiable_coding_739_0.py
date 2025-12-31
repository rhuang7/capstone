import sys

def solve():
    import sys
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    idx = 1
    for _ in range(T):
        path = input[idx:]
        idx += len(path)
        distance = 0
        direction = (0, 0)  # (x, y)
        current_dir = (0, 1)  # North
        for part in path:
            if part.isdigit():
                distance += int(part)
            else:
                if part == 'L':
                    current_dir = (-current_dir[1], current_dir[0])
                elif part == 'R':
                    current_dir = (current_dir[1], -current_dir[0])
                direction = (direction[0] + current_dir[0], direction[1] + current_dir[1])
        if distance == 0:
            print("0.0")
            continue
        dx, dy = direction
        if dx == 0 and dy > 0:
            dir_str = "N"
        elif dx == 0 and dy < 0:
            dir_str = "S"
        elif dx > 0 and dy == 0:
            dir_str = "E"
        elif dx < 0 and dy == 0:
            dir_str = "W"
        elif dx > 0 and dy > 0:
            dir_str = "NE"
        elif dx > 0 and dy < 0:
            dir_str = "SE"
        elif dx < 0 and dy > 0:
            dir_str = "NW"
        elif dx < 0 and dy < 0:
            dir_str = "SW"
        else:
            dir_str = "N"
        print(f"{distance}.0{dir_str}")

if __name__ == '__main__':
    solve()