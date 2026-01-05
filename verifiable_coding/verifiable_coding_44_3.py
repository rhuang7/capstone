import sys
import math

def solve():
    input = sys.stdin.buffer.read().split()
    t = int(input[0])
    cases = list(map(int, input[1:t+1]))
    
    for n in cases:
        res = []
        for i in range(n, 2*n):
            res.append(4*i)
        for i in range(1, n):
            res.append(4*i - 2)
        print(' '.join(map(str, res)))

if __name__ == '__main__':
    solve()