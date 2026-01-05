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
        # Each press of the second button consumes B energy and adds the current first screen value to the second screen
        # So, we should first press the first button as many times as possible to increase the first screen value
        # Then press the second button as many times as possible
        # Let's find how many times we can press the first button before pressing the second button
        # Let x be the number of times we press the first button before pressing the second button
        # Then, the remaining energy is N - x
        # We can press the second button (N - x) // B times
        # The total value on the second screen is x * ((N - x) // B)
        # We need to maximize this expression
        # The optimal x is around (N / (B + 1))
        # We can try x in the range [max(0, (N // (B + 1)) - 100), min(N, (N // (B + 1)) + 100)]
        # This is because the maximum value of x * ((N - x) // B) is achieved when x is around N/(B+1)
        # We can try a few values around that to find the maximum
        max_val = 0
        for x in range(max(0, (N // (B + 1)) - 100), min(N, (N // (B + 1)) + 100) + 1):
            remaining = N - x
            if remaining < 0:
                continue
            count = remaining // B
            val = x * count
            if val > max_val:
                max_val = val
        results.append(str(max_val))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()