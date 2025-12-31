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
        while (2 * (layer + 1) - 1) * 4 <= t:
            layer += 1
        # Calculate the remaining steps after completing the layer
        remaining = t - (2 * layer + 1) * 4 + 4
        # Determine the direction
        if remaining <= layer + 1:
            # Up
            x, y = 0, layer + 1
        elif remaining <= 2 * (layer + 1):
            # Left
            x, y = -(remaining - (layer + 1)), layer + 1
        elif remaining <= 3 * (layer + 1):
            # Down
            x, y = -(layer + 1), (remaining - 2 * (layer + 1))
        else:
            # Right
            x, y = (remaining - 3 * (layer + 1)), -(layer + 1)
        print(f"{x} {y}")

if __name__ == '__main__':
    solve()