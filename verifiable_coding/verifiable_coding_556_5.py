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
        # Determine the spiral layer
        layer = 0
        while (2 * (2 * layer + 1)) <= t:
            layer += 1
        layer -= 1
        # Calculate remaining steps after completing the layer
        remaining = t - (2 * (2 * layer + 1) - 1)
        # Determine which side of the spiral the remaining steps fall on
        if remaining <= 2 * layer + 1:
            # Up
            x = -layer
            y = remaining - 1
        elif remaining <= 4 * layer + 2:
            # Left
            x = -layer - (remaining - (2 * layer + 2))
            y = -layer
        elif remaining <= 6 * layer + 3:
            # Down
            x = -layer - (remaining - (4 * layer + 3))
            y = layer
        else:
            # Right
            x = -layer - (remaining - (6 * layer + 4))
            y = layer
        print(f"{x} {y}")

if __name__ == '__main__':
    solve()