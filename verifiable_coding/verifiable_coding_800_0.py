import sys

def solve():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    arr = list(map(int, data[1:]))
    print(max(arr), min(arr))

if __name__ == '__main__':
    solve()