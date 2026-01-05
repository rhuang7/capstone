import sys
import math

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    cases = list(map(int, data[1:T+1]))
    
    for N in cases:
        count = 0
        i = 1
        while i <= N:
            if i % 4 == 1:
                count += 1
            elif i % 4 == 3:
                count += 1
            i += 2
        print(count)

if __name__ == '__main__':
    solve()