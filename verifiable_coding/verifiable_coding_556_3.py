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
        # Determine the layer and remaining steps
        layer = 0
        while (2 * (2 * layer + 1)) <= t:
            layer += 1
        layer -= 1
        remaining = t - (2 * (2 * layer + 1) - 1)
        # Determine the direction
        if remaining < 2 * layer + 1:
            # Up
            x = -layer
            y = remaining
        elif remaining < 4 * layer + 2:
            # Left
            x = -remaining + 2 * layer + 1
            y = -layer
        elif remaining < 6 * layer + 3:
            # Down
            x = -layer
            y = -remaining + 6 * layer + 3
        else:
            # Right
            x = remaining - 6 * layer - 3
            y = layer
        print(f"{x} {y}")

if __name__ == '__main__':
    solve()