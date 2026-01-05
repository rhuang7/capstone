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
        # Then, the energy used is x + (x + 1) * (N // (B + 1)) * B
        # We need to maximize x * (x + 1) // 2
        # But we need to find the best x such that x + (x + 1) * (N // (B + 1)) * B <= N
        # Alternatively, the maximum number of times we can press the second button is (N // B)
        # But we can also press the first button before that
        # The maximum value is (N // B) * (N // B + 1) // 2
        # But we need to check if we can press the second button more times by pressing the first button first
        # So the maximum is (N // B) * (N // B + 1) // 2
        max_press = N // B
        res = max_press * (max_press + 1) // 2
        results.append(res)
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()