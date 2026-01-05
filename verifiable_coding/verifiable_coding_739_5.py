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
        current_dir = (0, 1)  # Start facing North (y increases)
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
        # Calculate the direction
        dx, dy = direction
        if dx == 0 and dy == 0:
            print(f"0.0")
        else:
            # Determine direction
            if dx > 0:
                if dy > 0:
                    dir = "NE"
                elif dy < 0:
                    dir = "SE"
                else:
                    dir = "E"
            elif dx < 0:
                if dy > 0:
                    dir = "NW"
                elif dy < 0:
                    dir = "SW"
                else:
                    dir = "W"
            elif dy > 0:
                dir = "N"
            else:
                dir = "S"
            # Calculate distance
            dist = (dx**2 + dy**2)**0.5
            print(f"{dist:.1f}{dir}")

if __name__ == '__main__':
    solve()