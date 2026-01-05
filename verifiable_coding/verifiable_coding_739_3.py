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
                    # Start direction is North
                    if part == 'R':
                        direction = (0, 1)
                    else:
                        direction = (0, -1)
                else:
                    # Rotate direction
                    if part == 'R':
                        # Right turn
                        if direction == (0, 1):  # North
                            direction = (1, 0)  # East
                        elif direction == (1, 0):  # East
                            direction = (0, -1)  # West
                        elif direction == (0, -1):  # West
                            direction = (-1, 0)  # South
                        elif direction == (-1, 0):  # South
                            direction = (0, 1)  # North
                    else:
                        # Left turn
                        if direction == (0, 1):  # North
                            direction = (-1, 0)  # West
                        elif direction == (-1, 0):  # West
                            direction = (0, -1)  # South
                        elif direction == (0, -1):  # South
                            direction = (1, 0)  # East
                        elif direction == (1, 0):  # East
                            direction = (0, 1)  # North
        # Calculate distance
        dist = (abs(direction[0]) + abs(direction[1])) * 1.0
        # Calculate direction
        if direction == (0, 0):
            print(f"0.0")
        else:
            if direction[0] > 0:
                if direction[1] > 0:
                    dir = "NE"
                elif direction[1] < 0:
                    dir = "NW"
                else:
                    dir = "E"
            elif direction[0] < 0:
                if direction[1] > 0:
                    dir = "SE"
                elif direction[1] < 0:
                    dir = "SW"
                else:
                    dir = "W"
            elif direction[1] > 0:
                dir = "N"
            else:
                dir = "S"
            print(f"{dist:.1f}{dir}")

if __name__ == '__main__':
    solve()