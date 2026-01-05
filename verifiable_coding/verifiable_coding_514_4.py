import sys

def solve():
    input = sys.stdin.buffer.read().split()
    n1 = int(input[0])
    n2 = int(input[1])
    if n1 > n2:
        print(n1 - n2)
    else:
        print(n1 + n2)

if __name__ == '__main__':
    solve()