import sys

import math

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    Xf_list = list(map(int, data[1:T+1]))
    
    for Xf in Xf_list:
        res = 0
        y = 0
        x = 0
        while True:
            p = 1
            while p * p <= y:
                p += 1
            if p * p > y:
                if p > Xf:
                    break
                x = p
                y += p * p
                res += 1
            else:
                break
        print(res)

if __name__ == '__main__':
    solve()