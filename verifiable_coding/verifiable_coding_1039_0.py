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
        # So, a - b = diff or a + b = diff
        # Since a is odd and b is even, a - b is odd, a + b is odd
        # So diff must be odd
        if diff % 2 == 0:
            # diff is even, so no solution
            results.append(-1)
            continue
        # Try a - b = diff
        # a is positive odd, b is positive even
        # a = diff + b
        # a must be positive odd
        # b must be positive even
        # So b can be 2, 4, 6, ...
        # Try b = 2, 4, 6, ... until a is positive
        for b in range(2, 1000000, 2):
            a = diff + b
            if a > 0 and a % 2 == 1:
                min_rounds = min(min_rounds, 1)
        # Try a + b = diff
        # a is positive odd, b is positive even
        # a = diff - b
        # a must be positive odd
        # b must be positive even
        # So b can be 2, 4, 6, ...
        # Try b = 2, 4, 6, ... until a is positive
        for b in range(2, 1000000, 2):
            a = diff - b
            if a > 0 and a % 2 == 1:
                min_rounds = min(min_rounds, 1)
        results.append(min_rounds)
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()