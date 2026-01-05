import sys

def solve():
    import math
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    for i in range(1, n+1):
        t = int(data[i])
        print(math.factorial(t))

if __name__ == '__main__':
    solve()