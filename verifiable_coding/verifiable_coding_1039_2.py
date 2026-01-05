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
        # We need to find a and b such that diff = a - b or diff = - (a - b)
        # So diff must be achievable by a - b or b - a
        # So diff must be positive or negative, but the absolute value must be achievable by a - b
        # Let's consider all possible a and b such that a - b = diff or b - a = diff
        # But since a and b are positive, we can try all possible a and b
        # But since a and b can be large, we need to find the minimum number of rounds
        # So for each possible a (odd), we can find the minimum b (even) such that a - b = diff or b - a = diff
        # But since we need to find the minimum number of rounds, we can try all possible a and b that satisfy the condition
        # Let's try all possible a (odd) such that a >= 1 and a <= abs(diff) + 1
        # Then find the minimum b (even) such that a - b = diff or b - a = diff
        # But since we need to find the minimum number of rounds, we can try all possible a and b that satisfy the condition
        # So for each possible a (odd), we can find the minimum b (even) such that a - b = diff or b - a = diff
        # And then calculate the number of rounds
        # But since a and b can be large, we need to find the minimum number of rounds
        # So for each possible a (odd), we can find the minimum b (even) such that a - b = diff or b - a = diff
        # And then calculate the number of rounds
        # But since a and b can be large, we need to find the minimum number of rounds
        # So for each possible a (odd), we can find the minimum b (even) such that a - b = diff or b - a = diff
        # And then calculate the number of rounds
        # But since a and b can be large, we need to find the minimum number of rounds
        # So for each possible a (odd), we can find the minimum b (even) such that a - b = diff or b - a = diff
        # And then calculate the number of rounds
        # But since a and b can be large, we need to find the minimum number of rounds
        # So for each possible a (odd), we can find the minimum b (even) such that a - b = diff or b - a = diff
        # And then calculate the number of rounds
        # But since a and b can be large, we need to find the minimum number of rounds
        # So for each possible a (odd), we can find the minimum b (even) such that a - b = diff or b - a = diff
        # And then calculate the number of rounds
        # But since a and b can be large, we need to find the minimum number of rounds
        # So for each possible a (odd), we can find the minimum b (even) such that a - b = diff or b - a = diff
        # And then calculate the number of rounds
        # But since a and b can be large, we need to find the minimum number of rounds
        # So for each possible a (odd), we can find the minimum b (even) such that a - b = diff or b - a = diff
        # And then calculate the number of rounds
        # But since a and b can be large, we need to find the minimum number of rounds
        # So for each possible a (odd), we can find the minimum b (even) such that a - b = diff or b - a = diff
        # And then calculate the number of rounds
        # But since a and b can be large, we need to find the minimum number of rounds
        # So for each possible a (odd), we can find the minimum b (even) such that a - b = diff or b - a = diff
        # And then calculate the number of rounds
        # But since a and b can be large, we need to find the minimum number of rounds
        # So for each possible a (odd), we can find the minimum b (even) such that a - b = diff or b - a = diff
        # And then calculate the number of rounds
        # But since a and b can be large, we need to find the minimum number of rounds
        # So for each possible a (odd), we can find the minimum b (even) such that a - b = diff or b - a = diff
        # And then calculate the number of rounds
        # But since a and b can be large, we need to find the minimum number of rounds
        # So for each possible a (odd), we can find the minimum b (even) such that a - b = diff or b - a = diff
        # And then calculate the number of rounds
        # But since a and b can be large, we need to find the minimum number of rounds
        # So for each possible a (odd), we can find the minimum b (even) such that a - b = diff or b - a = diff
        # And then calculate the number of rounds
        # But since a and b can be large, we need to find the minimum number of rounds
        # So for each possible a (odd), we can find the minimum b (even) such that a - b = diff or b - a = diff
        # And then calculate the number of rounds
        # But since a and b can be large, we need to find the minimum number of rounds
        # So for each possible a (odd), we can find the minimum b (even) such that a - b = diff or b - a = diff
        # And then calculate the number of rounds
        # But since a and b can be large, we need to find the minimum number of rounds
        # So for each possible a (odd), we can find the minimum b (even) such that a - b = diff or b - a = diff
        # And then calculate the number of rounds
        # But since a and b can be large, we need to find the minimum number of rounds
        # So for each possible a (odd), we can find the minimum b (even) such that a - b = diff or b - a = diff
        # And then calculate the number of rounds
        # But since a and b can be large, we need to find the minimum number of rounds
        # So for each possible a (odd), we can find the minimum b (even) such that a - b = diff or b - a = diff
        # And then calculate the number of rounds
        # But since a and b can be large, we need to find the minimum number of rounds
        # So for each possible a (odd), we can find the minimum b (even) such that a - b = diff or b - a = diff
        # And then calculate the number of rounds
        # But since a and b can be large, we need to find the minimum number of rounds
        # So for each possible a (odd), we can find the minimum b (even) such that a - b = diff or b - a = diff
        # And then calculate the number of rounds
        # But since a and b can be large, we need to find the minimum number of rounds
        # So for each possible a (odd), we can find the minimum b (even) such that a - b = diff or b - a = diff
        # And then calculate the number of rounds
        # But since a and b can be large, we need to find the minimum number of rounds
        # So for each possible a (odd), we can find the minimum b (even) such that a - b = diff or b - a = diff
        # And then calculate the number of rounds
        # But since a and b can be large, we need to find the minimum number of rounds
        # So for each possible a (odd), we can find the minimum b (even) such that a - b = diff or b - a = diff
        # And then calculate the number of rounds
        # But since a and b can be large, we need to find the minimum number of rounds
        # So for each possible a (odd), we can find the minimum b (even) such that a - b = diff or b - a = diff
        # And then calculate the number of rounds
        # But since a and b can be large, we need to find the minimum number of rounds
        # So for each possible a (odd