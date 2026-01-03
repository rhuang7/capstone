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
        # To maximize the second screen, we should use as many second button presses as possible
        # Each second button press uses B energy and adds the current first screen value to the second screen
        # So we should first fill the first screen as much as possible before using the second button
        # Let's calculate how many times we can press the first button before using the second button
        # Let's say we press the first button x times, then use the second button y times
        # Total energy: x + y*B = N
        # The value on the second screen is sum_{i=1}^y (x) = x*y
        # We want to maximize x*y under the constraint x + y*B = N
        # Let's try all possible y from 0 to N//B
        max_val = 0
        for y in range(0, N//B + 1):
            x = N - y*B
            if x >= 0:
                max_val = max(max_val, x * y)
        results.append(str(max_val))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()