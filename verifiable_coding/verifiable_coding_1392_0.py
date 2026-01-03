import sys

def solve():
    input = sys.stdin.buffer.read().split()
    x = int(input[0])
    y = int(input[1])
    print(x + y)

if __name__ == '__main__':
    solve()