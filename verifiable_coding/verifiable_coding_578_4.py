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
        # To maximize the second screen, we want to press the second button as many times as possible
        # Each press of the second button consumes B energy and adds the current first screen value to the second screen
        # The first screen increases by 1 per press of the first button
        # So, the optimal strategy is to press the first button (x) times to get a value of x on the first screen,
        # then press the second button (y) times, where x * B + y <= N
        # The total value on the second screen is x * y
        # We want to maximize x * y under the constraint x * B + y <= N
        # Let's try all possible x values from 0 to N // B
        max_val = 0
        for x in range(0, N // B + 1):
            remaining = N - x * B
            y = remaining
            current = x * y
            if current > max_val:
                max_val = current
        results.append(str(max_val))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()