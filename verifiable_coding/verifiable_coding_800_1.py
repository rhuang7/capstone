import sys

def solve():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    arr = list(map(int, data[1:]))
    highest = max(arr)
    lowest = min(arr)
    print(f"{highest} {lowest}")

if __name__ == '__main__':
    solve()