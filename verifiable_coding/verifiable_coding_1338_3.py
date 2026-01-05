import sys

def solve():
    import math

    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    idx = 1
    results = []

    for _ in range(n):
        a = float(data[idx])
        e = int(data[idx + 1])
        idx += 2

        value = a * (10 ** e)
        rounded = round(value, 2)
        results.append(f"{rounded:.2f}")

    print("\n".join(results))

if __name__ == '__main__':
    solve()