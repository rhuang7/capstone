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
        
        factors = []
        temp = M
        i = 2
        while i * i <= temp:
            if temp % i == 0:
                count = 0
                while temp % i == 0:
                    temp //= i
                    count += 1
                factors.append((i, count))
            i += 1
        if temp > 1:
            factors.append((temp, 1))
        
        res = set()
        for a in range(1, 10**6 + 1):
            found = False
            for (p, cnt) in factors:
                if a % p != 0:
                    continue
                if a // p > 0:
                    b = (a * p) // (M // p)
                    if b >= a and (a * b) // M == a + b:
                        found = True
                        break
            if found:
                res.add(a)
        
        res = sorted(res)
        print(len(res))
        for x in res:
            print(x)

if __name__ == '__main__':
    solve()