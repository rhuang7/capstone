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
        # So we should first press the first button as many times as possible to increase the first screen value
        # before pressing the second button
        # Let x be the number of times we press the first button before pressing the second button
        # Then, the number of times we can press the second button is (N - x) // B
        # The total value on the second screen is x * (N - x) // B
        # We need to maximize this expression
        # The maximum occurs when x is approximately (N / (B + 1))
        # So we can try x in the range [max(0, (N // (B + 1)) - 100), min(N, (N // (B + 1)) + 100)]
        # To avoid TLE, we can compute the optimal x directly
        # The optimal x is floor((N - 1) / (B + 1))
        x = (N - 1) // (B + 1)
        # Now compute the maximum value on the second screen
        # The number of times we can press the second button is (N - x) // B
        # The value on the second screen is x * ((N - x) // B)
        max_value = x * ((N - x) // B)
        results.append(str(max_value))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()