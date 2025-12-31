import sys

def solve():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    index = 1
    results = []
    for _ in range(n):
        a = float(data[index])
        e = int(data[index + 1])
        index += 2
        result = a * (10 ** e)
        results.append(f"{result:.2f}")
    print("\n".join(results))

if __name__ == '__main__':
    solve()