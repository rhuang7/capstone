import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    index = 1
    results = []
    for _ in range(T):
        N = int(data[index])
        B = int(data[index+1])
        index += 2
        # To maximize the second screen, we should press the second button as many times as possible
        # Each press of the second button consumes B energy and adds the current first screen value to the second
        # So we should first press the first button (x times) to get a value x, then press the second button (y times)
        # Total energy: x + y*B = N
        # We want to maximize x*y
        # Let's find the optimal x and y
        max_val = 0
        # Try all possible x from 0 to N//B
        # But since B can be large, we can optimize
        # Let's try x = N // B
        x = N // B
        y = N - x * B
        if y >= 0:
            max_val = x * y
        # Try x = N // B + 1
        x = (N // B) + 1
        y = N - x * B
        if y >= 0:
            max_val = max(max_val, x * y)
        # Try x = N // B - 1
        x = (N // B) - 1
        y = N - x * B
        if y >= 0:
            max_val = max(max_val, x * y)
        results.append(str(max_val))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()