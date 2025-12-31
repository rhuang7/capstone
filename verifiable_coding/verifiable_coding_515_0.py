import sys
import math

def compute_phi(n):
    phi = n
    i = 2
    while i * i <= n:
        if n % i == 0:
            while n % i == 0:
                n //= i
            phi -= phi // i
        i += 1
    if n > 1:
        phi -= phi // n
    return phi

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    cases = list(map(int, data[1:T+1]))
    
    for N in cases:
        max_val = -1
        best_i = 2
        for i in range(2, N+1):
            phi = compute_phi(i)
            ratio = phi / i
            if ratio > max_val:
                max_val = ratio
                best_i = i
        print(best_i)

if __name__ == '__main__':
    solve()