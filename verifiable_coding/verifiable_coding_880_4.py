import sys
import math

def solve():
    input = sys.stdin.buffer.read().split()
    n = int(input[0])
    for i in range(1, n+1):
        r = float(input[i])
        area = math.pi * r * r
        print("{0:.2f}".format(area))

if __name__ == '__main__':
    solve()