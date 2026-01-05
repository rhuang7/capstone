import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    idx = 1
    results = []
    for _ in range(T):
        X = int(data[idx])
        Y = int(data[idx+1])
        idx += 2
        diff = Y - X
        if diff == 0:
            results.append(0)
            continue
        min_rounds = float('inf')
        # Try all possible a and b combinations that satisfy the conditions
        # a is positive odd, b is positive even
        # We need to find a and b such that X + a - b = Y or X - b + a = Y
        # So, a - b = diff or a + b = diff
        # Try a - b = diff
        # a must be positive odd, b must be positive even
        # a = diff + b
        # a must be positive odd, so diff + b must be positive odd
        # Try b from 1 to 10^5 (since a and b are positive and diff can be large)
        # But since we need minimum rounds, we can try small b values
        for b in range(1, 100000):
            if b % 2 == 0:
                a = diff + b
                if a > 0 and a % 2 == 1:
                    min_rounds = min(min_rounds, 1)
        # Try a + b = diff
        # a must be positive odd, b must be positive even
        # a = diff - b
        # a must be positive odd, so diff - b must be positive odd
        for b in range(1, 100000):
            if b % 2 == 0:
                a = diff - b
                if a > 0 and a % 2 == 1:
                    min_rounds = min(min_rounds, 1)
        results.append(min_rounds)
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()