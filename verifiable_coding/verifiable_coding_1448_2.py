import sys

def solve():
    input = sys.stdin.buffer.read().split()
    idx = 0
    T = int(input[idx])
    idx += 1
    for _ in range(T):
        a = int(input[idx])
        d = int(input[idx+1])
        k = int(input[idx+2])
        n = int(input[idx+3])
        inc = int(input[idx+4])
        idx += 5
        
        current_d = d
        day = 1
        while day < n:
            day += 1
            if day % k == 0:
                current_d += inc
        print(a + (n - 1) * d + (n - 1) * (n - 2) // 2 * inc)