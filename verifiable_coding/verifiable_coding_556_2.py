import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    t_list = list(map(int, data[1:]))
    
    for t in t_list:
        if t == 0:
            print("0 0")
            continue
        # Determine the side length of the square the t-th move is on
        side = 1
        while side * 4 <= t:
            side += 1
        side -= 1
        # Determine the remaining steps after completing the square of side length
        remaining = t - (side * 4 - 4)
        # Determine the direction
        if remaining < side:
            # First side: right
            x = remaining - 1
            y = side
        elif remaining < 2 * side:
            # Second side: down
            x = -side
            y = side - (remaining - side) - 1
        elif remaining < 3 * side:
            # Third side: left
            x = -side - (remaining - 2 * side) + 1
            y = -side
        else:
            # Fourth side: up
            x = 0
            y = -side - (remaining - 3 * side) + 1
        print(f"{x} {y}")

if __name__ == '__main__':
    solve()