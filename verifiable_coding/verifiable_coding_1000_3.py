import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    for _ in range(T):
        N = int(data[idx])
        idx += 1
        A = list(map(int, data[idx:idx+N]))
        idx += N
        # Calculate the minimum speed
        total = 0
        for a in A:
            total += a
        # The minimum speed is the ceiling of total / N
        # But since we can't have fractions, we use integer division
        # If total is exactly divisible by N, then speed is total // N
        # Else, it's (total // N) + 1
        speed = total // N
        if total % N != 0:
            speed += 1
        results.append(str(speed))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()