import sys
import math

def solve():
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    index = 1
    results = []
    for _ in range(T):
        A = int(data[index])
        B = int(data[index+1])
        index += 2
        g = math.gcd(A, B)
        A //= g
        B //= g
        results.append(B - 1)
    print('\n'.join(map(str, results)))

if __name__ == '__main__':
    solve()