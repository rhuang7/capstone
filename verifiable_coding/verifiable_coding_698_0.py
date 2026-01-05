import sys
import math

def solve():
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    idx = 1
    for _ in range(T):
        A = int(input[idx])
        B = int(input[idx+1])
        idx += 2
        g = math.gcd(A, B)
        passcode = (B // g) - 1
        print(passcode)

if __name__ == '__main__':
    solve()