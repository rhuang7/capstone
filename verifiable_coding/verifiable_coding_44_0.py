import sys
import math

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    t = int(data[0])
    cases = list(map(int, data[1:t+1]))
    
    for n in cases:
        res = []
        for i in range(n):
            res.append(4 * n - i - 1)
        print(' '.join(map(str, res)))
        
if __name__ == '__main__':
    solve()