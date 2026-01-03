import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    t_list = list(map(int, data[1:T+1]))
    
    for t in t_list:
        if t == 0:
            print("0 0")
            continue
        n = t
        # Determine the layer and the position within the layer
        layer = 0
        while (2 * (layer + 1)) ** 2 <= n:
            layer += 1
        side = 2 * (layer + 1)
        remainder = n - (2 * layer) ** 2
        # Determine the direction
        if remainder < side // 2:
            # Right
            x = remainder - 0
            y = layer
        elif remainder < side:
            # Down
            x = side - 1
            y = layer - (remainder - side // 2)
        elif remainder < side + side // 2:
            # Left
            x = side - 1 - (remainder - side - side // 2)
            y = -layer - 1
        else:
            # Up
            x = -remainder + side + side // 2 - side // 2
            y = -layer - 1
        print(f"{x} {y}")

if __name__ == '__main__':
    solve()