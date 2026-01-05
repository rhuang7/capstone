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
        # The optimal strategy is to press the second button as many times as possible
        # after having accumulated enough on the first screen
        # Let x be the number of times we press the first button before pressing the second button
        # Then, the number of times we can press the second button is (N - x) // B
        # The total value on the second screen is x * (N - x) // B
        # We need to maximize this expression
        # The maximum occurs when x is as large as possible, but (N - x) is divisible by B
        # So we try x = N - (N % B) and x = N - (N % B) - 1
        # Because (N - x) must be divisible by B
        max_val = 0
        rem = N % B
        x1 = N - rem
        x2 = x1 - 1
        if x1 >= 0:
            cnt = (N - x1) // B
            max_val = x1 * cnt
        if x2 >= 0:
            cnt = (N - x2) // B
            max_val = max(max_val, x2 * cnt)
        results.append(str(max_val))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()