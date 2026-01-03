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
        passcode = (B // g) - 1
        results.append(str(passcode))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()