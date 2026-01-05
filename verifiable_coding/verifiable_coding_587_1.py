import sys
import math
from collections import defaultdict

def is_prime(x):
    if x < 2:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    sqrt_x = int(math.isqrt(x)) + 1
    for i in range(3, sqrt_x, 2):
        if x % i == 0:
            return False
    return True

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    N = int(data[0])
    girls = list(map(int, data[1:N+1]))
    
    boys = []
    for girl in girls:
        for i in range(1, 10**9 + 1):
            hate = girl ^ i
            if is_prime(hate):
                boys.append(i)
                break
    print(' '.join(map(str, boys)))

if __name__ == '__main__':
    solve()