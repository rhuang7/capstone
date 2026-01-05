import sys

def solve():
    data = sys.stdin.buffer.read().split()
    X = int(data[0])
    Y = int(data[1])
    print(X + Y)

if __name__ == '__main__':
    solve()