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
        current_dir = 'N'  # initial direction is North
        for part in path:
            if part.isdigit():
                distance += int(part)
            else:
                # Turn left or right
                if current_dir == 'N':
                    if part == 'L':
                        current_dir = 'W'
                    else:
                        current_dir = 'E'
                elif current_dir == 'E':
                    if part == 'L':
                        current_dir = 'N'
                    else:
                        current_dir = 'S'
                elif current_dir == 'S':
                    if part == 'L':
                        current_dir = 'E'
                    else:
                        current_dir = 'W'
                elif current_dir == 'W':
                    if part == 'L':
                        current_dir = 'S'
                    else:
                        current_dir = 'N'
        # Calculate final direction
        if direction == (0, 0):
            print(f"{distance}.0")
        else:
            # Determine final direction based on current_dir and displacement
            if direction[0] > 0 and direction[1] > 0:
                dir = 'NE'
            elif direction[0] > 0 and direction[1] == 0:
                dir = 'E'
            elif direction[0] > 0 and direction[1] < 0:
                dir = 'SE'
            elif direction[0] == 0 and direction[1] > 0:
                dir = 'N'
            elif direction[0] == 0 and direction[1] < 0:
                dir = 'S'
            elif direction[0] < 0 and direction[1] > 0:
                dir = 'NW'
            elif direction[0] < 0 and direction[1] == 0:
                dir = 'W'
            elif direction[0] < 0 and direction[1] < 0:
                dir = 'SW'
            else:
                dir = 'N'
            print(f"{distance}.0{dir}")

if __name__ == '__main__':
    solve()