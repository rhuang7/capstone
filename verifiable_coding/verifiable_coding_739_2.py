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
        current_dir = 'N'  # Initial direction is North
        for part in path:
            if part.isdigit():
                distance += int(part)
            else:
                # Change direction based on current direction and turn
                if current_dir == 'N':
                    if part == 'L':
                        current_dir = 'W'
                        direction = (-1, 0)
                    else:  # 'R'
                        current_dir = 'E'
                        direction = (1, 0)
                elif current_dir == 'E':
                    if part == 'L':
                        current_dir = 'N'
                        direction = (0, 1)
                    else:  # 'R'
                        current_dir = 'S'
                        direction = (0, -1)
                elif current_dir == 'S':
                    if part == 'L':
                        current_dir = 'E'
                        direction = (1, 0)
                    else:  # 'R'
                        current_dir = 'W'
                        direction = (-1, 0)
                elif current_dir == 'W':
                    if part == 'L':
                        current_dir = 'S'
                        direction = (0, -1)
                    else:  # 'R'
                        current_dir = 'N'
                        direction = (0, 1)
        # Calculate final direction
        if direction == (0, 0):
            print(f"{distance}.00")
        else:
            # Determine direction based on final position
            if direction[0] > 0 and direction[1] > 0:
                dir = 'NE'
            elif direction[0] > 0 and direction[1] == 0:
                dir = 'E'
            elif direction[0] > 0 and direction[1] < 0:
                dir = 'SE'
            elif direction[0] == 0 and direction[1] > 0:
                dir = 'N'
            elif direction[0] < 0 and direction[1] > 0:
                dir = 'NW'
            elif direction[0] < 0 and direction[1] == 0:
                dir = 'W'
            elif direction[0] < 0 and direction[1] < 0:
                dir = 'SW'
            elif direction[0] == 0 and direction[1] < 0:
                dir = 'S'
            # Calculate distance with one decimal place
            dist = distance + 0.0
            print(f"{dist:.1f}{dir}")

if __name__ == '__main__':
    solve()