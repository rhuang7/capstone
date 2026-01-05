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
        # Determine the layer and position within the layer
        layer = 0
        while (2 * (layer + 1) - 1) ** 2 < t:
            layer += 1
        # Calculate the side length of the current layer
        side = 2 * (layer + 1) - 1
        # Calculate the remaining steps after completing the previous layers
        remaining = t - (layer ** 2)
        # Determine which side of the square the remaining steps fall on
        if remaining <= side:
            # First side: up
            x = -layer
            y = remaining - 1
        elif remaining <= 2 * side:
            # Second side: left
            x = -layer - (remaining - side)
            y = -layer
        elif remaining <= 3 * side:
            # Third side: down
            x = -layer - (remaining - 2 * side)
            y = layer
        else:
            # Fourth side: right
            x = -layer - (remaining - 3 * side)
            y = layer + (remaining - 3 * side)
        print(f"{x} {y}")

if __name__ == '__main__':
    solve()