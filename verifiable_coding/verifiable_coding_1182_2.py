import sys
import math

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    M_list = list(map(int, data[1:T+1]))
    
    for M in M_list:
        if M == 1:
            print(1)
            print(1)
            continue
        
        res = []
        d = 1
        while d * d <= M:
            if M % d == 0:
                a = d
                b = M // d
                if a <= b:
                    res.append(a)
                if a != b:
                    res.append(b)
            d += 1
        
        res = list(set(res))
        res.sort()
        print(len(res))
        for x in res:
            print(x)

if __name__ == '__main__':
    solve()