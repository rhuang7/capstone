import sys

def solve():
    data = sys.stdin.buffer.read().split()
    n1 = int(data[0])
    n2 = int(data[1])
    if n1 > n2:
        print(n1 - n2)
    else:
        print(n1 + n2)

if __name__ == '__main__':
    solve()