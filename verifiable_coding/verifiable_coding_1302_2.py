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
            if i * (i + 1) <= N:
                count += 1
                i += 2
            else:
                break
        print(count)

if __name__ == '__main__':
    solve()