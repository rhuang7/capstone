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
        current_dir = (0, 1)  # Start facing North (y increases upwards)
        for part in path:
            if part.isdigit():
                distance += int(part)
            else:
                # Turn left or right
                if part == 'L':
                    current_dir = (-current_dir[1], current_dir[0])
                else:  # 'R'
                    current_dir = (current_dir[1], -current_dir[0])
                # Move one unit in the new direction
                direction = (direction[0] + current_dir[0], direction[1] + current_dir[1])
        # Determine direction
        if direction == (0, 0):
            print(f"{distance}.0")
        else:
            # Determine the direction based on the final position
            dx, dy = direction
            if dx > 0:
                if dy > 0:
                    dir_str = "NE"
                elif dy < 0:
                    dir_str = "SE"
                else:
                    dir_str = "E"
            elif dx < 0:
                if dy > 0:
                    dir_str = "NW"
                elif dy < 0:
                    dir_str = "SW"
                else:
                    dir_str = "W"
            elif dy > 0:
                dir_str = "N"
            else:
                dir_str = "S"
            print(f"{distance}.0{dir_str}")

if __name__ == '__main__':
    solve()