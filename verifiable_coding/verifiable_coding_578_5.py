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
        # Let's find the maximum number of times we can press the second button
        # Let x be the number of times we press the second button
        # Each second button press uses B energy, and we can press it x times
        # So total energy used is x * B
        # The first screen value is x (since each second button press adds the first screen value, but we need to fill it first)
        # So the maximum x is floor((N) / B)
        # But we can also press the first button before using the second button
        # So the optimal is to press the first button (x) times and then press the second button (y) times
        # Where x * 1 + y * B <= N
        # The second screen value is x * y
        # We need to maximize x * y under the constraint x + y * B <= N
        # This is a classic optimization problem
        # The maximum of x * y under x + y * B <= N is achieved when x = floor(N / (B + 1)) and y = floor(N / (B + 1))
        # Or when x is as large as possible and y is as large as possible
        # So we can try all possible x from 0 to N and find the maximum x * y
        # But since N can be up to 1e9, we need an O(1) solution
        # The optimal is to find x such that x + y * B <= N and x * y is maximized
        # Let's find the maximum x * y
        # Let's try x = floor(N / (B + 1))
        # Then y = floor((N - x) / B)
        # But this may not be optimal, so we can try x = floor(N / B) and x = floor(N / (B + 1))
        # Also, we can try x = floor(N / B) and y = floor((N - x) / B)
        # But to avoid O(1) complexity, we can use binary search or mathematical approach
        # The maximum x * y is achieved when x is as large as possible and y is as large as possible
        # So we can try x = floor(N / (B + 1)) and y = floor((N - x) / B)
        # Or x = floor(N / B) and y = floor((N - x) / B)
        # Or x = floor(N / B) and y = floor(N / B)
        # Let's try all possible x from 0 to N and find the maximum x * y
        # But since N is up to 1e9, we need an O(1) solution
        # The optimal is to find x such that x + y * B <= N and x * y is maximized
        # Let's find the maximum x * y
        # Let's try x = floor(N / (B + 1))
        # Then y = floor((N - x) / B)
        # Or x = floor(N / B)
        # Then y = floor((N - x) / B)
        # Or x = floor(N / B)
        # Then y = floor(N / B)
        # Let's compute all possible x and find the maximum x * y
        max_val = 0
        # Try x = floor(N / B)
        x = N // B
        y = (N - x) // B
        max_val = max(max_val, x * y)
        # Try x = floor(N / (B + 1))
        x = N // (B + 1)
        y = (N - x) // B
        max_val = max(max_val, x * y)
        # Try x = N // B
        x = N // B
        y = (N - x) // B
        max_val = max(max_val, x * y)
        # Try x = N // (B + 1)
        x = N // (B + 1)
        y = (N - x) // B
        max_val = max(max_val, x * y)
        # Try x = 0
        x = 0
        y = N // B
        max_val = max(max_val, x * y)
        # Try x = N
        x = N
        y = 0
        max_val = max(max_val, x * y)
        results.append(str(max_val))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()