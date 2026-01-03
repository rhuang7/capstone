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
        # We need to find the minimum number of rounds
        # For a - b = diff: a = diff + b
        # For a + b = diff: b = diff - a
        # Try all possible a and b that satisfy these conditions
        # Since a and b are positive, we can try small values of a and b
        # Try a from 1 to 1000 (since diff can be up to 2e9, but we need to find minimum rounds)
        # Try b from 1 to 1000
        # For each a and b, check if a - b = diff or a + b = diff
        # If so, compute the number of rounds
        # Also consider the case where we add a and then subtract b
        # Or subtract b and then add a
        # The minimum rounds is the minimum of all possible cases
        # Try all possible a and b combinations
        # Since a and b can be large, we need to find the minimum rounds efficiently
        # For a - b = diff: a = diff + b
        # So, for b in 1 to 1000, a = diff + b
        # Check if a is positive odd
        # For a + b = diff: b = diff - a
        # So, for a in 1 to 1000, b = diff - a
        # Check if b is positive even
        # Try all possible a and b
        # Also consider the case where we add a and then subtract b
        # Or subtract b and then add a
        # The minimum rounds is the minimum of all possible cases
        # Try all possible a and b
        # For a - b = diff
        for b in range(1, 1001):
            a = diff + b
            if a > 0 and a % 2 == 1:
                rounds = 1
                results.append(rounds)
                break
        else:
            # Try a + b = diff
            for a in range(1, 1001):
                b = diff - a
                if b > 0 and b % 2 == 0:
                    rounds = 1
                    results.append(rounds)
                    break
            else:
                # Try adding a and then subtracting b
                # Or subtracting b and then adding a
                # The minimum rounds is 2
                results.append(2)
    print('\n'.join(map(str, results)))

if __name__ == '__main__':
    solve()