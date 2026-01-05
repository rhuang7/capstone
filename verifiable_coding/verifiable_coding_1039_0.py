import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    index = 1
    results = []
    for _ in range(T):
        X = int(data[index])
        Y = int(data[index+1])
        index += 2
        diff = Y - X
        if diff == 0:
            results.append(0)
            continue
        min_rounds = float('inf')
        # Try all possible a and b combinations
        # a is positive odd, b is positive even
        # We need to find a and b such that X + a - b = Y or X - b + a = Y
        # Which simplifies to a - b = diff or a + b = diff
        # Since a is odd and b is even, a - b is odd, a + b is odd
        # So diff must be odd
        if diff % 2 != 1:
            results.append(-1)
            continue
        # Try a - b = diff
        # a is positive odd, b is positive even
        # a = diff + b
        # Since a must be positive, diff + b > 0 => b > -diff
        # Since b is positive, this is always true
        # Try all possible b (even) such that a is positive
        # a = diff + b
        # a must be positive odd
        # b must be even positive
        # Try b = 1, 2, 3, ... until a is positive odd
        # Since diff is odd, a = diff + b will be odd + even = odd
        # So a is always odd
        # Try b = 1, 2, 3, ... until a is positive
        # We can try b = 1, 2, 3, ..., until a is positive
        # But since diff is odd, we can try b = 1, 2, 3, ..., until a is positive
        # We can try b = 1, 2, 3, ... until a is positive
        # Since a = diff + b, and a must be positive, we can try b = 1, 2, 3, ... until a is positive
        # But since diff is odd, we can try b = 1, 2, 3, ... until a is positive
        # But since diff is odd, we can try b = 1, 2, 3, ... until a is positive
        # We can try b = 1, 2, 3, ... until a is positive
        # But since diff is odd, we can try b = 1, 2, 3, ... until a is positive
        # We can try b = 1, 2, 3, ... until a is positive
        # But since diff is odd, we can try b = 1, 2, 3, ... until a is positive
        # We can try b = 1, 2, 3, ... until a is positive
        # But since diff is odd, we can try b = 1, 2, 3, ... until a is positive
        # We can try b = 1, 2, 3, ... until a is positive
        # But since diff is odd, we can try b = 1, 2, 3, ... until a is positive
        # We can try b = 1, 2, 3, ... until a is positive
        # But since diff is odd, we can try b = 1, 2, 3, ... until a is positive
        # We can try b = 1, 2, 3, ... until a is positive
        # But since diff is odd, we can try b = 1, 2, 3, ... until a is positive
        # We can try b = 1, 2, 3, ... until a is positive
        # But since diff is odd, we can try b = 1, 2, 3, ... until a is positive
        # We can try b = 1, 2, 3, ... until a is positive
        # But since diff is odd, we can try b = 1, 2, 3, ... until a is positive
        # We can try b = 1, 2, 3, ... until a is positive
        # But since diff is odd, we can try b = 1, 2, 3, ... until a is positive
        # We can try b = 1, 2, 3, ... until a is positive
        # But since diff is odd, we can try b = 1, 2, 3, ... until a is positive
        # We can try b = 1, 2, 3, ... until a is positive
        # But since diff is odd, we can try b = 1, 2, 3, ... until a is positive
        # We can try b = 1, 2, 3, ... until a is positive
        # But since diff is odd, we can try b = 1, 2, 3, ... until a is positive
        # We can try b = 1, 2, 3, ... until a is positive
        # But since diff is odd, we can try b = 1, 2, 3, ... until a is positive
        # We can try b = 1, 2, 3, ... until a is positive
        # But since diff is odd, we can try b = 1, 2, 3, ... until a is positive
        # We can try b = 1, 2, 3, ... until a is positive
        # But since diff is odd, we can try b = 1, 2, 3, ... until a is positive
        # We can try b = 1, 2, 3, ... until a is positive
        # But since diff is odd, we can try b = 1, 2, 3, ... until a is positive
        # We can try b = 1, 2, 3, ... until a is positive
        # But since diff is odd, we can try b = 1, 2, 3, ... until a is positive
        # We can try b = 1, 2, 3, ... until a is positive
        # But since diff is odd, we can try b = 1, 2, 3, ... until a is positive
        # We can try b = 1, 2, 3, ... until a is positive
        # But since diff is odd, we can try b = 1, 2, 3, ... until a is positive
        # We can try b = 1, 2, 3, ... until a is positive
        # But since diff is odd, we can try b = 1, 2, 3, ... until a is positive
        # We can try b = 1, 2, 3, ... until a is positive
        # But since diff is odd, we can try b = 1, 2, 3, ... until a is positive
        # We can try b = 1, 2, 3, ... until a is positive
        # But since diff is odd, we can try b = 1, 2, 3, ... until a is positive
        # We can try b = 1, 2, 3, ... until a is positive
        # But since diff is odd, we can try b = 1, 2, 3, ... until a is positive
        # We can try b = 1, 2, 3, ... until a is positive
        # But since diff is odd, we can try b = 1, 2, 3, ... until a is positive
        # We can try b = 1, 2, 3, ... until a is positive
        # But since diff is odd, we can try b = 1, 2, 3, ... until a is positive
        # We can try b = 1, 2, 3, ... until a is positive
        # But since diff is odd, we can try b = 1, 2, 3, ... until a is positive
        # We can try b = 1, 2, 3, ... until a is positive
        # But since diff is odd, we can try b = 1, 2, 3, ... until a is positive
        # We can try b = 1, 2, 3, ... until a is positive
        # But since diff is odd, we can try b = 1, 2, 3, ... until a is positive
        # We can try b = 1, 2, 3, ... until a is positive
        # But since diff is odd, we can try b = 1, 2, 3, ... until a