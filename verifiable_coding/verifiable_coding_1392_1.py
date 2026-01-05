import sys

def solve():
    data = sys.stdin.buffer.read().split()
    x = int(data[0])
    y = int(data[1])
    print(x + y)

if __name__ == '__main__':
    solve()