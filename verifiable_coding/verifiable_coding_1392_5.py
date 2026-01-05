import sys

def solve():
    input = sys.stdin.buffer.read().split()
    X = int(input[0])
    Y = int(input[1])
    print(X + Y)

if __name__ == '__main__':
    solve()